#/bin/bash

make clean
make SGX=1 VAL_SIZE=$1 WORKLOAD=$2 MAXMEM=$3
make SGX_RUN=1 VAL_SIZE=$1 WORKLOAD=$2 MAXMEM=$3

