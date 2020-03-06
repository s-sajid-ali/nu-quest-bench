#!/bin/bash
#SBATCH --account=p30157
#SBATCH --partition=normal
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=24
#SBATCH --time=2:00:00
#SBATCH --job-name=test_mpi
#SBATCH --output=outlog
#SBATCH --error=errlog

source /home/sas4990/miniconda3/etc/profile.d/conda.sh
conda activate ipy3

module purge all
module load mpi/openmpi-1.10.5-gcc-4.8.3

BASE_DIR=$(pwd)

cd $BASE_DIR

gromacsver=$(echo "$gromacsmodule" </dev/null | cut -c9-)
gromacsver=$(echo $gromacsver | sed "s/\//-/g")
echo "$gromacsver" </dev/null

export OMP_NUM_THREADS=1

for run in {1..5}
do
	mpirun -np 48 /software/sources/builds/gromacs-2018.2/build_cpu/bin/gmx_mpi mdrun -s lignocellulose-rf.tpr -maxh 0.50 -resethway -noconfout -nsteps 10000 -g </dev/null &> log_$run
done

