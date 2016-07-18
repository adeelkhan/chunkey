
import os
import sys
import unittest
import subprocess
import boto

"""
tests for VEDA_HLS

"""
sys.path.append(
    os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        'vhls')
    )
from encode_pipeline import HLS_Pipeline
import util_functions


@unittest.skip("FFmpeg test")
class TestEncodePipeline(unittest.TestCase):

    def test_command_gen(self):
        """
        Generate an ffmpeg command

        """
        self.Pipeline = HLS_Pipeline(
            mezz_file=os.path.join(
                os.path.dirname(__file__),
                'OVTESTFILE_01.mp4'
                )
            )

        self.Pipeline._GENERATE_ENCODE()

        self.assertEqual(
            len(self.Pipeline.settings.TRANSCODE_PROFILES),
            len(self.Pipeline.encode_list)
            )
        return self


@unittest.skip("FFmpeg compiled")
class TestFFMPEGCompile(unittest.TestCase):
    def test_ffmpeg_compile(self):
        """
        test if ffmpeg has compiled properly

        """
        process = subprocess.Popen(
            'ffprobe',
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            shell=True,
            universal_newlines=True
            )

        probe_commands = []
        for line in iter(process.stdout.readline, b''):
            probe_commands.append(line.strip())

        self.assertTrue(
            "usage: ffprobe [OPTIONS] [INPUT_FILE]" in
            [l for l in probe_commands]
            )


@unittest.skip("AWS Credentials")
class TestAWSCredentials(unittest.TestCase):
    """
    Check settings, connect to AWS

    """
    def setUp():
        self.settings = VHLS_Globals()

    def test_upload_credentials(self):
        if self.settings.ACCESS_KEY_ID is not None:
            self.assertTrue(
                len(self.settings.ACCESS_KEY_ID) > 0
                )
            self.assertTrue(
                len(self.settings.SECRET_ACCESS_KEY) > 0
                )
        else:
            self.assertTrue(self.settings.SECRET_ACCESS_KEY is None)

    def s3_connection(self):
        if self.settings.ACCESS_KEY_ID is not None:
            try:
                conn = boto.connect_s3(
                    self.settings.ACCESS_KEY_ID,
                    self.settings.SECRET_ACCESS_KEY
                    )
                delv_bucket = conn.get_bucket(self.settings.DELIVER_BUCKET)
                return True
            except:
                return False
        else:
            return True

    def test_upload_connection(self):
        self.assertTrue(self.s3_connection())


def main():
    unittest.main()


if __name__ == '__main__':
    sys.exit(main())
