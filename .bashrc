#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

## PROMPT
PS1="\[\e[32m\]π "
PS1+="\[\e[33m\]\W "
PS1+="\[\e[m\]"

## ALIAS
# Utils
#alias ls='ls --color=auto'
alias ls='exa'
alias cat='bat'
alias find='fd'

[ -f "$HOME/.config/lf/diricons" ] && source "$HOME/.config/lf/diricons"
alias lf='lfrun'

# Pacman - Paru - Flatpak
alias pac='sudo pacman -S'
alias pacs='pacman -Ss'
alias pacr='sudo pacman -R'
alias pacu='sudo pacman -Syu'
alias paclo='pacman -Qdt'
alias pacro='paclo && sudo pacman -Rns $(pacman -Qtdq)'
alias pacc='sudo pacman -Scc'
alias updall='paru -Syu && flatpak update'

# Bitwarden
alias gitpat="rbw get GitHub --full | sed -n 's/^PAT.*: //p'"

# Dotfiles - GIT BARE
alias dots='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'
alias dotss='dots status'
alias dotsa='dots add'
alias dotsr='dots rm --cached'
alias dotsrf='dots rm -r --cached'
alias dotsu='dots add -u && dots commit -a && dots push'

## START
pfetch

## STARSHIP
eval "$(starship init bash)"

## DIRENV
eval "$(direnv hook bash)"

# BEGIN_KITTY_SHELL_INTEGRATION
if test -n "$KITTY_INSTALLATION_DIR" -a -e "$KITTY_INSTALLATION_DIR/shell-integration/bash/kitty.bash"; then source "$KITTY_INSTALLATION_DIR/shell-integration/bash/kitty.bash"; fi
# END_KITTY_SHELL_INTEGRATION
