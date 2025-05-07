#!/bin/bash
#BSUB -J w13e2_2
#BSUB -q hpc
#BSUB -W 10
#BSUB -R "rusage[mem=2GB]"
#BSUB -n 8
#BSUB -R "span[hosts=1]"
#BSUB -R "select[model==XeonGold6226R]"
#BSUB -o w13e2_2_%J.out
#BSUB -e w13e2_2_%J.err
# %J: Job ID

NUM_THREADS=8
OMP_NUM_THREADS=$NUM_THREADS
MPI_NUM_THREADS=$NUM_THREADS
MKL_NUM_THREADS=$NUM_THREADS
OPENBLAS_NUM_THREADS=$NUM_THREADS

uv run python 2_1.py
