=======
IpCamPy
=======

|image0|_

.. |image0| image:: https://drone.io/github.com/eraclitux/ipcampy/status.png
.. _image0: https://drone.io/github.com/eraclitux/ipcampy/latest

.. contents::

This package let you control supported ip cameras from your python app with ease.

Batteries are included so you can make a DIY surveillance system in a snap, see `A Raspberry Pi surveillance system`_

Package is written with easy extendibility in mind, pull requests that add new cams or fix issues are welcome, encouraged, and credited.

Examples
========

A Raspberry Pi surveillance system
----------------------------------

Login to your Pi and get the code from the cheese shop::

    $ pip install ipcampy

Define a configuraton file of your cams in json. For example, save these lines in `cam.conf`::

    {"address":"192.168.1.20", "user":"admin", "pswd":"xxyyzz", "port":"8010", "type":"foscam" "name":"Garden"}
    {"address":"192.168.1.21", "user":"admin", "pswd":"xxyyzz", "port":"8010", "type":"foscam", "name":"Gate"}

Start to get a snapshot from all defined camera every 10 seconds running::

    $ campatrol -d ~/cam.conf -p xxx

This even start a webpanel that can be accessed from any browser using this address with username ``watcher`` and password ``xxx``::

    http://<my_server_ip>:6001

Use chrome or firefox on smartphones and tablets to watch live streams.

Snapshots are stored in ``/tmp`` for default but a different path can be specified with ``-s`` option.

Screenshots
===========

|image1|_
|image2|_
|image3|_

.. |image1| image:: http://www.eraclitux.com/public/ipcampy-1.png
.. _image1: http://www.eraclitux.com/public/ipcampy-1.png

.. |image2| image:: http://www.eraclitux.com/public/ipcampy-2.png
.. _image2: http://www.eraclitux.com/public/ipcampy-2.png

.. |image3| image:: http://www.eraclitux.com/public/ipcampy-3.png
.. _image3: http://www.eraclitux.com/public/ipcampy-3.png

Supported cameras
=================

Defines wich type to use in json configuration "type" key.

Foscam
------

- **FI8908W** and clones, set ``"type": "foscam"``. May works on similar cams from same family too. 

Please report camera working status opening an issue_.

.. _issue: https://github.com/eraclitux/ipcampy/issues

Notes
=====

This package is in early development. Things **could** work or maybe not. APIs can quickly change.

To get the latest code clone the github's repository instead of using ``pip``::

    $ git clone https://github.com/eraclitux/ipcampy.git

Credits
=======

Favicon: http://www.iconarchive.com/artist/yusuke-kamiyamane.html

Disclaimer
==========

All trademarks, copyrights and other forms of intellectual property belong to their respective owners.

The author is not affiliated with any cam vendor cited above.
