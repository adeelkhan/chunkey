import os
import sys
import subprocess
import datetime

"""
"Dumb" utility executables

"""
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from settings import Settings
settings = Settings()


def log_results(message, result):
    with open(settings.LOG_FILE, 'a') as l1:
        l1.write('%s %s %s %s' % ('[', str(datetime.datetime.now()), ']', ' '))
        l1.write('%s : %r' % (message, result))
        l1.write('\n')
    return None


def seconds_from_string(duration):
    """
    Return a float (seconds) from something like 00:15:32.33

    """
    hours = float(duration.split(':')[0])
    minutes = float(duration.split(':')[1])
    seconds = float(duration.split(':')[2])
    duration_seconds = (((hours * 60) + minutes) * 60) + seconds
    return duration_seconds


def status_bar(process):
    """
    This is a little gross, but it'll get us a status bar

    """
    fps = None
    duration = None
    while True:
        line = process.stdout.readline().strip()

        if line == '' and process.poll() is not None:
            break
        if fps == None or duration == None:
            if "Stream #" in line and " Video: " in line:
                fps = [s for s in line.split(',') if "fps" in s][0].strip(' fps')

            if "Duration: " in line:
                dur = line.split('Duration: ')[1].split(',')[0].strip()
                duration = seconds_from_string(duration=dur)

        else:
            if 'frame=' in line:
                cur_frame = line.split('frame=')[1].split('fps=')[0].strip()
                end_frame = float(duration) * float(fps.strip())
                pctg = (float(cur_frame) / float(end_frame))

                sys.stdout.write('\r')
                i = int(pctg * 20.0)
                sys.stdout.write("%s : [%-20s] %d%%" % ('Transcode', '='*i, int(pctg * 100)))
                sys.stdout.flush()
    """
    Just for politeness
    """
    sys.stdout.write('\r')
    sys.stdout.write("%s : [%-20s] %d%%" % ('Transcode', '='*20, 100))
    sys.stdout.flush()
    print ''


def probe_video(VideoFileObject):
    """
    Use ffprobe to determine facts about the video
    """
    ffprobe_comm = 'ffprobe -hide_banner ' + VideoFileObject.filepath

    p = subprocess.Popen(
        ffprobe_comm, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.STDOUT, 
        shell=True
        )

    for line in iter(p.stdout.readline, b''):
        if "Duration: " in line:
            ## Duration
            vid_duration = line.split('Duration: ')[1].split(',')[0].strip()
            VideoFileObject.duration = seconds_from_string(duration=vid_duration)
            ## Bitrate
            try:
                VideoFileObject.bitrate = float(line.split('bitrate: ')[1].strip().split()[0])
            except:
                pass
        elif "Stream #" in line and 'Video: ' in line:
            codec_array = line.strip().split(',') 
            for c in codec_array:
                ## Resolution
                if len(c.split('x')) == 2:
                    if '[' not in c:
                        VideoFileObject.resolution = c.strip()
                    else:
                        VideoFileObject.resolution = c.strip().split(' ')[0]
    return VideoFileObject


def generate_veda_token(settings):
    """
    Gen and authorize a VEDA API token
    """
    # if Settings.NODE_VEDA_ATTACH is True:
        ## Generate Token
    payload = { 'grant_type' : 'client_credentials' }
    r = requests.post(
        Settings.VEDA_TOKEN_URL, 
        params=payload, 
        auth=(
            Settings.VEDA_API_CLIENTID, 
            Settings.VEDA_API_CLIENTSECRET
            ), 
        timeout=20
        )
        if r.status_code == 200:
            veda_token = ast.literal_eval(r.text)['access_token']
        else:
            ErrorObject(
                message = 'ERROR : VEDA Token Generate',
                method = 'veda_tokengen',
            )
            return None

        ## Authorize token
        """
        This is based around the VEDA "No Auth Server" hack
        """
        payload = { 'data' : veda_token }
        t = requests.post(Settings.VEDA_AUTH_URL, data=payload)
        if t.status_code == 200 and t.text == 'True':
            return veda_token
        else:
            ErrorObject(
                message = 'ERROR : VEDA Token Auth',
                method = 'veda_tokengen',
            )
            return None

    else:
        ErrorObject(
            message = 'ERROR : CONFIG - veda_attach is False',
            method = 'veda_tokengen',
        )
        return None
















if __name__ == '__main__':
    log_results('Test', True)



















