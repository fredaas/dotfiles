test -f /local/skel/all.bashrc && . /local/skel/all.bashrc

if [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
fi

[[ `type -t ls` == "alias" ]] && unalias ls

export PS1="\[\e[94m\]\u@\h:\W\$(__git_ps1 '[%s]')$\[\e[0m\] "

# NB! PATH must already be exported before executing this
export PATH=`perl -e 'print join(":", grep { not $seen{$_}++ } split(/:/, $ENV{PATH}))'`
