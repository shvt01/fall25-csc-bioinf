#!/bin/bash
set -euxo pipefail

# Check if virtual environment exists and activate it
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
else
    echo "Virtual environment not found. Using system Python."
    # Install required packages if not already installed
    pip install biopython numpy matplotlib || echo "Some packages might not be available"
fi

# Function to run and time a command and compute N50
run_and_time() {
    local cmd=$1
    local lang=$2
    local dataset=$3
    
    start_time=$(date +%s)
    output=$($cmd 2>&1)
    end_time=$(date +%s)
    runtime=$((end_time - start_time))
    
    # Compute N50 from output
    n50=$(echo "$output" | python week1/code/genome-assembly/compute_n50.py | awk '{print $2}')
    
    printf "%s\t%s\t\t%d\t\t%s\n" "$dataset" "$lang" "$runtime" "$n50"
}

echo "Dataset	Language	Runtime	N50"
echo "-----------------------------------------------------------------------"

# Test datasets
datasets=("data1" "data2" "data3" "data4")

for dataset in "${datasets[@]}"; do
    # Python version
    run_and_time "python week1/code/genome-assembly/main.py week1/data/${dataset}" "python" "$dataset"
    
    # Codon version
    run_and_time "codon run -release -plugin seq week1/code/genome-assembly/simple_assembler.codon week1/data/${dataset}" "codon" "$dataset"
done

# Deactivate virtual environment if it was activated
if [ -f "venv/bin/activate" ]; then
    deactivate
fi
