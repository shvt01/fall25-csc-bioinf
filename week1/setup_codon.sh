#!/bin/bash

# Check if Python is installed
if command -v python3 &> /dev/null; then
    echo "Found Python at: $(which python3)"
    python3 --version
elif command -v python &> /dev/null; then
    echo "Found Python at: $(which python)"
    python --version
else
    echo "Python not found. Please install Python."
    exit 1
fi

# Check if pip is installed
if command -v pip3 &> /dev/null; then
    echo "Found pip at: $(which pip3)"
    pip3 --version
elif command -v pip &> /dev/null; then
    echo "Found pip at: $(which pip)"
    pip --version
else
    echo "pip not found. Please install pip."
    exit 1
fi

echo "Setup completed successfully!"
