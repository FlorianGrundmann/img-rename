import unittest
import mock

from context import main

class Main_test(unittest.TestCase):
    
    def test_parse_args_returns_arg(self):
        dir = "testDir"
        input_args = [dir]
        
        args = main.parse_args(input_args)
        
        self.assertEquals(dir, args.dir)

if __name__ == '__main__':
    unittest.main()
