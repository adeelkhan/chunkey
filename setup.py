
from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='vhls',
    version='1.1.0',
    description='HLS Transport Stream Pipeline',
    url='http://github.com/yro/vhls',
    author='@yro',
    author_email='greg@willowgrain.io',
    license='GNU',
    packages=['vhls'],
    include_package_data=True,
    install_requires=[
        'boto',
        'requests',
        'pyyaml'
        ],
    test_suite='nose.collector',
    tests_require=['nose'],
    data_files=[('', ['encode_profiles.json'])],
    zip_safe=False
    )
