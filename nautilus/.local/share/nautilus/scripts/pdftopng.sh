#!/bin/bash
IFS=$'\n'
# See https://stackoverflow.com/a/53180170 for permission
for picture in $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS; do
	png_file=`echo "$picture" | sed 's/\.\w*$/.png/'`
	convert -background white -alpha remove -alpha off -density 300 $picture -quality 90 $png_file
done
