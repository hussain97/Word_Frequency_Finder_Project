#!/bin/bash

# Run unit tests
echo "Running unit tests..."
python -m unittest unit_testing.py

# Check if the tests passed
if [ $? -eq 0 ]; then
    echo "Tests passed. Starting the main application..."
    python word_frequency.py
else
    echo "Tests failed. Exiting..."
    exit 1
fi
