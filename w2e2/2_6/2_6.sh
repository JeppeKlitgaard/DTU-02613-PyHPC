#!/bin/bash
#BSUB -J w2e2_6
#BSUB -q hpc
#BSUB -W 10
#BSUB -R "rusage[mem=128MB]"
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -o w2e2_6_%J.out
#BSUB -e w2e2_6_%J.err

python -u 2_6.py input.npy 10