#!/bin/bash
#SBATCH --account=p30157
#SBATCH --partition=short  
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=1
#SBATCH --time=00:01:00
#SBATCH --job-name=test_mpi
#SBATCH --output=outlog
#SBATCH --error=errlog

source /home/sas4990/packages/spack/share/spack/setup-env.sh
module purge all 

for i in mpi/mpich-3.3-gcc-6.4.0 \
	mpi/openmpi-1.10.5-gcc-6.4.0 mpi/openmpi-1.10.5-intel2013.2 mpi/openmpi-3.1.3-gcc-6.4.0 \
	mpi/mvapich2-gcc-4.8.3
	
do
	k=$(echo $i | cut -c5-)
	mkdir $k && cd $k/

	module load $i

	for j in {1..10}
	do
		mpirun -np 2 osu_get_bw &> bw_$j
		mpirun -np 2 osu_get_latency &> lat_$j
	done
	cd ../
done

