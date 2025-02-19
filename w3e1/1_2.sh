#!/bin/bash
#BSUB -J w3e1_2
#BSUB -q hpc
#BSUB -W 20
#BSUB -R "rusage[mem=1024MB]"
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -R "select[model==XeonGold6226R]"
#BSUB -o w3e1_2_%J.out
#BSUB -e w3e1_2_%J.err
# Run nodestat -F on a host to find available nodes

python -u 1_1.py