#!/bin/bash

#xdotool behave_screen_edge top-left \
#exec /home/deepak/.config/rofi/bin/launcher_colorful &

cornora -tl "/home/deepak/.config/rofi/bin/launcher_colorful" -tr "xfdashboard --sm-client-disable" -bl "skippy-xd" -br "i3-msg fullscreen toggle" -v > /dev/null &


#xdotool behave_screen_edge top-right \
#exec xfdashboard --sm-client-disable &


#xdotool behave_screen_edge bottom-left \
#exec skippy-xd &