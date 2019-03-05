#!/usr/bin/env sh
#
# Check how many batch jobs I have running in the slurm cluster
#

set -euo pipefail

# Check if connection is ok
timeout 10s ssh -q cluster exit
if [ $? -eq 124 ]; then
	echo "timeout"
	exit
fi

JOBS=$(ssh cluster squeue | tail -n +2 | wc -l)
echo $JOBS
