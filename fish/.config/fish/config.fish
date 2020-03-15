set fish_greeting

set -gx EDITOR vim
set -gx LANG en_US.UTF-8
set -gx PATH ~/bin/(hostname) ~/bin ~/.local/bin /usr/local/bin /usr/bin /bin /sbin /usr/sbin


function fish_prompt
    printf '%s' (prompt_pwd)
    printf ' > '
end

# Enable fzf keybindings
function fish_user_key_bindings
	fzf_key_bindings
end

if test (tty) = /dev/tty1
	eval sway
end
