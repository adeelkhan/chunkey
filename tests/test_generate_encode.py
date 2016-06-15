import os
import sys
import unittest

"""
tests for VEDA_HLS

"""
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'veda_hls'))
from generate_encode import HLS_Command


class TestGenEncode(unittest.TestCase):
    def test_is_string(self):
        HE = HLS_Command(mezz_file = '/Users/tiagorodriguez/Desktop/HLS_testbed/TEST_VIDEO/XXXXXXXXT114-V015600.mp4')
        HE.run()
        self.assertEqual(len(HE.settings.TRANSCODE_PROFILES), len(HE.encode_list))



def main():
    unittest.main()


if __name__ == '__main__':
    sys.exit(main())