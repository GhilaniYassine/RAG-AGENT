#!/bin/bash

# Add all changes
git add .

# Prompt for commit message
echo "Enter commit message:"
read commit_message

# Check if commit message is empty
if [ -z "$commit_message" ]; then
    echo "Error: Commit message cannot be empty."
    exit 1
fi

# Commit changes
git commit -m "$commit_message"

# Push to remote
echo "Pushing to remote..."
git push

echo "Changes pushed successfully!"
