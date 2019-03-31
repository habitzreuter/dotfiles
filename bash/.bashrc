# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'

HISTCONTROL=ignoreboth

PS1='[\u@\h \W]\$ '
