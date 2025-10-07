#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Start the application using WSGI
exec gunicorn --bind 0.0.0.0:8080 wsgi:app
