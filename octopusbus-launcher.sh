#!/bin/bash

# navigate to script directory
cd "$(dirname "$0")"

# create log dir and file, set "latest" symlink to current log
LOGDIR="$(pwd)/logs"
LOGFILE="$LOGDIR/octopusbus-$(date +"%Y%m%d_%H%M%S").txt"
mkdir -p $LOGDIR
touch $LOGFILE
ln -sf $LOGFILE $LOGDIR/octopusbus-latest.txt
echo "Writing to logfile: $LOGFILE"

# execute python script in a new named tmux session "octopusbus"
# note: python -u flag disables buffering writes to stdout
tmux new-session -d -s octopusbus "python -u octopusbus.py 2>&1 | tee -a $LOGFILE"
