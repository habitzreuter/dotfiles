#!/usr/bin/bash
# From https://news.ycombinator.com/item?id=35132018

for file in $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS; do
	ROTATION=$(shuf -n 1 -e '-' '')$(shuf -n 1 -e $(seq 0.05 .3))
	convert -density 150 $file \
		-linear-stretch '1.5%x2%' \
		-rotate ${ROTATION} \
		-attenuate '0.01' \
		+noise  Multiplicative \
		-colorspace 'gray' $file
done
