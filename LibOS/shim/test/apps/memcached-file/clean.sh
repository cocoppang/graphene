#/bin/bash

make clean
make SGX=1 VAL_SIZE=128 WORKLOAD=a 
make SGX_RUN=1 VAL_SIZE=128 WORKLOAD=a 

