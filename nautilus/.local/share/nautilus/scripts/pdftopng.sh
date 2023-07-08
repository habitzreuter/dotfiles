#!/bin/bash
IFS=$'\n'
for picture in $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS; do
	png_file=`echo "$picture" | sed 's/\.\w*$/.png/'`
	convert -density 300 $picture -quality 90 $png_file
done
