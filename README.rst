=======
IpCamPy
=======

.. contents::

This package let you control supported ip cameras from your python app with ease.

It comes with utils to quickly make your surveillance system.

Package is written with easy extendibility in mind. Pull requests that add new cams or fix issues are welcome, encouraged, and credited.

Examples
========

Using built in utils
--------------------
Define a configuraton file of cams in json.

Example, save these lines in `cam.conf`::

    {"address":"192.168.1.20", "user":"admin", "pswd":"xxyyzz", "port":"8010" , "type":"foscam"}
    {"address":"192.168.1.21", "user":"admin", "pswd":"xxyyzz", "port":"8010" , "type":"foscam"}

To get a snapshot from all defined camera every 10 seconds, run this from command line::

    $ campatrol -d ~/cam.conf

Supported cameras
=================

Foscam
------
- **FI8908W** and clones. May work on similar cams from same family too. 

Notes
=====
This package is in early development. Things **could** work or maybe not. APIs can quickly change.
