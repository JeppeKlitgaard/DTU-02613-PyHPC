#!/bin/bash
#BSUB -J w1e2_6
#BSUB -q hpc
#BSUB -W 2
#BSUB -R "rusage[mem=128MB]"
#BSUB -n 64
#BSUB -R "span[hosts=1]"
#BSUB -o w1e2_6_%J.out
#BSUB -e w1e2_6_%J.err

echo "Done."