#!/bin/bash
# Print some of the environment variables Gadi sets for you at login.
echo $USER
echo $HOME
echo $PROJECT

# Set a variable of our own, so we can see whether it survives the script.
export MYSCRATCH=/scratch/$PROJECT/$USER
echo "MYSCRATCH is now $MYSCRATCH"
