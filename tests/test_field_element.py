import unittest
from field_element.field_element import FieldElement

class TestFieldElement(unittest.TestCase):
    
    def test_addition(self):
        fe1 = FieldElement(1, 7)
        fe2 = FieldElement(2, 7)
        result = fe1 + fe2
        self.assertEqual(result, FieldElement(3, 7))
        print(str(result))

if __name__ == '__main__':
    unittest.main()
