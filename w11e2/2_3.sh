#!/bin/bash
#BSUB -J w11e2_5_1_[1-203]
#BSUB -q hpc
#BSUB -W 10
#BSUB -R "rusage[mem=1024MB]"
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -o w11e2_5_1_%J_%I.out
#BSUB -e w11e2_5_1_%J_%I.err
# %J: Job ID
# %I: Job index

# Job array syntax: [start-end:step,start-end:step,...]
#NOTE: $LSB_JOBINDEX is the job index within the job array
uv run python 2_1.py $LSB_JOBINDEX