# ffmpeg -y -i /Users/tiagorodriguez/Desktop/HLS_testbed/TEST_VIDEO/XXXXXXXX2014-V000100.mov /Users/tiagorodriguez/Desktop/HLS_testbed/OUTPUT_TEST/XXXXXXXX2014-V000100.m3u8







ffmpeg -y -i /Users/tiagorodriguez/Desktop/HLS_testbed/TEST_VIDEO/XXXXXXXXT114-V015600.mp4 -c:a aac -strict experimental -ac 2 -b:a 64k -ar 44100 -c:v libx264 -vf scale=1920:1080 -crf 18 -r 24 -g 72 -f hls -hls_time 9 -hls_list_size 0 -s 1920x1080 /Users/tiagorodriguez/Desktop/HLS_testbed/0/XXXXXXXX2015-V000700_.m3u8
ffmpeg -y -i /Users/tiagorodriguez/Desktop/HLS_testbed/TEST_VIDEO/XXXXXXXXT114-V015600.mp4 -c:a aac -strict experimental -ac 2 -b:a 64k -ar 44100 -c:v libx264 -vf scale=1280:720 -crf 22 -r 24 -g 72 -f hls -hls_time 9 -hls_list_size 0 -s 1280x720 /Users/tiagorodriguez/Desktop/HLS_testbed/1/XXXXXXXX2015-V000700_.m3u8
ffmpeg -y -i /Users/tiagorodriguez/Desktop/HLS_testbed/TEST_VIDEO/XXXXXXXXT114-V015600.mp4 -c:a aac -strict experimental -ac 2 -b:a 64k -ar 44100 -c:v libx264 -vf scale=960:540 -crf 24 -r 24 -g 72 -f hls -hls_time 9 -hls_list_size 0 -s 960x540 /Users/tiagorodriguez/Desktop/HLS_testbed/2/XXXXXXXX2015-V000700_.m3u8
ffmpeg -y -i /Users/tiagorodriguez/Desktop/HLS_testbed/TEST_VIDEO/XXXXXXXXT114-V015600.mp4 -c:a aac -strict experimental -ac 2 -b:a 64k -ar 44100 -c:v libx264 -vf scale=640:360 -crf 26 -r 24 -g 72 -f hls -hls_time 9 -hls_list_size 0 -s 640x360 /Users/tiagorodriguez/Desktop/HLS_testbed/3/XXXXXXXX2015-V000700_.m3u8
ffmpeg -y -i /Users/tiagorodriguez/Desktop/HLS_testbed/TEST_VIDEO/XXXXXXXXT114-V015600.mp4 -c:a aac -strict experimental -ac 2 -b:a 32k -ar 22050 -c:v libx264 -vf scale=640:360 -crf 32 -r 24 -g 72 -f hls -hls_time 9 -hls_list_size 0 -s 640x360 /Users/tiagorodriguez/Desktop/HLS_testbed/4/XXXXXXXX2015-V000700_.m3u8

# ffmpeg -y -i /Users/tiagorodriguez/Desktop/HLS_testbed/TEST_VIDEO/HARSPU27T313-V043500_DTH.mp4 -c:a aac -strict experimental -ac 2 -b:a 96k -ar 44100 -c:v libx264 -pix_fmt yuv420p -profile:v main -level 3.2 -maxrate 2M -bufsize 6M -crf 18 -r 24 -g 72 -f hls -hls_time 9 -hls_list_size 0 -s 1280x720 /Users/tiagorodriguez/Desktop/HLS_testbed/OUTPUT_TEST/1280x720.m3u8

# ffmpeg -y -framerate 24 -i 720/sintel_trailer_2k_%4d.png -i sintel_trailer-audio.flac -c:a aac -strict experimental -ac 2 -b:a 64k -ar 44100 -c:v libx264 -pix_fmt yuv420p -profile:v baseline -level 1.3 -maxrate 192K -bufsize 1M -crf 18 -r 10 -g 30 -f hls -hls_time 9 -hls_list_size 0 -s 320x180 ts/320x180.m3u8
# ffmpeg -y -framerate 24 -i 720/sintel_trailer_2k_%4d.png -i sintel_trailer-audio.flac -c:a aac -strict experimental -ac 2 -b:a 64k -ar 44100 -c:v libx264 -pix_fmt yuv420p -profile:v baseline -level 2.1 -maxrate 500K -bufsize 2M -crf 18 -r 10 -g 30  -f hls -hls_time 9 -hls_list_size 0 -s 480x270 ts/480x270.m3u8
# ffmpeg -y -framerate 24 -i 720/sintel_trailer_2k_%4d.png -i sintel_trailer-audio.flac -c:a aac -strict experimental -ac 2 -b:a 96k -ar 44100 -c:v libx264 -pix_fmt yuv420p -profile:v baseline -level 3.1 -maxrate 1M -bufsize 3M -crf 18 -r 24 -g 72 -f hls -hls_time 9 -hls_list_size 0 -s 640x360 ts/640x360.m3u8
# ffmpeg -y -framerate 24 -i 720/sintel_trailer_2k_%4d.png -i sintel_trailer-audio.flac -c:a aac -strict experimental -ac 2 -b:a 96k -ar 44100 -c:v libx264 -pix_fmt yuv420p -profile:v main -level 3.2 -maxrate 2M -bufsize 6M -crf 18 -r 24 -g 72 -f hls -hls_time 9 -hls_list_size 0 -s 1280x720 ts/1280x720.m3u8
