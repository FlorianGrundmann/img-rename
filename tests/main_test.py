import unittest
import mock

from context import main

class Main_test(unittest.TestCase):
    
    def test_parse_args_returns_arg(self):
        dir = "testDir"
        flag = "-r"
        input_args = [dir, flag]
        
        args = main.parse_args(input_args)
        
        self.assertEquals(dir, args.dir)
        self.assertEquals(True, args.recursive)

if __name__ == '__main__':
    unittest.main()
