#!/bin/bash

# Install NLTK
# pip install nltk

# Create target directory if it doesn't exist
TARGET_DIR="/home/appuser/nltk_data"
mkdir -p $TARGET_DIR

# Download NLTK data to a temporary directory
TEMP_DIR=$(mktemp -d)
python3 -m nltk.downloader -d $TEMP_DIR all

# Move downloaded data to the target directory
mv $TEMP_DIR/* $TARGET_DIR

# Clean up temporary directory
rm -rf $TEMP_DIR

echo "NLTK data has been downloaded and moved to $TARGET_DIR"