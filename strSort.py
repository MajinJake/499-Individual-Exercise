import unittest

# This commit is for the video
def strSort(list):
    return sorted(list)
    
    
class TestStrSort(unittest.TestCase):
    def test_characters(self):
        list = ['j','a','k','e']
        self.assertEqual(strSort(list),['a','e','j','k'])
        
    def test_null(self):
        list = []
        self.assertEqual(strSort(list),[])
        
    def test_strings(self):
        list = ['jake','wants','some','candy']
        self.assertEqual(strSort(list),['candy','jake','some','wants'])
        