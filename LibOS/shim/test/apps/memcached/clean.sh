#/bin/bash

make clean
make SGX=1 && make SGX_RUN=1
