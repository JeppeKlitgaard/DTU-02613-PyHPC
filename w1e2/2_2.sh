#!/bin/bash
#BSUB -J w1e2_2
#BSUB -q hpc
#BSUB -W 1
#BSUB -R "rusage[mem=128MB]"
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -N
#BSUB -B

sleep 120