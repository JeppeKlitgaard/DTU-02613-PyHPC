#!/bin/bash
#BSUB -J w1e2_3
#BSUB -q hpc
#BSUB -W 1
#BSUB -R "rusage[mem=128MB]"
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -R "select[model==XeonE5_2660v3]"
# Run nodestat -F on a host to find available nodes

lscpu