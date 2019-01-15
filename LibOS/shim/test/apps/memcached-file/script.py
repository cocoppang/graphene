#/bin/python
import sys
import os
import time

thread_idx = ['1','2','4']
workloads = ['a','b','c','d','f','g','h','i']
val_size = ['16', '128', '512']

bin_file = "memcached.manifest.sgx"

for t in thread_idx:
    for v in val_size:
        for w in workloads:
            mem_size = '0'
            if v == '16': 
                mem_size = '4096'
                mem_size2 = '4096'
            elif v == '128':
                mem_size = '8192'
                mem_size2 = '8192'
            elif v == '512':
                mem_size = '16384'
                mem_size2 = '24576'
 
            build = "bash clean.sh " + v + " " + w + " " + mem_size
            cmd = "./" + bin_file + " -u root -B file -m " + mem_size2 + " -t " + t + " -o hashpower=23 -w " + w + " -z " + v 
            print build
            print cmd
            os.system(build)
            time.sleep(10)
            os.system(cmd)
            time.sleep(10)

