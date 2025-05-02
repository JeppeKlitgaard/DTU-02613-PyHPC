#!/bin/bash
#BSUB -J w11e1_1_[1-10]
#BSUB -q hpc
#BSUB -W 2
#BSUB -R "rusage[mem=512MB]"
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -o w11e1_1_%J_%I.out
#BSUB -e w11e1_1_%J_%I.err
# %J: Job ID
# %I: Job index

# Job array syntax: [start-end:step,start-end:step,...]
#NOTE: $LSB_JOBINDEX is the job index within the job array