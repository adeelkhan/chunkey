VEDA\_HLS
=========

HTTP Live Stream Encode for AWS EC2, VEDA, and edX
--------------------------------------------------

This is a quick HLS library/crawler for conversion from static file
hosting to an HLS solution for quick and high-quality/low-latency
streaming that is adaptible for differing global connection speeds.

Install
-------

::

    `pip install veda_hls`

| **NOTE:** This requires a compiled version of ffmpeg (with libx264)
  available here:
| https://trac.ffmpeg.org/wiki/CompilationGuide

Setup
-----

In the aws\_keys.json file, add AWS secret key, access key ID, and
target bucket. The “Deliver Root” is optional, and can point to a root
subdirectory in the bucket, if desired.

Use (one-off):
--------------

::

    from veda_hls import VEDA_HLS

    VEDA_HLS(
        mezz_file='link_to/file/to_be/transcoded.mp4'
        manifest='optional_manifest_name'
        )

Use (crawler)
-------------

::

    from veda_hls import VEDA_HLS

    VEDA_HLS(
        crawler=True
        crawl_bucket='aws_s3_bucketname'
        crawl_root='optional/bucketdir'
        )

| **TODO**:
| [ ] CRAWL

[ ] JSON setup scripting

[ ] Video ID Generation

[ ] API Data pushing

::

    [ ] VAL  

    [ ] VEDA  