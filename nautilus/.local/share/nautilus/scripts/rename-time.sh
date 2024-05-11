#!/bin/bash

# From https://askubuntu.com/a/959318

IFS=$'\n'
for i in $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
do
    nameInput="$(basename -- "$i")"
    extension="${nameInput#*.}"
    filePath="$i"

    case "$(basename -- "$nameInput")" in
    *.* )
        mv -nT -- "$filePath" "$PWD/$(date '+%Y-%m-%d-%H-%M-%N').$extension"
        ;;
    * )
        mv -nT -- "$filePath" "$PWD/$RANDOM"
        ;;
    esac
done

