
from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='vhls',
    version='0.1',
    description='HLS Transport Stream Pipeline',
    url='http://github.com/yro/vhls',
    author='@yro',
    author_email='greg@willowgrain.io',
    license='',
    packages=['vhls'],
    include_package_data=True,
    install_requires=[
        'boto',
        'requests',
        ],
    test_suite='nose.collector',
    tests_require=['nose'],
    zip_safe=False
    )
