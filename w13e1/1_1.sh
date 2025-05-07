#!/bin/bash
#BSUB -J w13e1_1
#BSUB -q hpc
#BSUB -W 10
#BSUB -R "rusage[mem=1024MB]"
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -o /work3/02613/dump/w13e1_1_%J.out
#BSUB -e /work3/02613/dump/w13e1_1_%J.err
# %J: Job ID

uv run python 1_1.py