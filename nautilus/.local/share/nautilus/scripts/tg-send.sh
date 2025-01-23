#!/usr/bin/bash

set -euo pipefail

source ~/.config/secrets/tg

# From https://askubuntu.com/a/243116
# This solves issues in filenames with spaces
IFS_BAK=$IFS
IFS="
"

for file in $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS; do
	curl -sL  \
	    -F document=@"$file" \
	    -F chat_id="$CHAT_ID" \
	    -F parse_mode="HTML" \
	    -X POST \
	    https://api.telegram.org/bot$TOKEN/sendDocument
done

IFS=$IFS_BAK

