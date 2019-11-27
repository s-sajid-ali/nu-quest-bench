#!/bin/bash
#SBATCH --account=p30157
#SBATCH --partition=short  
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=00:45:00
#SBATCH --exclusive
#SBATCH --job-name=test_mpi
#SBATCH --output=outlog
#SBATCH --error=errlog

source /home/sas4990/packages/spack/share/spack/setup-env.sh
module purge all 

for i in ydnn6yi x5jirha ek3oorz 7x34z32 u5qxmse jozbe3t
do
	mkdir $i
	cd $i/
	spack load --dependencies /$i 
	
	echo "MPI benchmark and library info :" >> mpi_config
	spack find -ldv /$i >> mpi_config
	echo -e "\n\n" >> mpi_config
	echo "mpirun location :" >> mpi_config
	which mpirun >> mpi_config
	echo -e "\n\n" >> mpi_config
	echo "Linking info for benchmark executable :" >> mpi_config
	ldd $(spack location -i /$i)/libexec/osu-micro-benchmarks/mpi/one-sided/osu_get_bw >> mpi_config

	for j in {1..20}
	do
		srun --mpi=pmi2 osu_get_bw &> bw_$j
		srun --mpi=pmi2 osu_get_latency &> lat_$j
	done
	cd ../
done

