#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Andrea Masi 2014 eraclitux@gmail.com

import unittest
import mock
import requests
from ipcampy.common import CamException
from ipcampy.foscam import FosCam, map_position 

class TestFosCam(unittest.TestCase):

    def test_map_position_1(self):
        self.assertEqual(map_position(1), 31)

    def test_map_position_16(self):
        self.assertEqual(map_position(16), 61)

    @mock.patch('ipcampy.foscam.requests')
    def test_move_no_password(self, mock_requests):
        r = requests.Response()
        r.status_code = 401
        mock_requests.get.return_value = r
        f = FosCam("localhost")
        with self.assertRaisesRegexp(CamException, "Unauthorized"):
            f.move(1) 

    @mock.patch('ipcampy.foscam.requests')
    def test_move_wrong_pos(self, mock_requests):
        r = requests.Response()
        r.status_code = 401
        mock_requests.get.return_value = r
        f = FosCam("localhost")
        with self.assertRaisesRegexp(CamException, "Position"):
            f.move(18) 

if __name__ == '__main__':
    unittest.main()
