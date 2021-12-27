#!/usr/bin/env bash

## Author : archer-65

theme="style"

dir="$HOME/.config/rofi/launcher"

rofi -no-lazy-grab -show drun \
-modi run,drun,window \
-theme $dir/$theme
