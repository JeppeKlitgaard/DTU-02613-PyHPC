#!/bin/bash
#BSUB -J w3e1_3
#BSUB -q hpc
#BSUB -W 120
#BSUB -R "rusage[mem=1GB]"
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -R "select[model==XeonGold6226R]"
#BSUB -o w3e1_3_%J.out
#BSUB -e w3e1_3_%J.err
# Run nodestat -F on a host to find available nodes

python -u -m cProfile 2_1.py input.csv