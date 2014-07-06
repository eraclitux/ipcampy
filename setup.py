#!/usr/bin/env python

try:
        from setuptools import setup
except ImportError:
        from distutils.core import setup

setup(
    name='IpCamPy',
    version='0.1.0',
    author='Andrea Masi',
    author_email='eraclitux@gmail.com',
    packages=['ipcampy', 'ipcampy.test'],
    scripts=['bin/campatrol'],
    url='http://pypi.python.org/pypi/IpCamPy/',
    license='LICENSE.txt',
    description='Easily control ip cameras. Built in surveillance systems utils.',
    long_description=open('README.rst').read(),
    install_requires=[
        "requests == 1.2.3",
    ],
)
