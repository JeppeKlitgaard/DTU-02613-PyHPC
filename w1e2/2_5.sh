#!/bin/bash
#BSUB -J w1e2_5
#BSUB -q hpc
#BSUB -W 2
#BSUB -R "rusage[mem=128MB]"
#BSUB -n 16
#BSUB -R "span[hosts=1]"
#BSUB -o w1e2_5_%J.out
#BSUB -e w1e2_5_%J.err

echo "Done."