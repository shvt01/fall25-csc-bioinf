#!/bin/bash
set -euxo pipefail

echo "Running Week 1 evaluation..."
echo "Dataset	Language	Runtime (s)	N50"
echo "-----------------------------------------------------------------------"

for i in {1..4}
do
    start_time=$(date +%s)
    python code/genome-assembly/genome_assembler.py data/data${i}/short_1.fasta data/data${i}/short_2.fasta data/data${i}/long.fasta
    end_time=$(date +%s)
    runtime=$((end_time - start_time))
    
    # For now, we'll use a placeholder for N50
    n50=0
    
    echo "data${i}	Python	${runtime}	${n50}"
done
