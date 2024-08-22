import unittest

from field_element.field_element import FieldElement
from term.term import Term
from polynomial.polynomial import Polynomial
import pdb

class TestPolynomial(unittest.TestCase):
    def setUp(self):
        self.test_modulus = 7
        self.test_field_elements = [FieldElement(1, self.test_modulus),
                               FieldElement(1, self.test_modulus),
                               FieldElement(2, self.test_modulus),
                               FieldElement(3, self.test_modulus)]
        self.test_terms = [Term(self.test_field_elements[0], 0, 0), 
                      Term(self.test_field_elements[1], 1, 1),
                      Term(self.test_field_elements[2], 2, 4),
                      Term(self.test_field_elements[3], 3, 1)]
        self.test_points_vector = [3,2,2]
        # 1 + 1(2) + 2(2)^4 + 3(2)

    # Flesh out with more tests
    def test_create(self):
        test_poly = Polynomial(self.test_terms)

    def test_evaluation(self):
        test_poly = Polynomial(self.test_terms)
        print(test_poly)
        result = test_poly.evaluate(self.test_points_vector)
        self.assertEqual(result, FieldElement(0, 7))
        print(result)

    def test_zero_evaluation(self):
        test_zero_vector = [0,0,0]
        test_poly = Polynomial(self.test_terms)
        result = test_poly.evaluate(test_zero_vector)
        self.assertEqual(result, self.test_field_elements[0])

    def test_degree(self):
        test_poly = Polynomial(self.test_terms)
        result = test_poly.degree()
        self.assertEqual(result, 4)

    def test_dims(self):
        test_poly = Polynomial(self.test_terms)
        result = test_poly.dims()
        self.assertEqual(result, len(self.test_terms)-1) # one less because there is a constant, this could be more robust

if __name__ == '__main__':
    unittest.main()

