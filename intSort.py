import unittest


def intSort(list):
    return sorted(list)
    
    
class TestIntSort(unittest.TestCase):
    def test_simple(self):
        list = [5,6,7,1,2]
        sortedList = intSort(list)
        self.assertEqual(sortedList,[1,2,5,6,7])
        
    def test_null(self):
        list = []
        self.assertEqual(intSort(list),[])
        
    def test_negative(self):
        list = [-5,-6,-7,-1,-2]
        self.assertEqual(intSort(list),[-7,-6,-5,-2,-1])
        