import numpy as np
import matplotlib.pyplot as plt
import os
pwd = os.getcwd()

lt_key = [1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0, 256.0, 512.0,
          1024.0, 2048.0, 4096.0, 8192.0, 16384.0, 32768.0, 65536.0, 
          131072.0, 262144.0, 524288.0, 1048576.0, 2097152.0, 4194304.0]
bw_key = [1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0, 256.0, 512.0, 
          1024.0, 2048.0, 4096.0, 8192.0, 16384.0, 32768.0, 65536.0,
          131072.0, 262144.0, 524288.0, 1048576.0, 2097152.0, 4194304.0]

def get_curr_mpi_dict():
    os.chdir(pwd+'/curr_mpi_bench')
    f = open('curr_mpi_list_sorted')
    l = f.readlines()
    f.close()
    l_ = []
    for i in range(len(l)):
        # Split each string and cut the mpi/ part
        l_.append(l[i].split()[0][4:])
    del l 
    
    key_soft  = {}
    key_class = {}

    for i in range(len(l_)):
        key_soft[i+1] = l_[i]
        if l_[i][:5]=='intel':
            key_class[i+1] = 'intel'
        if l_[i][:5]=='mpich':
            key_class[i+1] = 'mpich'
        if l_[i][:8]=='mvapich2':
            key_class[i+1] = 'mvapich2'
        if l_[i][:7]=='openmpi':
            key_class[i+1] = 'openmpi'
    
    del l_ 
    
    return key_soft,key_class


def get_BW_dset(dirname,osu_ver,trials):
    os.chdir(dirname)
    bw_start = ['#', 'OSU', 'MPI_Get', 'Bandwidth', 'Test', osu_ver]

    BW = np.zeros((23,trials))
    
    for i in np.arange(1,trials+1):
        f = open('bw_'+str(i))
        l = f.readlines()
        f.close()
        
        start = -1
        for j in range(len(l)):
            l[j] = l[j].split()
            if bw_start == l[j]:
                start = j      
        
        if start==-1:
            return BW
            
        bw = []
        for k in np.arange(start+4,start+4+23):
            bw.append(np.float(l[k][1]))
        BW[:,i-1] = bw
        del bw

    return BW



def get_LT_dset(dirname,osu_ver,trials):
    os.chdir(dirname)
    lt_start = ['#', 'OSU', 'MPI_Get', 'latency', 'Test', osu_ver]

    LT = np.zeros((23,trials))
    
    for i in np.arange(1,trials+1):
        f = open('lat_'+str(i))
        l = f.readlines()
        f.close()
        
        start = -1
        for j in range(len(l)):
            l[j] = l[j].split()
            if lt_start == l[j]:
                start = j      
        
        if start==-1:
            return LT
            
        lt = []
        for k in np.arange(start+4,start+4+23):
            lt.append(np.float(l[k][1]))
        LT[:,i-1] = lt
        del lt

    return LT