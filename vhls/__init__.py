
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


class VHLS():

    def __init__(self, **kwargs):
        self.mezz_file = kwargs.get('mezz_file', None)
        self.manifest = kwargs.get('manifest', None)
        self.manifest_url = None

        """
        Key kwargs
        """
        self.settings = Settings()
        for key, value in kwargs.items():
            setattr(self.settings, key, value)

        self.Pipeline = None
        self.complete = self._RUN()

    def _RUN(self):
        """
        Regular run
        """
        self.Pipeline = HLS_Pipeline(
            settings=self.settings,
            mezz_file=self.mezz_file
            )

        if self.manifest is not None:
            if '.m3u8' not in self.manifest:
                self.manifest += '.m3u8'

            self.Pipeline.manifest = self.manifest

        self.complete = self.Pipeline.run()
        self.manifest_url = self.Pipeline.manifest_url
        return None


def main():
    pass

if __name__ == '__main__':
    sys.exit(main())
