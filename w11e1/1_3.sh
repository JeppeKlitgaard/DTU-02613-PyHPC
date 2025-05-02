#!/bin/bash
#BSUB -J w11e1_1_[2,29,71,73,127]
#BSUB -q hpc
#BSUB -W 2
#BSUB -R "rusage[mem=512MB]"
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -o w11e1_1_%J_%I.out
#BSUB -e w11e1_1_%J_%I.err
# %J: Job ID
# %I: Job index
#BSUB -w done(1234567)
# Example -w done(job1) # Waits for job1 to reach done state. Also works with job ids
## Possible states: done(), exit(), ended():=done() OR exit(), started():=run() OR exit() OR done()
# Default when target is job array is to wait for all jobs in the array to finish
# Can wait on specific jobs in array with [job index]. For matching array sizes, we can use [*] to match indices

# Job array syntax: [start-end:step,start-end:step,...]
#NOTE: $LSB_JOBINDEX is the job index within the job array