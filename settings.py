
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
            os.path.join(os.getcwd(), 'WORKDIR')
            )

        """
        Encode Profiles

        """
        self.encode_profiles = kwargs.get(
            'encode_profiles',
            os.path.join(os.path.dirname(__file__), 'encode_profiles.json')
            )
        with open(self.encode_profiles) as encode_data_file:
            encode_data = json.load(encode_data_file)

        self.TRANSCODE_PROFILES = encode_data['ENCODE_PROFILES']
        self.HLS_TIME = encode_data['HLS_TIME']
        self.TARGET_ASPECT_RATIO = float(16) / float(9)

        """
        Key information

        """
        self.access_keys = kwargs.get(
            'aws_keyfile',
            os.path.join(os.path.dirname(__file__), 'access_keys.json')
            )

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
