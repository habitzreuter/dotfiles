#!/usr/bin/bash

# TODO Handle filenames with spaces
for picture in $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS; do
	convert -strip -interlace Plane -gaussian-blur 0.05 -resize 50% -quality 60% "$picture" "$picture"
done
