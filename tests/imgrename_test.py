import mock
import unittest

import os.path

from context import ir
from context import exifutil


class imgrenameTest(unittest.TestCase):

    @mock.patch("imgrename.core.os.path")
    @mock.patch("imgrename.exifutil.get_creation_date")
    def test_create_name_returns_correct_name(self, get_creation_date_mock, path_mock):
        path = "fakepath"
        get_creation_date_mock.return_value = "2016-12-20"
        path_mock.isdir.imgrename.return_value = True
        path_mock.join.side_effect = lambda a, b: "\\".join([a, b]) 
        path_mock.dirname.return_value = path
        
        expected = "2016-12-20-img-000.jpg"
        result = ir.get_new_name(path, path)
        
        self.assertEqual(expected, result)

    @mock.patch("imgrename.exifutil.get_creation_date")
    def test_create_name_returns_none_if_no_exif(self, get_creation_date_mock):
        get_creation_date_mock.return_value = None

        self.assertTrue(ir.get_new_name("test.jpg", "destinationPath") is None)
        

if __name__ == '__main__':
    unittest.main()
