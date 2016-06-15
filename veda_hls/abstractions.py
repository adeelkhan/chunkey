import os
import sys

"""
Video object abstraction

"""
# sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# from settings import Settings



class VideoFile():
    """
    A simple object for a video file, could be a mezz,
    a transport stream or an encode

    """
    def __init__(self, filepath=None):
        self.filepath = filepath
        self.duration = None
        self.bitrate = None
        self.resolution = None


class TransportStream()
    """
    A simple object to abstract a transport stream

    """

    def __init__(self):
        self.manifest_bitrate = None
        self.resolution = None
        self.manifest_file = None
        self.encode_profile = None