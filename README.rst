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

    `pip install vhls`

| **NOTE:** This requires a compiled version of ffmpeg (with libx264)
  available here:
| https://trac.ffmpeg.org/wiki/CompilationGuide

Setup
-----

In the aws\_keys.json file, add AWS secret key, access key ID, and
target bucket. The “Deliver Root” is optional, and can point to a root
subdirectory in the bucket, if desired.

Use:
--------------

::

    from vhls import VHLS

    VHLS(
        mezz_file='link_to/file/to_be/transcoded.mp4'
        manifest='manifest_name' ## optional
        )




**TODO**:

[ ] Logging
[ ] passing AWS creds to tests
[ ] ffmpeg testing for included test file

