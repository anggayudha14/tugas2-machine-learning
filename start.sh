#!/bin/bash

# Activate the virtual environment
. venv/bin/activate

# Start the application using Waitress
exec waitress-serve --port=5000 app:app
