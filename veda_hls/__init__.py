import os
import sys
import argparse

"""
Primary Function

"""
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from settings import Settings

from encode_pipeline import HLS_Pipeline
import util_functions


class VEDA_HLS():

    def __init__(self, **kwargs):

        self.mezz_file = kwargs.get('mezz_file', None)
        self.manifest = kwargs.get('manifest', None)
        self.log_results = kwargs.get('log_results', None)

        """
        Crawler commands
        """
        self.crawl = kwargs.get('crawl', False)
        self.crawl_bucket = kwargs.get('crawl_bucket', None)
        self.crawl_root = kwargs.get('crawl_root', None)

        """
        Key kwargs
        """
        self.settings = Settings()
        for key, value in kwargs.items():
            setattr(self.settings, key, value)

        self.Pipeline = None
        self.complete = self._RUN()
        if self.complete is True:
            return self.Pipeline.manifest_url
        else:
            return None


    def _RUN(self):
        """
        Regular run
        """
        self.Pipeline = HLS_Pipeline(
            settings=self.settings,
            mezz_file=self.mezz_file
            )

        if self.manifest != None:
            if '.m3u8' not in self.manifest:
                self.manifest += '.m3u8'

            self.Pipeline.manifest = self.manifest

        complete = self.Pipeline.run()
        return complete



def main():
    ## NOTE: May enable this in future ##
    # """
    # Can be run as either standalone or as a script

    # """
    # parser = argparse.ArgumentParser()

    # parser.usage = '''
    # {cmd} -v [--mezz_file] mezzanine video (file to be encoded)

    # {cmd} -m [--manifest] m3u8 target manifest name

    # {cmd} -log [--log_results] Drop results in logfile 
    #     instead of sys.stdout

    # '''.format(cmd=sys.argv[0])

    # parser.add_argument(
    #     '-v', '--mezz_file', help='Mezzanine Video', default=''
    #     )
    # parser.add_argument(
    #     '-m', '--manifest', help='Target Manifest Name', default=None
    #     )
    # parser.add_argument(
    #     '-log', '--log_results', help='Log Results in Datafile', default=False)

    # args = parser.parse_args()

    # if len(args.mezz_file) == 0:
    #     print 'ERROR : No video file specified'
    #     return 1

    # V1 = VEDA_HLS(
    #     mezz_file=args.mezz_file,
    #     manifest=args.manifest,
    #     log_results=args.log_results
    #     )
    pass

if __name__ == '__main__':
    sys.exit(main())

