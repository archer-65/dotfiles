import os
import subprocess

from typing import List 

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

home    = os.path.expanduser('~')
scripts = home + "/.local/bin/"

mod         = "mod4"
terminal    = "alacritty"
browser     = "google-chrome-stable"
editor      = "emacsclient -c -a emacs"
filemanager = "thunar"

launcher    = scripts + "rofi_launcher"
powermenu   = scripts + "rofi_powermenu"
clipboard   = scripts + "rofi_clipboard"
volume      = scripts + "volume"

layout_test = ["monadwide", "monadtall"]

@hook.subscribe.startup_once
def autostart():
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])

colors = {
    "fg"       : ["#e0def4", "#ffffff"],
    "bg"       : ["#232136", "#232136"],
    "grey"     : ["#817c9c", "#817c9c"],
    "active"   : ["#3e8fb0", "#3e8fb0"],
    "inactive" : ["#59546d", "#59546d"],
    "urgent"   : ["#eb6f92", "#eb6f92"],
    "color1"   : ["#f6c177", "#f6c177"],
    "color2"   : ["#ea9a97", "#ea9a97"],
    "color3"   : ["#9ccfd8", "#9ccfd8"],
    "color4"   : ["#c4a7e7", "#bc96f7"],
}
    
keys = [
    #########################
    ##### QTILE CONTROL #####
    #########################
    
    # Switch between windows
    Key([mod], "h",
        lazy.layout.left(),
        desc="Move focus to left"),

    Key([mod], "l",
        lazy.layout.right(),
        desc="Move focus to right"),

    Key([mod], "j",
        lazy.layout.down(),
        desc="Move focus down"),

    Key([mod], "k",
        lazy.layout.up(),
        desc="Move focus up"),

    Key([mod], "space",
        lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h",
        lazy.layout.swap_left(),
        lazy.layout.swap_column_left(),
        lazy.layout.shuffle_left().when(layout="bsp"),
        desc="Move window to the left or swap column"),
    
    Key([mod, "shift"], "l",
        lazy.layout.swap_right(),
        lazy.layout.swap_column_right(),
        lazy.layout.shuffle_right().when(layout="bsp"),
        desc="Move window to the right or swap column"),
    
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down() ,
        desc="Move window down"),
    
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        desc="Move window up"),
    
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        desc="Grow window to the left"),
    
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        desc="Grow window to the right"),
    
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        desc="Grow window down"),
    
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        desc="Grow window up"),
    
    Key([mod], "n",
        lazy.layout.normalize(),
        desc="Reset all window sizes (secondary clients)"),

    # Monad
    Key([mod], "equal",
        lazy.layout.grow(),
        desc="Grow Monad"),
    
    Key([mod], "minus",
        lazy.layout.shrink(),
        desc="Shrink Monad"),
    
    Key([mod, "shift"], "space",
        lazy.layout.flip(),
        desc="Flip layout"),

    Key([mod], "m",
        lazy.layout.maximize(),
        desc="Toggle maximize for focused"),

    # BSP
    Key([mod, "mod1"], "j",
        lazy.layout.flip_down(),
        desc="Flip BSP down"),
    
    Key([mod, "mod1"], "k",
        lazy.layout.flip_up(),
        desc="Flip BSP up"),

    Key([mod, "mod1"], "h",
        lazy.layout.flip_left(),
        desc="Flip BSP left"),

    Key([mod, "mod1"], "l",
        lazy.layout.flip_right(),
        desc="Flip BSP right"),
    
    # Switch to next/prev
    Key([mod], "Left", lazy.screen.prev_group(), desc="Switch to previous group"),
    Key([mod], "Right", lazy.screen.next_group(), desc="Switch to next group"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    # ATM for BSP and Columns
    Key([mod, "shift"], "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "Tab", lazy.prev_layout(), desc="Toggle between layouts (backward)"),

    # Window control
    Key([mod], "w",
        lazy.window.kill(),
        desc="Kill focused window"),
    
    Key([mod], "t",
        lazy.window.toggle_floating(),
        desc="Toggle floating for focused window"),

    # Qtile utils
    Key([mod, "control"], "r",
        lazy.reload_config(),
        desc="Reload the config"),
    
    Key([mod, "shift"], "r",
        lazy.restart(),
        desc="Restart Qtile"),
    
    Key([mod, "control"], "q",
        lazy.shutdown(),
        desc="Shutdown Qtile"),

    ####################
    ##### PROGRAMS #####
    ####################

    # Terminal
    Key([mod], "Return",
        lazy.spawn(terminal),
        desc="Launch terminal"),

    # Rofi
    Key([mod], "d",
        lazy.spawn(launcher),
        desc="Rofi launcher"),
    
    Key([mod, "shift"], "q",
        lazy.spawn(powermenu),
        desc="Rofi powermenu"),

    Key([mod], "comma",
        lazy.spawn(clipboard + " copy"),
        desc="Rofi clipboard"),
    
    Key([mod], "period",
        lazy.spawn(clipboard + " paste"),
        desc="Rofi clipboard"),

    # File Manager
    Key([mod], "f",
        lazy.spawn(filemanager),
        desc="Launch file manager"),

    ## Keychord with R(un)
    KeyChord([mod], "r", [
        # Browser
        Key([], "b", lazy.spawn(browser)),
        # Editor
        Key([], "e", lazy.spawn(editor))]),

    #################
    ##### MEDIA #####
    #################

    # Volume
    Key([], "XF86AudioRaiseVolume",
        lazy.spawn(volume + " up"),
        desc="Volume up"),
    
    Key([], "XF86AudioLowerVolume",
        lazy.spawn(volume + " down"),
        desc="Volume down"),
    
    Key([], "XF86AudioMute",
        lazy.spawn(volume + " mute"),
        desc="Volume toggle mute"),
]

#groups = [Group(i) for i in "123456789"]
groups = [
    Group("1", label="一", layout="monadtall"),
    Group("2", label="二", layout="columns"),
    Group("3", label="三", layout="monadtall"),
    Group("4", label="四", layout="monadtall"),
    Group("5", label="五", layout="monadtall"),
    Group("6", label="六", layout="monadtall")
]

for i in groups:
     keys.extend([
         # mod1 + letter of group = switch to group
         Key([mod], i.name, lazy.group[i.name].toscreen(),
             desc="Switch to group {}".format(i.name)),

         # mod1 + shift + letter of group = switch to & move focused window to group
         Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
             desc="Switch to & move focused window to group {}".format(i.name)),
         # Or, use below if you prefer not to switch to that group.
         # # mod1 + shift + letter of group = move focused window to group
         # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
         #     desc="move focused window to group {}".format(i.name)),
     ])

layout_theme = {
    "border_width": 3,
    "border_focus": colors["active"],
    "border_normal": colors["inactive"],
}  

layouts = [
    layout.MonadTall(
        **layout_theme,
        margin = 10,
        #name = "Tall",
    ),
    layout.Columns(
        **layout_theme,
        margin = 10,
        grow_amount = 5,
        num_columns = 3,
        #name = "Three Col"
    ),
    layout.Bsp(
        **layout_theme,
        margin = 10,
        ratio = 1.5,
        #name = "Bsp",
    ),
    layout.Max(
        #name = "Monocle"
    ),
    layout.Floating(
        **layout_theme,
        #name = "Floating"
    ),
    # layout.MonadWide(
    #     **layout_theme,
    #     margin = 10,
    #     #name = "Mirror Tall",
    # ),
    # layout.Stack(num_stacks=2),
    # layout.Matrix(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Inconsolata Nerd Font Mono",
    fontsize=18,
    foreground=colors["fg"],
    padding=3,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(
                    text="  ",
                    font="Iosevka Nerd Font",
                    fontsize="22",
                    background=colors["color1"],
                    foreground=colors["bg"],
                    # mouse_callbacks={
                    #     "Button1": lambda: qtile.cmd_spawn("rofi -show drun -modi drun")
                    # },
                ),
                widget.TextBox(
                    text="\ue0be",
                    font="Inconsolata Nerd Font Mono",
                    fontsize="33",
                    padding=-1,
                    background=colors["color1"],
                    foreground=colors["bg"],
                ),
                widget.GroupBox(
                    font="Iosevka Nerd Font",
                    fontsize=18,
                    margin_x=6,
                    margin_y=3,
                    active=colors["active"],
                    inactive=colors["inactive"],
                    highlight_method="block",
                    block_highlight_text_color=colors["bg"],
                    this_current_screen_border=colors["active"],
                    urgent_alert_method="text",
                    urgent_text=colors["urgent"],
                    borderwidth=4,
                    rounded=True,
                ),
                widget.TextBox(
                    text="\ue0be",
                    font="Inconsolata Nerd Font Mono",
                    fontsize="33",
                    padding=-1,
                    background=colors["bg"],
                    foreground=colors["color1"],
                ),
                widget.WindowName(
                    font="Iosevka Nerd Font",
                    fontsize=18,
                    background=colors["color1"],
                    foreground=colors["bg"],
                ),
                widget.Prompt(
                    background=colors["color1"],
                    foreground=colors["bg"],
                    font="Inconsolata Nerd Font",
                    fontsize=18,
                ),
                widget.TextBox(
                    text="\ue0be",
                    font="Inconsolata Nerd Font Mono",
                    fontsize="33",
                    padding=-1,
                    background=colors["color1"],
                    foreground=colors["bg"],
                ),
                widget.Spacer(),
                widget.TextBox(
                    text="\ue0be",
                    font="Inconsolata Nerd Font Mono",
                    fontsize="33",
                    padding=-1,
                    background=colors["bg"],
                    foreground=colors["grey"],
                ),
                widget.Systray(
                    background=colors["grey"],
                    foreground=colors["fg"],
                    icons_size=24,
                    padding=10,
                ),
                widget.Sep(
                    padding=10,
                    linewidth=0,
                    background=colors["grey"],
                ),
                widget.TextBox(
                    text="\ue0be",
                    font="Inconsolata Nerd Font Mono",
                    fontsize="33",
                    padding=-1,
                    background=colors["grey"],
                    foreground=colors["color4"],
                ),
                 widget.CurrentLayoutIcon(
                     custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                     scale=0.6,
                     padding=0,
                     background=colors["color4"],
                     foreground=colors["fg"],
                     font="Iosevka Nerd Font",
                     fontsize=14,
                 ),
                widget.CurrentLayout(
                    font="Iosevka Nerd Font",
                    fontsize=18,
                    background=colors["color4"],
                    foreground=colors["fg"],
                ),
                widget.TextBox(
                    text="\ue0be",
                    font="Inconsolata Nerd Font Mono",
                    fontsize="33",
                    padding=-1,
                    background=colors["color4"],
                    foreground=colors["urgent"],
                ),
                widget.TextBox(
                    text=" ",
                    font="Iosevka Nerd Font",
                    fontsize=22,
                    padding=0,
                    background=colors["urgent"],
                    foreground=colors["fg"],
                ),
                widget.CheckUpdates(
                    distro="Arch_checkupdates",
                    font="Iosevka Nerd Font",
                    fontsize=18,
                    background=colors["urgent"],
                    colour_have_updates=colors["fg"],
                    colour_no_updates=colors["fg"],
                    display_format="{updates} updates",
                    no_update_string="Nothing",
                    update_interval="3600",
                ),
                widget.TextBox(
                    text="\ue0be",
                    font="Inconsolata Nerd Font Mono",
                    fontsize="33",
                    padding=-1,
                    background=colors["urgent"],
                    foreground=colors["color2"],
                ),
                 widget.TextBox(
                    text=" ",
                    font="Iosevka Nerd Font",
                    fontsize=22,
                    padding=0,
                    background=colors["color2"],
                    foreground=colors["fg"],
                ),
                widget.ThermalSensor(
                    treshold=75,
                    background=colors["color2"],
                    foreground=colors["fg"],
                    padding=10,
                    fontsize=18,
                    update_interval=10,
                ),
                 widget.TextBox(
                    text="\ue0be",
                    font="Inconsolata Nerd Font Mono",
                    fontsize="33",
                    padding=-1,
                    background=colors["color2"],
                    foreground=colors["active"],
                ),
                widget.TextBox(
                    text=" ",
                    font="Iosevka Nerd Font",
                    fontsize=22,
                    padding=0,
                    background=colors["active"],
                    foreground=colors["fg"],
                ),
                widget.DF(
                    fmt="{}",
                    font="Iosevka Nerd Font",
                    fontsize=18,
                    partition="/home",
                    format="{uf}{m} ({r:.0f}%)",
                    visible_on_warn=False,
                    background=colors["active"],
                    foreground=colors["fg"],
                    padding=5,
                    update_interval=3600,
                    #mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("kitty -e bashtop")},
                ),
                widget.TextBox(
                    text="\ue0be",
                    font="Inconsolata Nerd Font Mono",
                    fontsize="33",
                    padding=-1,
                    background=colors["active"],
                    foreground=colors["color4"],
                ),
                widget.TextBox(
                    text=" ",
                    font="Iosevka Nerd Font",
                    fontsize=22,
                    foreground=colors["fg"],
                    background=colors["color4"],
                    padding=0,
                    #mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("kitty -e bashtop")},
                ),
                widget.Memory(
                    background=colors["color4"],
                    foreground=colors["fg"],
                    font="Iosevka Nerd Font",
                    fontsize=18,
                    format="{MemUsed: .0f} MB",
                    update_interval=10,
                    #mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("kitty -e bashtop")},
                ),
                widget.TextBox(
                    text="\ue0be",
                    font="Inconsolata Nerd Font Mono",
                    fontsize="33",
                    padding=-1,
                    background=colors["color4"],
                    foreground=colors["color3"],
                ),
                widget.TextBox(
                    text="墳 ",
                    font="Iosevka Nerd Font",
                    fontsize=22,
                    background=colors["color3"],
                    foreground=colors["bg"],
                ),
                widget.PulseVolume(
                    background=colors["color3"],
                    foreground=colors["bg"],
                    font="Iosevka Nerd Font",
                    fontsize=18,
                    limit_max_volume=True,
                    volume_app="pavucontrol",
                    mouse_callbacks={"Button3": lambda: qtile.cmd_spawn("alacritty -e pulsemixer")},
                ),
                # # Doesn't work with Spotify so its disabled!
                # # widget.TextBox(
                # #    text="\u2572",
                # #    font="Inconsolata Nerd Font Mono",
                # #    fontsize="33",
                # #    padding=0,
                # #    background=colors[13],
                # #    foreground=colors[0],
                # # ),
                # # widget.Mpd2(
                # #   background=colors[13],
                # #   foreground=colors[0],
                # #   idle_message=" ",
                # #   idle_format="{idle_message} Not Playing",
                # #   status_format="  {artist}/{title} [{updating_db}]",
                # #   font="Iosevka Nerd Font",
                # #   fontsize=16,
                # # ),
                # This one works with Spotify, enable if you want!
                widget.Mpris2(
                   background=colors["color3"],
                   foreground=colors["bg"],
                   name="spotify",
                   objname="org.mpris.MediaPlayer2.spotify",
                   fmt="\u2572   {}",
                   display_metadata=["xesam:title", "xesam:artist"],
                   scroll_chars=30,
                   scroll_wait_intervals=50,
                   font="Iosevka Nerd Font",
                   fontsize=18,
                ),
                widget.TextBox(
                    text="\ue0be",
                    font="Inconsolata Nerd Font Mono",
                    fontsize="33",
                    padding=-1,
                    background=colors["color3"],
                    foreground=colors["color1"],
                ),
                widget.TextBox(
                    text="   ",
                    font="Iosevka Nerd Font",
                    fontsize=22,
                    padding=0,
                    background=colors["color1"],
                    foreground=colors["bg"],
                ),
                widget.Clock(
                    font="Iosevka Nerd Font",
                    foreground=colors["bg"],
                    background=colors["color1"],
                    fontsize=18,
                    format="%d %b, %A",
                ),
                # widget.TextBox(
                #     text="\ue0be",
                #     font="Inconsolata Nerd Font Mono",
                #     fontsize="33",
                #     padding=-1,
                #     background=colors["color1"],
                #     foreground=colors["color"],
                # ),
                widget.TextBox(
                    text="\u2572  ",
                    font="Iosevka Nerd Font",
                    fontsize=22,
                    padding=0,
                    background=colors["color1"],
                    foreground=colors["bg"],
                ),
                widget.Clock(
                    font="Iosevka Nerd Font",
                    foreground=colors["bg"],
                    background=colors["color1"],
                    fontsize=18,
                    format="%R",
                ),
                widget.Sep(
                    padding=10,
                    linewidth=0,
                    background=colors["color1"],
                ),
            ],
            size=35,
            background=colors["bg"],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry
    ],
    **layout_theme,
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
