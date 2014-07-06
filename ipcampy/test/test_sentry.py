#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Andrea Masi 2014 eraclitux@gmail.com

import unittest
import mock
from ipcampy.sentry import __parse_args as parse_args

class TestSentry(unittest.TestCase):

    def test_parse_args_1(self):
        test_data = {"address":"192.168.1.2", "user":"admin", "pswd":"superpswd", "port":"8010" , "type":"foscam"}
        expeted_data = {"address":"192.168.1.2:8010", "user":"admin", "pswd":"superpswd", "name": None}
        self.assertEqual(parse_args(test_data), expeted_data)

    def test_parse_args_2(self):
        test_data = {"address":"192.168.1.2", "port":"8010" , "type":"foscam"}
        expeted_data = {"address":"192.168.1.2:8010", "user":None, "pswd":None, "name": None}
        self.assertEqual(parse_args(test_data), expeted_data)

if __name__ == '__main__':
    unittest.main()
