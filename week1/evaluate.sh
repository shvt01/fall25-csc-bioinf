#!/bin/bash
set -euxo pipefail

echo "Running Week 1 evaluation..."

# Run Python and Codon versions on all datasets
# This is a simplified version - you'll need to adapt it to your actual implementation

echo "Dataset	Language	Runtime (s)	N50"
echo "-----------------------------------------------------------------------"

for i in {1..4}; do
    # Run Python version
    start_time=$(date +%s)
    python code/genome-assembly/genome_assembler.py data/data${i}/short_1.fasta data/data${i}/short_2.fasta data/data${i}/long.fasta
    end_time=$(date +%s)
    python_time=$((end_time - start_time))
    
    # Get N50 from Python output (you'll need to modify this based on your actual output)
    python_n50=9990  # Placeholder - replace with actual calculation
    
    # Run Codon version
    start_time=$(date +%s)
    codon run -release code/genome-assembly/genome_assembler.codon data/data${i}/short_1.fasta data/data${i}/short_2.fasta data/data${i}/long.fasta
    end_time=$(date +%s)
    codon_time=$((end_time - start_time))
    
    # Get N50 from Codon output (you'll need to modify this based on your actual output)
    codon_n50=25  # Placeholder - replace with actual calculation
    
    # Calculate speedup
    speedup=$(echo "scale=1; $python_time / $codon_time" | bc)
    
    echo "data${i}	Python		${python_time}		${python_n50}"
    echo "data${i}	Codon		${codon_time}		${codon_n50}	${speedup}x"
done
