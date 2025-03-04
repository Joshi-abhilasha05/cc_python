import unittest
from app import add

class TestApp(unittest.TestCase):
    def Test_add(self):
        self.assertEqual(add(2,3),5)
        self.assertEqual(add(4,6),10)
        self.assertEqual(add(12,13),25)
        self.assertEqual(add(-1,-1),-2)
        self.assertEqual(add(1,2),3)

if __name__ == '__main__':
    unittest.main()        