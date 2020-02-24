import sys

_dict = {'NAMD/2.13' : '/software/NAMD/2.13/verbs/charmrun',
         'NAMD/2.13-smp' : '/software/NAMD/2.13/verbs-smp/charmrun',
         'NAMD/2.12' : '/software/NAMD/2.12/charmrun',
         'NAMD/namd-2.9-impi' : 'charmrun',
         'NAMD/namd-2.9-ompi-gcc' : 'charmrun',
         'NAMD/namd-2.9-ompi-intel' : 'charmrun'}

if __name__ == '__main__':
    arg = sys.argv[1]
    print(_dict[arg])
