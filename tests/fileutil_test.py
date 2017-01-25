import unittest
import mock

from context import ir
from context import fileutil as fu

class Fileutil_test(unittest.TestCase):
    
    def test_search_files_returns_empty_list_if_dir_nonexisting(self):
        wrongPath = "this is not a path"
        self.assertRaises(NotADirectoryError, lambda: fu.get_all_file_names(wrongPath))
    
    @mock.patch("imgrename.fileutil.os")
    @mock.patch("imgrename.fileutil.os.path")
    def test_search_files_returns_list_if_dir_exists(self, path_mock, os_mock):
        dir = "fake dir"
        files = ["file1.txt", "file2.dat", "file3.txt"]
        path_mock.isdir.return_value = True
        os_mock.listdir.return_value = files

        self.assertTrue(len(fu.get_all_file_names(dir)) != 0)

    @mock.patch("imgrename.fileutil.os")
    @mock.patch("imgrename.fileutil.os.path")
    def test_search_files_returns_filtered_list(self, path_mock, os_mock):
        dir = "fake dir"
        files = ["file1.txt", "file2.dat", "file3.txt"]
        path_mock.isdir.return_value = True
        os_mock.listdir.return_value = files

        expected = ["file1.txt", "file3.txt"]
        result = fu.get_all_file_names(dir, ".txt")

        self.assertEquals(expected, result)

    @mock.patch("imgrename.fileutil.os")
    @mock.patch("imgrename.fileutil.os.path")
    def test_search_files_returns_empty_list_if_extension_not_present(self, path_mock, os_mock):
        dir = "fake dir"
        files = ["file1.txt", "file2.dat", "file3.txt"]
        path_mock.isdir.return_value = True
        os_mock.listdir.return_value = files

        emptyList = []
        result = fu.get_all_file_names(dir, ".jpg")

        self.assertEquals(emptyList, result)

if __name__ == '__main__':
    unittest.main()
