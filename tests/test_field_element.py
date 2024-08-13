import unittest
from field_element.field_element import FieldElement

class TestFieldElement(unittest.TestCase):
    
    def test_addition(self):
        # Basic Test
        fe1 = FieldElement(1, 7)
        fe2 = FieldElement(2, 7)
        result = fe1 + fe2
        self.assertEqual(result, FieldElement(3, 7))
        print(str(result))
        
        # Wrap around
        fe1 = FieldElement(13,37)
        fe2 = FieldElement(25,37)
        result = fe1 + fe2
        self.assertEqual(result, FieldElement(1, 37))
        print(str(result))
        
        # Sum to a multiple of modulus
        fe1 = FieldElement(6,13)
        fe2 = FieldElement(7,13)
        result = fe1 + fe2
        self.assertEqual(result, FieldElement(0, 13))
        print(str(result))
        
if __name__ == '__main__':
    unittest.main()
