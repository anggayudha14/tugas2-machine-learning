#!/bin/bash

# Activate the virtual environment
. venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Add changes
git add .

# Commit changes
git commit -m "Automated update"

# Push to GitHub
git push origin main
