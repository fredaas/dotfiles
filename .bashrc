test -f /local/skel/all.bashrc && . /local/skel/all.bashrc

if [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
fi

[[ `type -t ls` == "alias" ]] && unalias ls

export PS1="\[\e[38;5;222m\]\u@\h:\W\$(__git_ps1 '[%s]')\$\[\e[0m\] "

alias print-path="tr ':' '\n' <<< $PATH"
alias print-man="man -k . -s"
alias rsync-all="rsync -avPI --exclude='.git'"
