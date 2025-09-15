#!/bin/bash
# setup_codon.sh - Properly configure Codon environment

# Install find_libpython
pip install find_libpython

# Find Python library path
CODON_PYTHON=$(python -c "import find_libpython; print(find_libpython.find_libpython())")
echo "CODON_PYTHON=$CODON_PYTHON" >> $GITHUB_ENV
echo "Found Python at: ${CODON_PYTHON}"

# Add Codon to PATH
echo "$HOME/.codon/bin" >> $GITHUB_PATH
