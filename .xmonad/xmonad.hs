--
-- IMPORTS
--

import XMonad
import Data.Monoid
import System.Exit

-- Hooks
import XMonad.Hooks.DynamicLog
import XMonad.Hooks.SetWMName
import XMonad.Hooks.EwmhDesktops

-- Layout
import XMonad.Layout.Magnifier
import XMonad.Layout.ThreeColumns
import XMonad.Layout.Spacing
import XMonad.Layout.LayoutModifier
import XMonad.Layout.NoBorders

-- Util
import XMonad.Util.Cursor (setDefaultCursor)
import XMonad.Util.EZConfig
import XMonad.Util.Loggers
import XMonad.Util.Run (spawnPipe, hPutStrLn)
import XMonad.Util.SpawnOnce (spawnOnce)
import XMonad.Util.Ungrab

-- Qualified Imports
import qualified XMonad.StackSet as W
import qualified Data.Map        as M

-- The preferred terminal program, which is used in a binding below and by
-- certain contrib modules.
--
myTerminal      = "alacritty"

-- Whether focus follows the mouse pointer.
myFocusFollowsMouse :: Bool
myFocusFollowsMouse = True

-- Whether clicking on a window to focus also passes the click to the window
myClickJustFocuses :: Bool
myClickJustFocuses = False

-- Width of the window border in pixels.
--
myBorderWidth = 3

-- modMask lets you specify which modkey you want to use. The default
-- is mod1Mask ("left alt").  You may also consider using mod3Mask
-- ("right alt"), which does not conflict with emacs keybindings. The
-- "windows key" is usually mod4Mask.
--
myModMask = mod4Mask

-- The default number of workspaces (virtual screens) and their names.
-- By default we use numeric strings, but any string may be used as a
-- workspace name. The number of workspaces is determined by the length
-- of this list.
--
-- A tagging example:
--
-- > workspaces = ["web", "irc", "code" ] ++ map show [4..9]
--
myWorkspaces = ["一","二","三","四","五","六"]

-- Border colors for unfocused and focused windows, respectively.
--
myNormalBorderColor  = "#abb2bf"
myFocusedBorderColor = "#61afef"

------------------------------------------------------------------------
-- Key bindings. Add, modify or remove key bindings here.
--
myKeys conf@(XConfig {XMonad.modMask = modm}) = M.fromList $

    -- launch a terminal
    [ ((modm, xK_t),
       spawn $ XMonad.terminal conf)

    -- launch dmenu
    , ((modm, xK_p),
       spawn "dmenu_run")

    -- close focused window
    , ((modm, xK_w),
       kill)

     -- Rotate through the available layout algorithms
    , ((modm, xK_backslash),
       sendMessage NextLayout)

    --  Reset the layouts on the current workspace to default
    , ((modm .|. shiftMask, xK_space ),
       setLayout $ XMonad.layoutHook conf)

    -- Resize viewed windows to the correct size
    , ((modm, xK_r),
       refresh)

    -- Move focus to the next window
    , ((modm, xK_j),
       windows W.focusDown)

    -- Move focus to the previous window
    , ((modm, xK_k),
       windows W.focusUp)

    -- Move focus to the master window
    , ((modm, xK_m),
       windows W.focusMaster)

    -- Swap the focused window and the master window
    , ((modm, xK_Return),
       windows W.swapMaster)

    -- Swap the focused window with the next window
    , ((modm .|. shiftMask, xK_j),
       windows W.swapDown)

    -- Swap the focused window with the previous window
    , ((modm .|. shiftMask, xK_k),
       windows W.swapUp)

    -- Shrink the master area
    , ((modm, xK_h),
       sendMessage Shrink)

    -- Expand the master area
    , ((modm, xK_l),
       sendMessage Expand)

    -- Push window back into tiling
    , ((modm, xK_f),
       withFocused $ windows . W.sink)

    -- Increment the number of windows in the master area
    , ((modm, xK_comma),
       sendMessage (IncMasterN 1))

    -- Deincrement the number of windows in the master area
    , ((modm, xK_period),
       sendMessage (IncMasterN (-1)))

    -- Quit xmonad
    , ((modm .|. shiftMask, xK_q),
       io exitSuccess)

    -- Restart xmonad
    , ((modm, xK_q),
       spawn "xmonad --recompile; xmonad --restart")

    ]
    ++

    --
    -- mod-[1..9], Switch to workspace N
    -- mod-shift-[1..9], Move client to workspace N
    --
    [((m .|. modm, k), windows $ f i)
        | (i, k) <- zip (XMonad.workspaces conf) [xK_1 .. xK_9]
        , (f, m) <- [(W.greedyView, 0), (W.shift, shiftMask)]]
    
------------------------------------------------------------------------
-- Mouse bindings: default actions bound to mouse events
--
myMouseBindings (XConfig {XMonad.modMask = modm}) = M.fromList

    -- mod-button1, Set the window to floating mode and move by dragging
    [ ((modm, button1), \w -> focus w >> mouseMoveWindow w
                                       >> windows W.shiftMaster)

    -- mod-button2, Raise the window to the top of the stack
    , ((modm, button2), \w -> focus w >> windows W.shiftMaster)

    -- mod-button3, Set the window to floating mode and resize by dragging
    , ((modm, button3), \w -> focus w >> mouseResizeWindow w
                                       >> windows W.shiftMaster)

    -- you may also bind events to the mouse scroll wheel (button4 and button5)
    ]
    
------------------------------------------------------------------------
-- Layouts:

-- You can specify and transform your layouts by modifying these values.
-- If you change layout bindings be sure to use 'mod-shift-space' after
-- restarting (with 'mod-q') to reset your layout state to the new
-- defaults, as xmonad preserves your old layout settings by default.
--
-- The available layouts.  Note that each layout is separated by |||,
-- which denotes layout choice.
--

myLayout = tiled ||| Mirror tiled ||| Full ||| threeCol
  where
     -- Three columns
     threeCol = smartSpacing 6 $ ThreeColMid nmaster delta ratio
    
     -- default tiling algorithm partitions the screen into two panes
     tiled   = smartSpacing 6 $ Tall nmaster delta ratio

     mySpacing :: Integer -> l a -> ModifiedLayout XMonad.Layout.Spacing.Spacing l a
     mySpacing i = spacingRaw False (Border i i i i) True (Border i i i i) True

     -- The default number of windows in the master pane
     nmaster = 1

     -- Default proportion of screen occupied by master pane
     ratio   = 1/2

     -- Percent of screen to increment by when resizing panes
     delta   = 3/100

------------------------------------------------------------------------
-- Window rules:

-- Execute arbitrary actions and WindowSet manipulations when managing
-- a new window. You can use this to, for example, always float a
-- particular program, or have a client always appear on a particular
-- workspace.
--
-- To find the property name associated with a program, use
-- > xprop | grep WM_CLASS
-- and click on the client you're interested in.
--
-- To match on the WM_NAME, you can use 'title' in the same way that
-- 'className' and 'resource' are used below.
--
myManageHook = composeAll
    [ className =? "TelegramDesktop" --> doShift "一"
    , className =? "Discord"         --> doShift "一"
    , className =? "discord"         --> doShift "一"
    , className =? "trayer"          --> doIgnore
    , resource  =? "desktop_window"  --> doIgnore
    , resource  =? "kdesktop"        --> doIgnore ]

------------------------------------------------------------------------
-- Event handling

-- * EwmhDesktops users should change this to ewmhDesktopsEventHook
--
-- Defines a custom handler function for X Events. The function should
-- return (All True) if the default handler is to be run afterwards. To
-- combine event hooks use mappend or mconcat from Data.Monoid.
--
myEventHook = fullscreenEventHook

------------------------------------------------------------------------
-- Status bars and logging

-- Perform an arbitrary action on each internal state change or X event.
-- See the 'XMonad.Hooks.DynamicLog' extension for examples.
--
myLogHook = return ()

myXMobarPP :: PP
myXMobarPP = def
    { ppSep = magenta " • "
    , ppTitleSanitize = xmobarStrip
    , ppCurrent = wrap (blue "[") (blue "]")
    , ppHidden = white . wrap " " ""
    , ppHiddenNoWindows = lowWhite . wrap " " ""
    , ppUrgent = red . wrap (yellow "!") (yellow "!")
    --, ppOrder = \[ws, l, _, wins] -> [ws, l, wins]
    --, ppExtras          = [logTitle formatFocused formatUnfocused]  -- 0.17
    }
  where
    -- formatFocused   = wrap (white    "[") (white    "]") . magenta . ppWindow  -- 0.17
    -- formatUnfocused = wrap (lowWhite "[") (lowWhite "]") . blue    . ppWindow  -- 0.17 

    -- ppWindow :: String -> String
    -- ppWindow = xmobarRaw . (\w -> if null w then "untitled" else w) . shorten 30

    blue, lowWhite, magenta, red, white, yellow :: String -> String
    magenta = xmobarColor "#ff79c6" ""
    blue = xmobarColor "#bd93f9" ""
    white = xmobarColor "#f8f8f2" ""
    yellow = xmobarColor "#f1fa8c" ""
    red = xmobarColor "#ff5555" ""
    lowWhite = xmobarColor "#bbbbbb" ""

------------------------------------------------------------------------
-- Startup hook

-- Perform an arbitrary action each time xmonad starts or is restarted
-- with mod-q.  Used by, e.g., XMonad.Layout.PerWorkspace to initialize
-- per-workspace layout choices.
--
-- By default, do nothing.
myStartupHook :: X ()
myStartupHook = do
  -- Kill before start
  spawn "killall trayer"

  -- Start always
  spawnOnce "picom"
  spawnOnce "dunst"
  spawnOnce "nitrogen --restore" -- Wallpaper
  spawn "sleep 1 && trayer --edge top --align right --SetDockType true --SetPartialStrut true --expand true --widthtype request --padding 2 --iconspacing 8 --transparent true --alpha 0 --tint 0x5f5f5f --height 25" -- Tray
  spawnOnce "nm-applet" -- Network Manager Applet in Tray

  -- Various
  setDefaultCursor xC_left_ptr  -- Left Ptr set in X
  setWMName "LG3D"  -- Set WMName for JAVA Apps

------------------------------------------------------------------------
-- Now run xmonad with all the defaults we set up.
-- Run xmonad with the settings you specify. No need to modify this.
--
main :: IO ()
main = xmonad 
     . ewmh
     =<< statusBar "xmobar ~/.xmonad/xmobar.hs" myXMobarPP toggleStrutsKey defaults
  where
    toggleStrutsKey :: XConfig Layout -> (KeyMask, KeySym)
    toggleStrutsKey XConfig { modMask = m } = (m, xK_n)

-- A structure containing your configuration settings, overriding
-- fields in the default config. Any you don't override, will
-- use the defaults defined in xmonad/XMonad/Config.hs
--
-- No need to modify this.
--
defaults = def {
      -- simple stuff
        terminal           = myTerminal,
        focusFollowsMouse  = myFocusFollowsMouse,
        clickJustFocuses   = myClickJustFocuses,
        borderWidth        = myBorderWidth,
        modMask            = myModMask,
        workspaces         = myWorkspaces,
        normalBorderColor  = myNormalBorderColor,
        focusedBorderColor = myFocusedBorderColor,

      -- key bindings
        keys               = myKeys,
        mouseBindings      = myMouseBindings,

      -- hooks, layouts
        layoutHook         = myLayout,
        manageHook         = myManageHook,
        handleEventHook    = myEventHook,
        logHook            = myLogHook,
        startupHook        = myStartupHook
    }
