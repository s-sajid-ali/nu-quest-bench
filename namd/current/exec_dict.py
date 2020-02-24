import sys

_dict = {'NAMD/2.13' : '/software/NAMD/2.13/verbs/namd2',
         'NAMD/2.13-smp' : '/software/NAMD/2.13/verbs-smp/namd2',
         'NAMD/2.12' : '/software/NAMD/2.12/namd2',
         'NAMD/namd-2.9-impi' : 'namd2',
         'NAMD/namd-2.9-ompi-gcc' : 'namd2',
         'NAMD/namd-2.9-ompi-intel' : 'namd2'}

if __name__ == '__main__':
    arg = sys.argv[1]
    print(_dict[arg])
