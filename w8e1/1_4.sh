#!/bin/bash
#BSUB -J w8e1_2
#BSUB -q hpc
#BSUB -W 120
#BSUB -R "rusage[mem=4096MB]"
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -R "select[model==XeonGold6226R]"
#BSUB -o w8e1_2_%J.out
#BSUB -e w8e1_2_%J.err
# Run nodestat -F on a host to find available

/usr/bin/time -f"mem=%M KB runtime=%e s"  uv run python -u 1_4.py 1_3.parquet