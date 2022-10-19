# /bin/bash

# Open Zoom
/bin/zoom

resulution=$(xdpyinfo | awk '/dimensions/{print $2}')

# ffmpeg -video_size 1920x1080 -framerate 25 -f x11grab -i :0.0+0,0 -f alsa -ac 2 -i hw:1 output.mp4
# recordmydesktop --width 1920 --height 1080 --full-shots --fps 15 --channels 1 --device hw:1,0 --delay 10
# ffmpeg -video_size 1920x1080 -framerate 25 -f x11grab -i :0.0+0,0 -f pulse -ac 2 -i default output.mp4


#python3 zoom_bot.py