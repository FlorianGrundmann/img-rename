import unittest
import mock

from context import exifutil as eu

class Exifutil_test(unittest.TestCase):
    
    @mock.patch("imgrename.exifutil.os.path")  
    def test_get_creating_date_returns_none_if_no_exif(self, path_mock):
        path_mock.isfile.return_value = True
        path = "fake path"

        self.assertTrue(eu.get_creation_date(path) is None)

    @mock.patch("imgrename.exifutil.os.path")
    @mock.patch("imgrename.exifutil.get_tags")
    def test_get_creation_date_returns_date(self, mock_get_tags, mock_path):
        mock_get_tags.return_value = {"a tag": "something", "EXIF DateTimeOriginal":"2016:12:20 111 test", "another tag":"something else"}
        mock_path.isfile.return_value = True
        path = "fake path"

        expected = "2016-12-20"
        result = eu.get_creation_date(path)

        self.assertEqual(expected, result)


    def test_get_creating_date_file_not_found(self):
        path = "fake path"
        self.assertRaises(FileNotFoundError, lambda: eu.get_creation_date(path))
        

    @mock.patch("imgrename.exifutil.os.path")
    @mock.patch("imgrename.exifutil.get_tags")
    def test_get_creation_date_returns_none_when_no_tags(self, mock_get_tags, mock_path):
        mock_get_tags.return_value = None
        mock_path.isfile.return_value = True
        path = "fake path"

        result = eu.get_creation_date(path)

        self.assertEqual(None, result)


if __name__ == '__main__':
    unittest.main()
