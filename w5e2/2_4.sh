#!/bin/bash
#BSUB -J w5e2_1
#BSUB -q hpc
#BSUB -W 120
#BSUB -R "rusage[mem=1GB]"
#BSUB -n 8
#BSUB -R "span[hosts=1]"
#BSUB -R "select[model==XeonGold6226R]"
#BSUB -o w5e2_1_%J.out
#BSUB -e w5e2_1_%J.err
# Run nodestat -F on a host to find available nodes
printf "n_proc\ttime"
python -u 2_4.py 1
python -u 2_4.py 2
python -u 2_4.py 3
python -u 2_4.py 4
python -u 2_4.py 5
python -u 2_4.py 6
python -u 2_4.py 7
python -u 2_4.py 8
