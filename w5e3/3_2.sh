#!/bin/bash
#BSUB -J w5e3_2
#BSUB -q hpc
#BSUB -W 120
#BSUB -R "rusage[mem=256MB]"
#BSUB -n 16
#BSUB -R "span[hosts=1]"
#BSUB -R "select[model==XeonGold6226R]"
#BSUB -o w5e3_2_%J.out
#BSUB -e w5e3_2_%J.err
# Run nodestat -F on a host to find available nodes
printf "n_proc\ttime\n"
python -u 3_2.py 1
python -u 3_2.py 2
python -u 3_2.py 3
python -u 3_2.py 4
python -u 3_2.py 5
python -u 3_2.py 6
python -u 3_2.py 7
python -u 3_2.py 8
python -u 3_2.py 9
python -u 3_2.py 10
python -u 3_2.py 11
python -u 3_2.py 12
python -u 3_2.py 13
python -u 3_2.py 14
python -u 3_2.py 15
python -u 3_2.py 16
