import sys

_dict = { 'lammps/lammps-10Feb2015/lammps-gcc' : 'lmp_mpi',
          'lammps/lammps-22Aug18' : 'lmp',
          'lammps/lammps-31Mar17-mpich' : 'lmp_Questmpich',
          'lammps/lammps-gcc' : 'lmp_Quest_gcc',
          'lammps/lammps-gcc-mkl' : 'lmp_Quest_gcc_mkl',
          'lammps/lammps-intel' : 'lmp_Quest_intel',
          'lammps/lammps-intel-mkl' : 'lmp_Quest_intel_mkl',
          'lammps/lammps-mpich' : 'lmp_Questmpich'}

if __name__ == '__main__':
    arg = sys.argv[1]
    print(_dict[arg])
