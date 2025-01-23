#!/bin/bash
# This scripts checks each backup repository and sends a notification if any of
# them haven't been backed up in more than two weeks.

# Define the number of seconds in two weeks for comparison
two_weeks_seconds=$((14 * 24 * 60 * 60))

current_timestamp=$(date +%s)

# Loop over directories in the parent directory
for dir in ./backup-*; do
    if [ -d "$dir" ]; then
        echo "Processing directory: $dir"
	
	# Extract date of last archive
	#echo $last_archive
	last_archive=$(borg list $dir | tail -n 1)
	date_time_str=$(echo "$last_archive" | awk '{print $2, $3, $4}')
	timestamp=$(date -d "$date_time_str" +%s)

	# Calculate the difference in seconds
	diff_seconds=$((current_timestamp - timestamp))

	# Compare the difference
	if [ "$diff_seconds" -gt "$two_weeks_seconds" ]; then
	    ~/bin/notify "Warning: $dir hasn't been backup up in two weeks."
	fi
    fi
done

