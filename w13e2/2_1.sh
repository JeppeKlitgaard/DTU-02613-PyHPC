#!/bin/bash
#BSUB -J w13e2_1
#BSUB -q hpc
#BSUB -W 10
#BSUB -R "rusage[mem=6GB]"
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -R "select[model==XeonGold6226R]"
#BSUB -o w13e2_1_%J.out
#BSUB -e w13e2_1_%J.err
# %J: Job ID

uv run python 2_1.py