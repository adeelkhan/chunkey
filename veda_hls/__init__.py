import os
import sys
import argparse

"""
Primary Function

"""

from encode_pipeline import HLS_Pipeline

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

        if self.crawl is False:
            self._RUN()

        elif self.crawl is True:
            self._CRAWL()


    def _RUN(self):
        """
        Regular run
        """
        # if self.crawl is False:
        EP = HLS_Pipeline(
            mezz_file=self.mezz_file
            )

        if self.manifest != None:
            if '.m3u8' not in self.manifest:
                self.manifest += '.m3u8'

            EP.manifest = self.manifest

        complete = EP.run()
        return complete


    def _CRAWL(self):
        """
        Crawl Function
        """

        if self.crawl_bucket == None:
            print "ERROR : No crawl bucket specified"
            return False

        return False





def main():
    """
    Can be run as either standalone or as a script

    """
    parser = argparse.ArgumentParser()

    parser.usage = '''
    {cmd} -v [--mezz_file] mezzanine video (file to be encoded)

    {cmd} -m [--manifest] m3u8 target manifest name

    {cmd} -log [--log_results] Drop results in logfile 
        instead of sys.stdout

    '''.format(cmd=sys.argv[0])

    parser.add_argument(
        '-v', '--mezz_file', help='Mezzanine Video', default=''
        )
    parser.add_argument(
        '-m', '--manifest', help='Target Manifest Name', default=None
        )
    parser.add_argument(
        '-log', '--log_results', help='Log Results in Datafile', default=False)

    args = parser.parse_args()

    if len(args.mezz_file) == 0:
        print 'ERROR : No video file specified'
        return 1

    V1 = VEDA_HLS(
        mezz_file=args.mezz_file,
        manifest=args.manifest
        log_results=args.log_results
        )


if __name__ == '__main__':
    sys.exit(main())

