#!/bin/bash
#BSUB -J w13e1_1
#BSUB -q hpc
#BSUB -W 10
#BSUB -R "rusage[mem=1024MB]"
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -o /work3/02613/dump/w13e1_2_1%J.out
#BSUB -e /work3/02613/dump/w13e1_2_1%J.err
# %J: Job ID

uv run python 1_1.py 1> /work3/02613/dump/w13e1_2_2_%J.out 2> /work3/02613/dump/w13e1_2_2_%J.err