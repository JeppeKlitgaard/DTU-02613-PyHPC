#!/bin/bash
#BSUB -J w5e1_5
#BSUB -q hpc
#BSUB -W 120
#BSUB -R "rusage[mem=4096MB]"
#BSUB -n 32
#BSUB -R "span[hosts=1]"
#BSUB -R "select[model==XeonGold6226R]"
#BSUB -o w6e1_5_%J.out
#BSUB -e w6e1_5_%J.err
# Run nodestat -F on a host to find available

lscpu
printf "n_proc\tn_run\ttime\n"
numactl --interleave=all python -u 1_4_one_read.py /dtu/projects/02613_2025/data/celeba/celeba_100K.npy