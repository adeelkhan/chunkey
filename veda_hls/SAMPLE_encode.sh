#! /bin/bash

echo "Input full filepath : "
read MEZZ_FILE

DIR=$(dirname "${MEZZ_FILE}")
FILE=$(basename "${MEZZ_FILE}")
VIDID="${FILE%.*}"

## run ffmpeg command
ffmpeg -y -i ${MEZZ_FILE} -c:a aac -strict experimental -ac 2 -b:a 96k -ar 44100 \
-c:v libx264 -pix_fmt yuv420p -profile:v main -level 3.2 -maxrate 2M -bufsize 6M \
-crf 18 -r 24 -g 72 -f hls -hls_time 9 -hls_list_size 0 -s 1280x720 ${DIR}/${VIDID}.m3u8

