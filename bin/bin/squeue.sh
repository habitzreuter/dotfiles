#!/usr/bin/env sh
#
# Check how many batch jobs I have running in the slurm cluster
#

set -uo pipefail

# Check if connection is ok
timeout 10s ssh -q cluster exit
if [ $? -ne 0 ]; then
	echo "?"
	exit
fi

JOBS=$(ssh cluster squeue | tail -n +2 | wc -l)
echo $JOBS
