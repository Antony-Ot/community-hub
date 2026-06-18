#!/bin/bash

# Exit on error
set -o errexit

# Install dependencies (Vercel automatically does this, but it's good practice to have it)
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate