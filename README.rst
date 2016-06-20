VHLS
=========

HTTP Live Stream Encode for endpoints in AWS EC2
--------------------------------------------------

This is a quick HLS library/crawler for conversion from static file
hosting to an HLS solution for quick and high-quality/low-latency
streaming that is adaptible for differing global connection speeds.

Install
-------

::

    `python setup.py install`

| **NOTE:** This requires a compiled version of ffmpeg (with libx264)
  available here:
| https://trac.ffmpeg.org/wiki/CompilationGuide


Setup
-----

In the 'aws\_keys.json' file, add AWS secret key, access key ID, and
target bucket. 
| The “Deliver Root” is optional, and can point to a root
subdirectory in the bucket, if desired.
| The 'encode\_profiles.json' file can act as a template for a set of 
encoding profiles as desired

Use:
----

::

    from vhls import VHLS


    V1 = VHLS(
        mezz_file='link_to/file/to_be/transcoded.mp4'
        )

will generate an HLS manifest with as many streams as indicated by 
default (5), or the optional 'encode\_profiles.json' file pointed to by 
a keyword arg (see below)


Args (optional):
-----

::
    manifest='manifest_name' ## optional

    access_keys='path/to/access_keys.json'

    encode_profiles='path/to/encode_profiles.json'


Retrieve data:

::
    V1.manifest_url -- endpoint url for manifest (aws s3)


**TODO**:

[ ] Logging

[ ] passing AWS creds to tests

[ ] ffmpeg testing for included test file

