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
echo "impl_1"
time python -u impl_1.py
echo "impl_2"
time python -u impl_2.py
echo "impl_3"
time python -u impl_3.py
