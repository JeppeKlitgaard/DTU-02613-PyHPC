#!/bin/bash
#BSUB -J w3e1_5
#BSUB -q hpc
#BSUB -W 5
#BSUB -R "rusage[mem=16GB]"
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -R "select[model==XeonGold6226R]"
#BSUB -o w3e1_5_%J.out
#BSUB -e w3e1_5_%J.err
# Run nodestat -F on a host to find available nodes

../.venv/bin/python -u 1_5.py

lscpu
