import os
import sys
import json

"""
globals

"""


class Settings():

    def __init__(self, **kwargs):

        ## encode directory
        self.WORKDIR = kwargs.get(
            'work_dir', 
            os.path.join(os.path.dirname(__file__), 'WORKDIR')
            )

        self.LOG_FILE = os.path.join(os.path.dirname(__file__), 'log.out')

        ## encode switching target length
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

        """
        Key information

        """
        self.access_keys = kwargs.get('aws_keyfile', os.path.join(os.path.dirname(__file__), 'access_keys.json'))

        with open(self.access_keys) as data_file:
            data = json.load(data_file)
        """
        AWS s3 information
        """
        self.ACCESS_KEY_ID = kwargs.get(
            'ACCESS_KEY_ID', 
            data["AWS_KEYS"]["ACCESS_KEY_ID"]
            )
        self.SECRET_ACCESS_KEY = kwargs.get(
            'SECRET_ACCESS_KEY', 
            data["AWS_KEYS"]["SECRET_ACCESS_KEY"]
            )
        self.DELIVER_BUCKET = kwargs.get(
            'DELIVER_BUCKET', 
            data["AWS_DEFAULTS"]["DELIVER_BUCKET"]
            )
        self.DELIVER_ROOT = kwargs.get(
            'DELIVER_ROOT', 
            data["AWS_DEFAULTS"]["DELIVER_ROOT"]
            )

        """
        VAL information
        """

        """
        VEDA information
        """

