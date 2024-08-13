import unittest
import pdb

from field_element.field_element import FieldElement
from term.term import Term

class TestTerm(unittest.TestCase):

    def test_evaluate(self):
        # pdb.set_trace()
        test_element = FieldElement(4,7)
        test_term = Term(test_element,1,2)
        point = 3
        result = test_term.evaluate(point)
        self.assertEqual(result, FieldElement(1, 7))

if __name__ == "__main__":
    unittest.main()
