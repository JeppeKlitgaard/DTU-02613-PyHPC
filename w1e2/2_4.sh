#!/bin/bash
#BSUB -J w1e2_4
#BSUB -q hpc
#BSUB -W 2
#BSUB -R "rusage[mem=128MB]"
#BSUB -n 4
#BSUB -R "span[hosts=1]"
#BSUB -o w1e2_4_%J.out
#BSUB -e w1e2_4_%J.err

echo "Done."