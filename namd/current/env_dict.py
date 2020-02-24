import sys

_dict = { 'lammps/lammps-10Feb2015/lammps-gcc' : 'OMPI_MCA_rmaps_base_oversubscribe=1',
          'lammps/lammps-22Aug18' : 'OMPI_MCA_rmaps_base_oversubscribe=1',
          'lammps/lammps-31Mar17-mpich' : ' ',
          'lammps/lammps-gcc' : ' ',
          'lammps/lammps-gcc-mkl' : ' ',
          'lammps/lammps-intel' : ' ',
          'lammps/lammps-intel-mkl' : ' ',
          'lammps/lammps-mpich' : ' '}

if __name__ == '__main__':
    arg = sys.argv[1]
    print(_dict[arg])
