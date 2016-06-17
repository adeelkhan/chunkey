import os
import sys

"""

Crawl s3 bucket/dir

"""
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from settings import Settings

settings = Settings()


class CrawlBucket():
    
    def __init__(self, bucket, directory=None):

        self.bucket = bucket
        self.directory = directory
        ##
        self._CONNECT()


    def _CONNECT(self):
        pass

    def _LISTDIR(self):
        pass

    def _DOWNLOAD(self):
        pass

    def _RUN_HLSSTREAM(self):
        ## get encode_pipeline, run on file
        pass

    def _PASS_DATA(self):
        ## Send Data to VEDA / VAL
        pass

    def _LOG_DATA(self):
        pass



def main():
    pass

if __name__ == '__main__':
    sys.exit(main())

