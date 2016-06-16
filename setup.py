from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='veda_hls',
    version='0.1',
    description='HLS Transport Stream Pipeline',
    url='http://github.com/yro/veda_hls',
    author='@yro',
    author_email='greg@willowgrain.io',
    license='',
    packages=['veda_hls'],
    include_package_data=True
    install_requires=[
        'boto',
        'requests',
        ]
    test_suite='nose.collector',
    tests_require=['nose'],
    zip_safe=False
    )
