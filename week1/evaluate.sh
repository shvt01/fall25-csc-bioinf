#!/bin/bash
set -euxo pipefail

echo "Running Week 1 evaluation..."
echo "Dataset	Language	Runtime (s)	N50"
echo "-----------------------------------------------------------------------"

for i in {1..4}; do
    # Run Python version only
    start_time=$(date +%s)
    python code/genome-assembly/genome_assembler.py data/data${i}/short_1.fasta data/data${i}/short_2.fasta data/data${i}/long.fasta
    end_time=$(date +%s)
    python_time=$((end_time - start_time))
    
    # Placeholder for N50 - you'll need to implement actual calculation
    python_n50=0
    
    echo "data${i}	Python	${python_time}	${python_n50}"
done
