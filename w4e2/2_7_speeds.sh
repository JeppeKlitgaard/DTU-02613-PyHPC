#!/bin/bash
#BSUB -J w3e1_3
#BSUB -q hpc
#BSUB -W 120
#BSUB -R "rusage[mem=1GB]"
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -R "select[model==XeonGold6226R]"
#BSUB -o w3e1_3_%J.out
#BSUB -e w3e1_3_%J.err
# Run nodestat -F on a host to find available nodes

# LINE_PROFILE=1 uv run python -u 2_4.py "/dtu/projects/02613_2025/data/locations/locations_1000.csv"
# LINE_PROFILE=1 uv run kernprof -lvr 2_7.py "/dtu/projects/02613_2025/data/locations/locations_5000.csv"
DATA_FILE="/dtu/projects/02613_2025/data/locations/locations_5000.csv"

echo "2_3"
time uv run python -u 2_3.py "$DATA_FILE"
echo "2_4"
time uv run python -u 2_4.py "$DATA_FILE"
echo "2_7"
time uv run python -u 2_7.py "$DATA_FILE"