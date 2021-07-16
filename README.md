# PDE_Final_Report

### To creaet a video from images, use `ffmpeg` command.

command:

```ffmpeg -r 10 -start_number 1 -i filename_%03d.jpg -vcodec libx264 –pix_fmt yuv420p output_video.mp4```

`-r` : framerate

`-start_number` : number of the first file

`-i` : filename

`-vcodec` : encoding

`output_video.mp4` : output video in mp4 format
