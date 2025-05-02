#!/bin/bash
#BSUB -J w11e2_5_2
#BSUB -q hpc
#BSUB -W 2
#BSUB -R "rusage[mem=512MB]"
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -o output/w11e2_5_2_%J_%I.out
#BSUB -e output/w11e2_5_2_%J_%I.err
# %J: Job ID
# %I: Job index
#BSUB -w done(w11e2_5_1_)

# Job array syntax: [start-end:step,start-end:step,...]
#NOTE: $LSB_JOBINDEX is the job index within the job array
uv run python 2_1.py $LSB_JOBINDEX