import unittest
from field_element.field_element import FieldElement

class TestFieldElement(unittest.TestCase):

    def test_create(self):
        # Create a basic field element consisting of a value and a prime modulus
        value = 4
        prime = 7
        fe = FieldElement(value, prime)
        self.assertEqual(fe, FieldElement(4,7))
        self.assertEqual(fe.value, value)
        self.assertEqual(fe.prime, prime)

        # Create a field element greater than the prime modulus (should fail)
        value = 25
        prime = 23
        with self.assertRaises(AssertionError):
            FieldElement(value, prime)
    
        # Create a field element with a nonprime modulus
        value = 36
        prime = 40
        with self.assertRaises(AssertionError):
            FieldElement(value, prime)

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
        
        # Try adding elements from two different fields; should fail
        fe1 = FieldElement(6,13)
        fe2 = FieldElement(7,43)
        with self.assertRaises(AssertionError):
            fe1 + fe2

if __name__ == '__main__':
    unittest.main()
