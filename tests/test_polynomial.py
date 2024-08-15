import unittest

from field_element.field_element import FieldElement
from term.term import Term
from polynomial.polynomial import Polynomial
import pdb

class TestPolynomial(unittest.TestCase):
    
    def test_evaluation(self):
        test_modulus = 7
        test_field_elements = [FieldElement(1, test_modulus),
                               FieldElement(1, test_modulus),
                               FieldElement(2, test_modulus),
                               FieldElement(3, test_modulus)]
        test_terms = [Term(test_field_elements[0], 0, 0), 
                      Term(test_field_elements[1], 1, 1),
                      Term(test_field_elements[2], 2, 1),
                      Term(test_field_elements[3], 3, 1)]
        test_points_vector = [3,2,2]
        test_poly = Polynomial(test_terms)
        # 1 + 1(2) + 2(2) + 3(2)
        # pdb.set_trace()
        print(str(test_poly))
        result = test_poly.evaluate(test_points_vector)
        self.assertEqual(result, FieldElement(0, 7))
        print(str(result))

    def test_degree(self):
        test_modulus = 7
        test_field_elements = [FieldElement(1, test_modulus),
                               FieldElement(2, test_modulus),
                               FieldElement(3, test_modulus)]
        test_terms = [Term(test_field_elements[0], 1, 3), 
                      Term(test_field_elements[1], 2, 1),
                      Term(test_field_elements[2], 3, 1)]
        test_points_vector = [2,2,3]
        test_poly = Polynomial(test_terms)

        result = test_poly.degree()
        self.assertEqual(result, 3)
        # print(str(result))

    def test_zero_evaluation(self):
        test_modulus = 13
        test_field_elements = [FieldElement(4, test_modulus),
                               FieldElement(12, test_modulus),
                               FieldElement(3, test_modulus)]
        test_constant_term = FieldElement(5, test_modulus)
        # Term(coefficient, var_number, var_power)
        test_terms = [Term(test_constant_term, 0, 1),
                      Term(test_field_elements[0], 1, 3), 
                      Term(test_field_elements[1], 2, 1),
                      Term(test_field_elements[2], 3, 1)]
        test_points_vector = [0,0,0]
        test_poly = Polynomial(test_terms)
        result = test_poly.evaluate(test_points_vector)
        self.assertEqual(result, test_constant_term)

if __name__ == '__main__':
    unittest.main()

