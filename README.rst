=======
IpCamPy
=======

.. contents::

This package let you control supported ip cameras from your python app with ease.

Batteries are included so you can make a DIY surveillance system in a snap, see `Using built in utils`_

Package is written with easy extendibility in mind, pull requests that add new cams or fix issues are welcome, encouraged, and credited.

Examples
========

Using built in utils
--------------------
Define a configuraton file of cams in json. For example, save these lines in `cam.conf`::

    {"address":"192.168.1.20", "user":"admin", "pswd":"xxyyzz", "port":"8010", "type":"foscam" "name":"Garden"}
    {"address":"192.168.1.21", "user":"admin", "pswd":"xxyyzz", "port":"8010", "type":"foscam", "name":"Gate"}

To get a snapshot from all defined camera every 10 seconds, run this from command line::

    $ campatrol -d ~/cam.conf -p xxx

This even start a webpanel that can be accessed from any browser using this address with username ``watcher`` and password ``xxx``::

    http://<my_server_ip>:6001

Use chrome or firefox on smartphones and tablets to watch live streams.

Snapshots are stored in ``/tmp`` for default but a different path can be specified with ``-s`` option.

Supported cameras
=================

Defines wich type to use in json configuration "type" key.

Foscam
------
- **FI8908W** and clones, set ``"type": "foscam"``. May works on similar cams from same family too. Please report camera working status opening an issue_.

.. _issue: https://github.com/eraclitux/ipcampy/issues

Notes
=====
This package is in early development. Things **could** work or maybe not. APIs can quickly change.

Credits
=======
Favicon: http://www.iconarchive.com/artist/yusuke-kamiyamane.html
