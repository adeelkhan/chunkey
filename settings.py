import os
import sys
import json

"""
globals

"""


class Settings():

    def __init__(self, **kwargs):
        self.WORKDIR = kwargs.get(
            'work_dir', 
            os.path.join(os.path.dirname(__file__), 'WORKDIR')
            )

        self.HLS_TIME = kwargs.get('hls_time', 9)

        ## TODO: redo this
        self.TRANSCODE_PROFILES = {
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
        self.TARGET_ASPECT_RATIO = float(16) / float(9)

        self.aws_keys = kwargs.get('aws_keyfile', os.path.join(os.path.dirname(__file__), 'aws_keys.json'))

        with open(self.aws_keys) as data_file:
            data = json.load(data_file)
            self.ACCESS_KEY_ID = data["AWS_ACCESS_KEY"]["ACCESS_KEY_ID"]
            self.SECRET_ACCESS_KEY = data["AWS_ACCESS_KEY"]["SECRET_ACCESS_KEY"]
            self.DELIVER_BUCKET = data["AWS_DEFAULTS"]["DELIVER_BUCKET"]
            self.DELIVER_ROOT = data["AWS_DEFAULTS"]["DELIVER_ROOT"]