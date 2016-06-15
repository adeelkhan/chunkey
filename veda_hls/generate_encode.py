#! usr/bin/env python

import os
import sys
import subprocess
import fnmatch
import boto
import boto.s3
from boto.s3.key import Key

"""
Encode streams of input -> output for HLS five stream video

NOTE: Just a test, so will need greater looking into

Generate master manifest, upload (easy, via boto) to output bucket

"""


'''
ffmpeg command :

"-b:a 64k -ar 44100 -c:v libx264 -vf scale=1920:1080 -crf 18 -r 24 -g 72 
-f hls -hls_time 9 -hls_list_size 0 -s 1920x1080 
/Users/tiagorodriguez/Desktop/HLS_testbed/0/XXXXXXXX2015-V000700_0.m3u8",

'''

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from settings import Settings

# from abstractions import VideoFile, TransportStream
import util_functions



class HLS_Command():

    def __init__(self, mezz_file, **kwargs):
        """
        TESTING ONLY
        """
        self.settings = Settings(
            deliver_bucket = 'veda-testoutput',
            deliver_directory = 'HLS_TEST'
            )

        self.mezz_file = mezz_file

        self.encode_list = []
        self.video_id = kwargs.get(
            'video_id', mezz_file.split('/')[-1].split('.')[0]
            )
        self.video_root = os.path.join(self.settings.WORKDIR, self.video_id)

        self.manifest = kwargs.get('manifest', self.video_id + '.m3u8')
        self.manifest_data = []

        self.completed_encodes = []


    def run(self):
        """
        Groom environ, make dirs
        """
        if not os.path.exists(self.settings.WORKDIR):
            os.mkdir(self.settings.WORKDIR)

        if not os.path.exists(self.video_root):
            os.mkdir(self.video_root)

        self._GENERATE_ENCODE()
        self._EXECUTE_ENCODE()
        self._MANIFEST_DATA()
        self._MANIFEST_GENERATE()
        self._UPLOAD_TRANSPORT()


    def _GENERATE_ENCODE(self):
        """
        Generate ffmpeg commands into array by use in transcode function

        """
        '''
        # ffmpeg -y -i 
        /Users/tiagorodriguez/Desktop/HLS_testbed/TEST_VIDEO/HARSPU27T313-V043500_DTH.mp4 
        -c:a aac -strict experimental -ac 2 -b:a 96k -ar 44100 
        -c:v libx264 -pix_fmt yuv420p -profile:v main -level 3.2 -maxrate 2M -bufsize 6M 
        -crf 18 -r 24 -g 72 -f hls -hls_time 9 -hls_list_size 0 -s 1280x720 
        /Users/tiagorodriguez/Desktop/HLS_testbed/OUTPUT_TEST/1280x720.m3u8
        
        '''
        for profile_name, profile in self.settings.TRANSCODE_PROFILES.iteritems():
            ffcommand = ['ffmpeg -y -i']
            ffcommand.append(self.mezz_file)

            """
            Add Audio
            """
            ffcommand.append("-c:a aac -strict experimental -ac 2")
            ffcommand.append("-b:a")
            ffcommand.append(profile['audio_depth'])
            ffcommand.append("-ar")
            ffcommand.append("44100")

            """
            Add codec
            """
            ffcommand.append("-pix_fmt yuv420p -profile:v main -level 3.2 -maxrate 2M -bufsize 6M")
            ffcommand.append("-c:v")
            ffcommand.append("libx264")
            
            """
            Add scaling / rate factor / framerate
            """
            ffcommand.append("-vf")
            ffcommand.append("scale=" + profile['scale'])
            ffcommand.append("-crf")
            ffcommand.append(profile['rate_factor'])
            ffcommand.append("-r")
            ffcommand.append(profile['fps'])
            ffcommand.append("-g")
            ffcommand.append("72")
            ffcommand.append("-f")
            """
            Add HLS Commands
            """
            ffcommand.append("hls")
            ffcommand.append("-hls_time")
            ffcommand.append(str(self.settings.HLS_TIME))
            ffcommand.append("-hls_list_size")
            ffcommand.append("0")
            ffcommand.append("-s")
            ffcommand.append(profile['scale'].replace(':', 'x'))

            """
            Add output files
            """
            # if not os.path.exists(os.path.join(self.video_root, profile_name)):
            #     os.mkdir(os.path.join(self.video_root, profile_name))
            destination = os.path.join(self.video_root, self.video_id)
            destination += '_' + profile_name + '_'
            destination += ".m3u8"

            ffcommand.append(destination)
            if len(ffcommand) > 0:

                self.encode_list.append(' '.join((ffcommand)))

        return None


    def _EXECUTE_ENCODE(self):
        for command in self.encode_list:

            files_array = [f for f in command.split(' ') if '/' in f]
            source_file = files_array[0]
            output_file = files_array[1]

            process = subprocess.Popen(
                command, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.STDOUT, 
                shell=True, 
                universal_newlines=True
                )
            """ 
            get vid info, gen status
            """
            util_functions.status_bar(process=process)

            if os.path.exists(output_file):
                """
                We'll let this fail quietly
                """
                self.completed_encodes.append(output_file) 
            print ''
        return None


    def _DETERMINE_BANDWIDTH(self, profile_name):

        max_bandwidth = 0.0

        """this is crappy"""
        for file in os.listdir(self.video_root):
            if fnmatch.fnmatch(file, '*.ts') \
            and fnmatch.fnmatch(file, '_'.join((self.video_id, profile_name, '*'))):

                bandwidth = float(os.stat(os.path.join(self.video_root, file)).st_size) / 9
                if bandwidth > max_bandwidth:
                    max_bandwidth = bandwidth

        ## THIS CALCULATES FROM BITRATE AS PRESENTED IN FFPROBE
        #         VideoFileObject = VideoFile(
        #             filepath = os.path.join(transport_dir, file)
        #             )
        #         util_functions.probe_video(VideoFileObject=VideoFileObject)
        #         if VideoFileObject.bitrate > max_bitrate:
        #             max_bitrate = VideoFileObject.bitrate
        return max_bandwidth



    def _MANIFEST_DATA(self):

        class TransportStream():
            self.bandwidth = None
            self.resolution = None
            self.ts_manifest = None

        '''
        MANIFEST : 
        NOTE -- this doesn't seem to work with directories in S3

        #EXTM3U
        #EXT-X-STREAM-INF:BANDWIDTH=192000,RESOLUTION=320x180
        OUTPUT_TEST/XXXXXXXX2015-V000700_.m3u8
        #EXT-X-STREAM-INF:BANDWIDTH=500000,RESOLUTION=480x270
        OUTPUT_TEST/XXXXXXXX2015-V000700_.m3u8
        #EXT-X-STREAM-INF:BANDWIDTH=1000000,RESOLUTION=640x360
        OUTPUT_TEST/XXXXXXXX2015-V000700_.m3u8
        #EXT-X-STREAM-INF:BANDWIDTH=2000000,RESOLUTION=1280x720
        OUTPUT_TEST/XXXXXXXX2015-V000700_.m3u8

        '''
        for profile_name, profile in self.settings.TRANSCODE_PROFILES.iteritems():
            T1 = TransportStream()
            """
            TS manifest
            """
            T1.ts_manifest = self.video_id
            T1.ts_manifest += '_' + profile_name + '_'
            T1.ts_manifest += ".m3u8"
            """
            Bandwidth
            """
            T1.bandwidth = int(self._DETERMINE_BANDWIDTH(profile_name=profile_name))
            """
            resolution
            """
            T1.resolution = self.settings.TRANSCODE_PROFILES[profile_name]['scale'].replace(':', 'x')
            self.manifest_data.append(T1)

        return None



    def _MANIFEST_GENERATE(self):
        print self.manifest
        print self.video_root
        print os.path.join(self.video_root, self.manifest)
        with open(os.path.join(self.video_root, self.manifest), 'w') as m1:
            m1.write('#EXTM3U')
        # print self.manifest_data
            m1.write('\n')
            for m in self.manifest_data:
                m1.write('#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=')
                m1.write(str(m.bandwidth))
                m1.write(',')
                m1.write('RESOLUTION=')
                m1.write(m.resolution)
                m1.write('\n')
                m1.write(m.ts_manifest)
                m1.write('\n')

        return None



    def _UPLOAD_TRANSPORT(self):
        """
        **NOTE**
        We won't bother with multipart upload operations here, 
        as this should NEVER be that big. We're uploading ${settings.HLS_TIME} (default=9) 
        seconds of a squashed file, so if you're above 5gB, you're from the future, 
        and you should be doing something else or outside playing with your jetpack 
        above the sunken city of Miami


        Upload single part
        """
        conn = boto.connect_s3(
            self.settings.ACCESS_KEY_ID,
            self.settings.SECRET_ACCESS_KEY
            )
        delv_bucket = conn.get_bucket(self.settings.deliver_bucket)

        """
        TODO: Set this to be the video ID on key upload
        """
        for ts1 in os.listdir(self.video_root):
            print ts1
            upload_key = Key(delv_bucket)
            upload_key.key = '/'.join((self.settings.deliver_directory, ts1))
            """
            Actually upload the thing
            """
            upload_key.set_contents_from_filename(
                os.path.join(self.video_root, ts1)
                )
            upload_key.set_acl('public-read')

        return True



    def _PASS_DATA(self):
        pass



    def _CLEAN_WORKDIR(self):
        pass





def main():

    HE = HLS_Command(
        mezz_file = "/Users/tiagorodriguez/Desktop/HLS_testbed/TEST_VIDEO/XXXXXXXXT114-V015600.mp4",
        manifest = "XXXXXXXX2015-V000700_0.m3u8",
        )
    HE.run()



    ##         https://s3.amazonaws.com/veda-testoutput/HLS_TEST/XXXXXXXX2015-V000700_.m3u8



if __name__ == '__main__':
    sys.exit(main())











