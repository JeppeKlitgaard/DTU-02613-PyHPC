#!/bin/bash
#BSUB -J w5e1_4
#BSUB -q hpc
#BSUB -W 120
#BSUB -R "rusage[mem=4096MB]"
#BSUB -n 16
#BSUB -R "span[hosts=1]"
#BSUB -R "select[model==XeonGold6226R]"
#BSUB -o w6e1_4_%J.out
#BSUB -e w6e1_4_%J.err
# Run nodestat -F on a host to find available

printf "n_proc\tn_run\ttime\n"

python -u 1_4.py 16 3 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 15 3 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 14 3 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 13 3 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 12 3 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 11 3 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 10 3 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 9 3 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 8 3 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 7 3 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 6 3 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 5 3 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 4 3 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 3 3 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 2 3 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 1 3 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 16 2 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 15 2 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 14 2 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 13 2 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 12 2 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 11 2 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 10 2 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 9 2 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 8 2 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 7 2 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 6 2 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 5 2 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 4 2 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 3 2 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 2 2 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 1 2 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 16 1 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 15 1 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 14 1 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 13 1 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 12 1 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 11 1 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 10 1 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 9 1 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 8 1 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 7 1 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 6 1 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 5 1 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 4 1 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 3 1 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 2 1 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy
python -u 1_4.py 1 1 /dtu/projects/02613_2025/data/celeba/celeba_100K.npy