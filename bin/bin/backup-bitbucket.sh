#!/bin/bash
# Requires https://github.com/samkuehn/bitbucket-backup

source ~/.config/secrets/bitbucket_backup_password

bitbucket-backup -u $USER -p $PASSWORD -l ~/src/bitbucket-backup
