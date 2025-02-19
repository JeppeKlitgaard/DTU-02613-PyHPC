#!/bin/bash
#BSUB -J sleeper
#BSUB -q hpc
#BSUB -W 2
#BSUB -R "rusage[mem=128MB]"
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -o sleeper_%J.out
#BSUB -e sleeper_%J.err

sleep 60