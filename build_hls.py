#! usr/bin/env python

import os
import sys

"""
Encode streams of input -> output for HLS five stream video

NOTE: Just a test, so will need greater looking into

Generate master manifest, upload (easy, via boto) to output bucket

"""

'''
https://s3.amazonaws.com/veda-testoutput/HLS_TEST/XXXXXXXX2015-V000700_.m3u8

#EXTM3U
#EXT-X-STREAM-INF:BANDWIDTH=192000,RESOLUTION=320x180
OUTPUT_TEST/XXXXXXXX2015-V000700_.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=500000,RESOLUTION=480x270
OUTPUT_TEST/XXXXXXXX2015-V000700_.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=1000000,RESOLUTION=640x360
OUTPUT_TEST/XXXXXXXX2015-V000700_.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=2000000,RESOLUTION=1280x720
OUTPUT_TEST/XXXXXXXX2015-V000700_.m3u8
'''



WORKDIR = os.path.dirname(__file__)

FFBEGIN = "ffmpeg -y -i /Users/tiagorodriguez/Desktop/HLS_testbed/TEST_VIDEO/XXXXXXXXT114-V015600.mp4 -c:a aac -strict experimental -ac 2 "

TRANSCODE_PROFILES = {
    "0" : {
        'scale' : "1920:1080",
        'audio_depth' : "64k",
        'rate_factor' : "18",
        'fps' : "29.97",
    },
    "1" : {
        'scale' : "1280:720",
        'audio_depth' : "64k",
        'rate_factor' : "22",
        'fps' : "29.97",
    },
    "2" : {
        'scale': "960:540",
        'audio_depth' : "64k",
        'rate_factor' : "24",
        'fps' : "29.97",
    },
    "3" : {
        'scale' : "640:360",
        'audio_depth' : "64k",
        'rate_factor' : "26",
        'fps' : "29.97",
    },
    "4" : {
        'scale' : "640:360",
        'audio_depth' : "64k",
        'rate_factor' : "32",
        'fps' : "29.97",
    },
}

ffcommands = [
    "-b:a 64k -ar 44100 -c:v libx264 -vf scale=1920:1080 -crf 18 -r 24 -g 72 -f hls -hls_time 9 -hls_list_size 0 -s 1920x1080 /Users/tiagorodriguez/Desktop/HLS_testbed/0/XXXXXXXX2015-V000700_0.m3u8",
    "-b:a 64k -ar 44100 -c:v libx264 -vf scale=1280:720 -crf 22 -r 24 -g 72 -f hls -hls_time 9 -hls_list_size 0 -s 1280x720 /Users/tiagorodriguez/Desktop/HLS_testbed/1/XXXXXXXX2015-V000700_1.m3u8",
    "-b:a 64k -ar 44100 -c:v libx264 -vf scale=960:540 -crf 24 -r 24 -g 72 -f hls -hls_time 9 -hls_list_size 0 -s 960x540 /Users/tiagorodriguez/Desktop/HLS_testbed/2/XXXXXXXX2015-V000700_2.m3u8",
    "-b:a 64k -ar 44100 -c:v libx264 -vf scale=640:360 -crf 26 -r 24 -g 72 -f hls -hls_time 9 -hls_list_size 0 -s 640x360 /Users/tiagorodriguez/Desktop/HLS_testbed/3/XXXXXXXX2015-V000700_3.m3u8",
    "-b:a 32k -ar 44100 -c:v libx264 -vf scale=640:360 -crf 32 -r 24 -g 72 -f hls -hls_time 9 -hls_list_size 0 -s 640x360 /Users/tiagorodriguez/Desktop/HLS_testbed/4/XXXXXXXX2015-V000700_4.m3u8",
    ]


class HLS_Encode():

    def __init__(self, mezz_file):
        self.mezz_file = mezz_file
        self.ffcommand = ['ffmpeg -y -i']


    def GENERATE(self):
        for t in TRANSCODE_PROFILES:
            self.ffcommand.append(self.mezz_file)
            print self.ffcommand

            break



def main():

    HE = HLS_Encode(mezz_file = '/Users/tiagorodriguez/Desktop/HLS_testbed/TEST_VIDEO/XXXXXXXXT114-V015600.mp4')
    HE.GENERATE()
    # hsl_transcode()



# if not os.path.exists(os.path.join(output_id):
#     os.mkdir(output_id)


# for f in ffcommands:
#     output_id = f.split()[-1]..split('/')[-1]
#     output_dir = f.split()[-1].replace(output_id, '')

#     if not os.path.exists(output_dir):
#         os.mkdir(output_dir)

#     os.system(ffbegin + f)


# ###Build Manifest
# for file in os.listdir(os.path.join(os.path.dirname(__file__), )


if __name__ == '__main__':
    sys.exit(main())











