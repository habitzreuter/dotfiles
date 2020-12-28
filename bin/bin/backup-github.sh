#!/bin/bash
# Requires https://github.com/josegonzalez/python-github-backup

source ~/.config/secrets/github_backup_token

github-backup $USER -t $TOKEN --all -o ~/src/github-backup
