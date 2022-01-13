#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

## PATH
export PATH="$PATH:$HOME/.local/bin"

# SSH
export SSH_AUTH_SOCK="$XDG_RUNTIME_DIR/ssh-agent.socket"

# ENV
export VISUAL="emacsclient -c -a emacs"
export EDITOR="emacsclient -t"

# SET QT5CT FOR NOT-KDE ENV
if [ "$XDG_CURRENT_DESKTOP" != "KDE" ]
then
    export QT_QPA_PLATFORMTHEME=qt5ct
fi
