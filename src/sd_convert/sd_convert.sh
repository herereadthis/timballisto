#!/bin/bash

# command to convert one file to 24fps
# ffmpeg -i M2U00006.MPG -vf "yadif=0:-1:0,framerate=24:interp_start=0:interp_end=255:scene=100" -c:v libx264 -crf 18 -c:a copy output_24.mp4

# command to convert one file to 30fps
# ffmpeg -i M2U00006.MPG -vf "setpts=PTS*1001/1000,yadif=0:-1:0,framestep=2" -r 30 -c:v libx264 -crf 18 -c:a copy output_30.mp4

# Directory containing the input videos
input_dir="input_videos"

# Create directories for 24fps and 30fps copies
mkdir -p 24fps
mkdir -p 30fps

# Loop through each video file in the input directory
for video_file in "${input_dir}"/*.MPG; do
    # Extract the filename without extension
    filename=$(basename -- "$video_file")
    filename_no_ext="${filename%.*}"

    # Deinterlace and create 24fps copy
    ffmpeg -i "${video_file}" -vf "yadif=0:-1:0,framerate=24:interp_start=0:interp_end=255:scene=100" \
    -c:v libx264 -crf 18 -c:a copy "24fps/${filename_no_ext}_24fps.mp4"

    # Deinterlace and create 30fps copy
    ffmpeg -i "${video_file}" -vf "setpts=PTS*1001/1000,yadif=0:-1:0,framestep=2" -r 30 \
    -c:v libx264 -crf 18 -c:a copy "30fps/${filename_no_ext}_30fps.mp4"
done
