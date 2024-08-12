import unittest

from field_element.field_element import FieldElement
from term.term import Term

class TestTerm(unittest.TestCase):

    def test_evaluate(self):
        test_element = FieldElement(2,7)
        test_term = Term(test_element,1,3)
        point = 2
        result = test_term.evaluate(point)
        print(result)

if __name__ == "__main__":
    unittest.main()
