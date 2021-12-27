Config { overrideRedirect = True
       , font     = "xft:iosevka-12, Source Han Sans JP:size=12"
       , bgColor  = "#5f5f5f"
       , fgColor  = "#f8f8f2"
       , position = Top --Size L 100 25
       , allDesktops = True
       , persistent  = True
       , commands = [ Run Cpu
                        [ "-L", "3"
                        , "-H", "50"
                        , "--high"  , "red"
                        , "--normal", "green"
                        ] 10
                    , Run Memory ["--template", "Mem: <usedratio>%"] 10
                    , Run Swap [] 10
                    , Run Date "%a %Y-%m-%d <fc=#8be9fd>%H:%M</fc>" "date" 10
                    , Run Com ".xmonad/scripts/tray-padding-icon.sh" [] "tray" 10
                    , Run StdinReader
                    ]
       , sepChar  = "%"
       , alignSep = "}{"
       , template = "%StdinReader% }{%cpu% | %memory% * %swap% | %date% | %tray% "
       }
