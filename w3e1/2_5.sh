#!/bin/bash
#BSUB -J w3e2_5
#BSUB -q hpc
#BSUB -W 5
#BSUB -R "rusage[mem=16GB]"
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -o w3e2_5_%J.out
#BSUB -e w3e2_5_%J.err
# Run nodestat -F on a host to find available nodes

../.venv/bin/python -u 2_5.py 256
../.venv/bin/python -u 2_5.py 512
../.venv/bin/python -u 2_5.py 1024
