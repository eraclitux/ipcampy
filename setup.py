#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='IpCamPy',
    version='0.2.0',
    author='Andrea Masi',
    author_email='eraclitux@gmail.com',
    packages=['ipcampy', 'ipcampy.test', 'ipcamweb'],
    scripts=['bin/campatrol'],
    url='https://github.com/eraclitux/ipcampy',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Multimedia :: Video :: Capture',
    ],
    tests_require = [
        'mock'
    ],
    keywords='ipcam foscam raspberrypi surveillance',
    license='LICENSE.txt',
    description='Easily control ip cameras. Comes with built in utilities to make a simple surveillance system.',
    long_description=open('README.rst').read(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "requests==1.2.3",
        "Flask==0.10.1",
    ],
)
