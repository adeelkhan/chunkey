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

        self._RUN()


    def _RUN(self):

        EP = HLS_Pipeline(
            mezz_file=self.mezz_file
            )
        if self.manifest != None:
            if '.m3u8' not in self.manifest:
                self.manifest += '.m3u8'

            EP.manifest = self.manifest

        EP.run()



def main():
    """
    Can be run as either standalone or as a script

    """
    parser = argparse.ArgumentParser()

    parser.usage = '''
    {cmd} -v [--mezz_file] mezzanine video (file to be encoded)
    {cmd} -m [--manifest] m3u8 target manifest name
    '''.format(cmd=sys.argv[0])

    parser.add_argument(
        '-v', '--mezz_file', help='Mezzanine Video', default=''
        )
    parser.add_argument(
        '-m', '--manifest', help='Target Manifest Name', default=None
        )
    args = parser.parse_args()

    if len(args.mezz_file) == 0:
        print 'ERROR : No video file specified'
        return 1

    V1 = VEDA_HLS(
        mezz_file=args.mezz_file,
        manifest=args.manifest
        )


if __name__ == '__main__':
    sys.exit(main())

