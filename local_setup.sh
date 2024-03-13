#!/bin/bash
# To run this file, use the command: source setup.sh
# This file must have execute permission.
# Run chmod +x setup.sh to give it execute permission.
# To stop the virtual env, use the command: deactivate

# Check if the virtual environment already exists
if [ ! -d ".venv" ]; then
    # Create a virtual environment
    python -m venv .venv
fi

# Activate the virtual environment
source .venv/bin/activate || exit 1

# Install project dependencies
pip install -r requirements.txt || exit 1

echo "Virtual environment activated and dependencies installed successfully."
