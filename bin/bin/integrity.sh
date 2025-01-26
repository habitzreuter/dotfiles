#!/bin/bash
set -euf -o pipefail

# Finds all files recursively and calculates checksums
# These checksums are saved to a file
# To check the data integrity, you should compare the saved checksums: md5sum -c md5sum.txt

find -type f \( -not -name "md5sum.txt" \) -exec md5sum '{}' \; > md5sum.txt

