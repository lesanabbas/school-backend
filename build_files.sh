#!/bin/bash

# Set the virtual environment directory name
VENV_DIR="venv"

# Install system dependencies
echo "Installing system dependencies..."
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    sudo apt-get update
    sudo apt-get install -y libxml2-dev libxslt1-dev
elif [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    brew install libxml2 libxslt
    brew link libxml2 --force
    brew link libxslt --force
fi

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv $VENV_DIR

# Activate virtual environment
echo "Activating virtual environment..."
source $VENV_DIR/bin/activate

# Check if the virtual environment was activated successfully
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "Virtual environment activated successfully."

    # Build project
    echo "Building the project..."
    python3 -m pip install --upgrade pip  # Upgrade pip to the latest version
    python3 -m pip install -r requirements.txt

    # Make Migrations
    echo "Make Migrations"
    python3 manage.py makemigrations --noinput

    # Apply Migrations
    echo "Applying Migrations"
    python3 manage.py migrate --noinput

    # Collect Static Files
    echo "Collecting Static Files"
    python3 manage.py collectstatic --noinput --clear

    echo "BUILD END"
else
    echo "Failed to activate virtual environment."
    exit 1
fi
