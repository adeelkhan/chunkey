import os
import sys
import boto
import boto.s3
from boto.s3.key import Key

"""

Crawl s3 bucket/dir

"""
# boto.config.add_section('Boto') 
boto.config.set('Boto','http_socket_timeout','10') 

from encode_pipeline import HLS_Pipeline

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from settings import Settings


class Crawler():
    """
    Iterate through s3 bucket, dl source, and retranscode to HLS stream
    via HLS_Pipeline() 

    ** Note ** 
    is meant to get all files from bucket, with a reasonable 
    number of retries, not to retrieve specific files

    """

    def __init__(self, bucket, directory=None, **kwargs):

        self.settings = kwargs.get('settings', Settings())

        self.bucket = bucket
        self.directory = directory
        if self.directory != None and self.directory[-1] != '/':
            self.directory += '/'

        self.string_matching = kwargs.get('string_match', ['_DTH', '_100'])

        self.complete = False
        ##
        self.run = True
        while self.run is True:
            self.run = self._CONNECT()
            self.run = self._LIST()
            self.run = self._RUN_HLSSTREAM()

            self.run = False


    def _CONNECT(self):
        try:
            connect = boto.connect_s3(
                self.settings.ACCESS_KEY_ID,
                self.settings.SECRET_ACCESS_KEY
                )
            self.boto_bucket = connect.get_bucket(self.bucket)
            return True
        except:
            return False


    def _LIST(self):
        """
        Since this is a VEDA-Based process, 
        the keyname is related to the VEDA ID

        """
        if not os.path.exists(self.settings.CRAWLDIR):
            os.mkdir(self.settings.CRAWLDIR)

        for key in self.boto_bucket.list(self.directory, '/'):
            if self.string_matching != None and len(self.string_matching) > 0:
                if any(s in key.name for s in self.string_matching):
                    dl_key = self.boto_bucket.get_key(key.name)
                    dl_key.get_contents_to_filename(
                        os.path.join(self.settings.CRAWLDIR, key.name)
                        )
            else:
                dl_key = self.boto_bucket.get_key(key.name)
                dl_key.get_contents_to_filename(
                    os.path.join(self.settings.CRAWLDIR, key.name)
                    )
        return True


    def _RUN_HLSSTREAM(self):
        for file in os.listdir(self.settings.CRAWLDIR):
            print file
            video_id = file.split('_')[0]
            HP = HLS_Pipeline(
                settings = self.settings,
                mezz_file = os.path.join(self.settings.CRAWLDIR, file),
                video_id = video_id
                )
            HP.run()
        return True


    def _PASS_DATA(self):
        ## Send Data to VEDA / VAL
        pass

    def _LOG_DATA(self):
        pass

    def _CLEAN_ENVIRONMENT(self):
        pass



def main():
    # c1 = Crawler()
    # bucket='veda-testinput',
    # )
    pass

if __name__ == '__main__':
    sys.exit(main())

