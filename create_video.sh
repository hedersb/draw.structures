#!/bin/bash
#
# Parameters:
# 1 -	input format
#		images/structure2d_%06d.png
# 2 -	output file
#		video.avi


ffmpeg -f image2 -i $1 -b 800k -r 29.97 $2
