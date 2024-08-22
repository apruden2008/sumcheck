import unittest
import pdb

from field_element.field_element import FieldElement
from term.term import Term

class TestTerm(unittest.TestCase):

    def setUp(self):
        """Common setup code for all tests."""
        self.test_modulus = 7
        self.test_element =  FieldElement(4,7)

    def test_evaluate(self):
        # pdb.set_trace()
        test_term = Term(self.test_element,1,2)
        point = 3
        result = test_term.evaluate(point)
        self.assertEqual(result, FieldElement(1, 7))

    def test_as_dict(self):
        test_term = Term(self.test_element,3,4)
        attr_dict = test_term.as_dict()
        self.assertEqual(attr_dict["coefficient"], FieldElement(4,7))
        self.assertEqual(attr_dict["var_number"], 3)
        self.assertEqual(attr_dict["var_exponent"], 4)

if __name__ == "__main__":
    unittest.main()
