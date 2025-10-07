#!/bin/bash

# Activate the virtual environment
. venv/bin/activate

# Start the application using Flask
exec python -m flask run --host=0.0.0.0
