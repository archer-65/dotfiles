#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

## PATH
export PATH="$PATH:$HOME/.local/bin:$HOME/.nix-profile/bin"

# SSH
export SSH_AUTH_SOCK="$XDG_RUNTIME_DIR/ssh-agent.socket"

# ENV
export VISUAL="emacsclient -c -a emacs"
export EDITOR="emacsclient -t"
export NIX_PATH="$HOME/.nix-defexpr/channels/"

# SET QT5CT FOR NOT-KDE ENV
if [ "$XDG_CURRENT_DESKTOP" != "KDE" ]
then
    export QT_QPA_PLATFORMTHEME=qt5ct
fi
