from os import path
import subprocess
import platform

from typing import List 

from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy

from settings.theme import colors

# Get hostname
hostname = platform.uname().node

# Expand every important dir
home       = path.expanduser('~')
scripts    = path.join(home, ".local", "bin")
qtile_path = path.join(home, ".config", "qtile")

# Mod key and useful programs
mod         = "mod4"
terminal    = "alacritty"
browser     = "google-chrome-stable"
editor      = "emacsclient -c -a emacs"
filemanager = "thunar"

# Rofi launchers
launcher    = path.join(scripts, "rofi_launcher")
powermenu   = path.join(scripts, "rofi_powermenu")
clipboard   = path.join(scripts, "rofi_clipboard")
emoji       = path.join(scripts, "rofi_emoji")

# Media scripts
volume      = path.join(scripts, "volume")

# Widget commands for callback
update      = terminal + " -e sudo pacman -Syu"
mixer       = terminal + " -e pulsemixer"

@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(qtile_path, "autostart.sh")])

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


    ################
    ##### XF86 #####
    ################

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

    ###################
    ##### GENERAL #####
    ###################
    
    ##### Rofi #####
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
        desc="Rofi clipboard direct paste"),

    Key([mod], "slash",
        lazy.spawn(emoji),
        desc="Rofi emoji"),

    Key([mod], "p",
        lazy.spawn("rofi-rbw"),
        desc="Rofi RBW"),

    ##### FLAMESHOT #####

    # Full capture
    Key([], 'Print',
        lazy.spawn("flameshot full -c"),
        desc="Full screenshot"),

    # Open GUI
    Key([mod], 'Print',
        lazy.spawn("flameshot gui"),
        desc="Capture GUI"),

    ##### APPS #####
    
    # Terminal
    Key([mod], "Return",
        lazy.spawn(terminal),
        desc="Launch terminal"),


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
]

groups = [
    Group("1", label="一", layout="monadtall"),
    Group("2", label="二", layout="columns"),
    Group("3", label="三", layout="monadtall"),
    Group("4", label="四", layout="monadtall"),
    Group("5", label="五", layout="monadtall"),
    Group("6", label="六", layout="monadtall"),
]

# groups = [
#     Group("1", label="", layout="monadtall"),
#     Group("2", label="", layout="columns"),
#     Group("3", label="", layout="monadtall"),
#     Group("4", label="", layout="monadtall"),
#     Group("5", label="", layout="monadtall"),
#     Group("6", label="", layout="monadtall"),
# ]

for i in groups:
    keys.extend([
        # Switch to group
         Key([mod], i.name, lazy.group[i.name].toscreen(),
             desc="Switch to group {}".format(i.name)),

         # Switch to & move focused window to group
         Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
             desc="Switch to & move focused window to group {}".format(i.name)),
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
    ),
    layout.Columns(
        **layout_theme,
        margin = 10,
        grow_amount = 5,
        num_columns = 3,
    ),
    layout.Bsp(
        **layout_theme,
        margin = 10,
        ratio = 1.5,
    ),
    layout.Max(),
    layout.Floating(
        **layout_theme,
    ),
]

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='bitwarden'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry
        Match(wm_class='pinentry-gtk-2'),  # GPG key password entry
    ],
    **layout_theme,
)

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

def open_updates():
    qtile.cmd_spawn(update)

def open_mixer():
    qtile.cmd_spawn(mixer)

def base(fg='fg', bg='bg'):
    return {
        'foreground': colors[fg],
        'background': colors[bg],
    }

# def separator(fg='fg', bg='bg'):
#     return widget.TextBox(
#         **base(fg, bg),
#         text="\ue0be",
#         font="Iosevka Nerd Font",
#         fontsize=33,
#         padding=-1
#     )

def sep(fg='fg', bg='bg'):
     return widget.Sep(
         **base(fg, bg),
         padding = 8,
         linewidth = 0,
     )

def laptop_extra():
    global hostname
    if hostname == 'quietfrost':
        widgets_list = [
            sep(),
        ]
    else:
        widgets_list = [
            #sep(),
            
            widget.Backlight(
                **base(fg='bg', bg='color1'),
                format=' {percent:2.0%}',
                backlight_name='amdgpu_bl0',
                brightness_file='brightness',
                max_brightness_file='max_brightness',
                change_command='xbacklight -set {0}',
                step=5,
                padding=10,
            ),

            #sep(),
            
            widget.Battery(
                **base(fg='bg', bg='color1'),
                low_foreground=colors['urgent'],
                format='{char}{percent:2.0%}({hour:d}:{min:02d})',
                charge_char='',
                full_char=' ',
                discharge_char=' ',
                empty_char=' ',
                battery=1,
                low_percentage=0.15,
                notify_below=0.1,
                padding=10,
            ),

            sep(),
        ]
    return widgets_list

screens= [
    Screen(
        top=bar.Bar(
            [
                ### LEFT 
                widget.GroupBox(
                    padding=8,
                    active=colors["fg"],
                    inactive=colors["fg"],
                    highlight_method="block",
                    this_current_screen_border=colors["grey"],
                    urgent_alert_method="text",
                    urgent_text=colors["urgent"],
                    disable_drag=True,
                ),
                
                widget.Spacer(),

                ### CENTER
                
                # widget.Mpris2(
                #     **base(fg='fg', bg='bg'),
                #     fmt="  {}",
                #     name="spotify",
                #     objname="org.mpris.MediaPlayer2.spotify",
                #     display_metadata=["xesam:title", "xesam:artist"],
                #     scroll_chars=15,
                #     scroll_interval=0.5,
                #     scroll_wait_intervals=8,
                #     padding=8,
                # ),


                ### RIGHT
                
                widget.Spacer(),

                widget.CurrentLayoutIcon(
                    **base(fg='bg', bg='fg'),
                    custom_icon_paths=[path.join(qtile_path, "icons")],
                    scale=0.7,
                    padding=8,
                ),

                sep(),
                
                widget.CheckUpdates(
                    **base(fg='bg', bg='color3'),
                    distro="Arch_checkupdates",
                    colour_have_updates=colors["bg"],
                    colour_no_updates=colors["bg"],
                    display_format=" {updates} updates",
                    no_update_string=" no updates",
                    update_interval=1800,
                    padding=8,
                    mouse_callbacks={"Button1": open_updates},
                ),

                sep(),

                widget.CPU(
                    **base(fg='bg', bg='color2'),
                    format="  {load_percent}%",
                    update_interval=5,
                    padding=8,
                ),
                
                sep(),
                
                widget.ThermalSensor(
                    **base(fg='bg', bg='urgent'),
                    foreground_alert=colors["urgent"],
                    #font='Font Awesome 5 Free Solid',
                    tag_sensor='Tctl' if hostname == 'quietfrost' else None,
                    fmt=" {}",
                    treshold=75,
                    update_interval=5,
                    padding=8,
                ),

                sep(),

                widget.Memory(
                    **base(fg='bg', bg='color4'),
                    format="{MemUsed: .0f} MB",
                    update_interval=5,
                    padding=8,
                ),

                sep(),

                widget.PulseVolume(
                    **base(fg='bg', bg='color1'),
                    fmt=" {}",
                    limit_max_volume=True,
                    volume_app="pavucontrol",
                    padding=8,
                    mouse_callbacks={"Button2": open_mixer},
                ),

            ]
            +
            
            laptop_extra()

            +
            [
                widget.Clock(
                    **base(fg='bg', bg='active'),
                    format=" %R",
                    padding=8,
                ),

                sep(),
                
                widget.Systray(
                    **base(bg='inactive'),
                    padding=8,
                    icon_size=24,
                ),

                sep(bg='inactive'),
            ],
            size=34 if hostname == 'quietfrost' else 32,
            background=colors["bg"],
         ),
     ),
]

widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=20 if hostname == 'quietfrost' else 18,
    foreground=colors["fg"],
    padding=3,
)

extension_defaults = widget_defaults.copy()

main = None

dgroups_key_binder = None
dgroups_app_rules  = []

focus_on_window_activation = "smart"

follow_mouse_focus = True
bring_front_click  = False
cursor_warp        = False

reconfigure_screens = True

auto_minimize   = True
auto_fullscreen = True

wmname = "LG3D"
