#!/usr/bin/env bash

# Configure X and KB
xrandr --rate 144.00
setxkbmap -layout us -variant intl &

# Polkit
/usr/lib/polkit-kde-authentication-agent-1 &

# Lockscreen manager
xss-lock -l -- betterlockscreen -l blur --off 300 &

# CoreCtrl
corectrl &

# Compositor
picom -b

# Wallpaper
nitrogen --restore &

# Notifications
dunst &

# Disk mount
udiskie --tray &

# Tray
nm-applet &

# Screenshots background
flameshot &
