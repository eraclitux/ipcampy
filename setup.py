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
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Multimedia :: Video :: Capture',
    ],
    keywords='ipcam foscam raspberrypi surveillance ',
    license='LICENSE.txt',
    description='Easily control ip cameras. Comes with built in utilities to make a simple surveillance system.',
    long_description=open('README.rst').read(),
    install_requires=[
        "requests == 1.2.3",
    ],
)
