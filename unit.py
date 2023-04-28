import unittest

class Testing(unittest.TestCase):

    def test_is_str(self):
       self.assertEqual("Hello world", "Hello world")

    def test_is_num(self):
        self.assertEqual("01101101","01101101" )  

    def test_is_list(self):
        self.assertListEqual([0,1,0,0,1,0],[0,1,0,0,1,0]) 

    def test_item_is_num(self):
        for item in [0,1,0,0,1,0]:
            self.assertIsInstance(item, int)      
   
if __name__ == "__main__":
    unittest.main()        
