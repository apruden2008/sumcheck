import unittest
from field_element.field_element import FieldElement
from term.term import Term
from polynomial.polynomial import Polynomial
from prover.prover import Prover

class TestProver(unittest.TestCase):

    def setUp(self):
        """Common setup code for all tests."""
        self.test_modulus = 7
        self.test_field_elements = [
            FieldElement(1, self.test_modulus),
            FieldElement(1, self.test_modulus),
            FieldElement(2, self.test_modulus),
            FieldElement(3, self.test_modulus)
        ]
        self.test_terms = [
            Term(self.test_field_elements[0], 0, 0), 
            Term(self.test_field_elements[1], 1, 1),
            Term(self.test_field_elements[2], 2, 1),
            Term(self.test_field_elements[3], 3, 1)
        ]
        self.test_poly = Polynomial(self.test_terms)
        self.test_point = [2,2,2]

    def test_create(self):

        # Create a prover object from the test polynomial
        Prover(self.test_poly)

        # Should fail if you pass in the list of terms instead of Polynomial object
        with self.assertRaises(TypeError):
            Prover(self.test_terms)

    def test_evaluate(self):
        test_prover = Prover(self.test_poly)
        result = test_prover.evaluate(test_point)
        self.assertEqual(FieldElement(6, self.test_modulus, result))

    def test_
