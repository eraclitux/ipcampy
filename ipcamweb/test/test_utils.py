#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Andrea Masi 2014 eraclitux@gmail.com

import os
import unittest
import mock
from mock import inPy3k, MagicMock
from StringIO import StringIO
from ipcamweb.utils import ensure_secret

if inPy3k:
    file_spec = ['_CHUNK_SIZE', '__enter__', '__eq__', '__exit__',
        '__format__', '__ge__', '__gt__', '__hash__', '__iter__', '__le__',
        '__lt__', '__ne__', '__next__', '__repr__', '__str__',
        '_checkClosed', '_checkReadable', '_checkSeekable',
        '_checkWritable', 'buffer', 'close', 'closed', 'detach',
        'encoding', 'errors', 'fileno', 'flush', 'isatty',
        'line_buffering', 'mode', 'name',
        'newlines', 'peek', 'raw', 'read', 'read1', 'readable',
        'readinto', 'readline', 'readlines', 'seek', 'seekable', 'tell',
        'truncate', 'writable', 'write', 'writelines']
else:
    file_spec = file

def mock_open(mock=None, data=None):
    if mock is None:
        mock = MagicMock(spec=file_spec)

    handle = MagicMock(spec=file_spec)
    handle.write.return_value = None
    if data is None:
        handle.__enter__.return_value = handle
    else:
        handle.__enter__.return_value = data
    mock.return_value = handle
    return mock

# FIXME is really worth it?
class TestUtils(unittest.TestCase):

    @mock.patch('ipcamweb.utils.os.path')
    def test_ensure_secret_file_exists(self, mock_os_path):
        mock_os_path.exists.return_value = True
        m = mock_open(data=StringIO('random'))
        with mock.patch('ipcamweb.utils.open', m, create=True):
            self.assertEqual(ensure_secret(), "random")
        m.assert_called_once_with(os.environ['HOME']+"/.ipcamweb", 'r')

if __name__ == '__main__':
    unittest.main()
