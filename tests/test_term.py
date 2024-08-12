# make some tests

from field_element.field_element import FieldElement
from term.term import Term

def test_evaluate():
    test_element = FieldElement(2,7)
    test_term = Term(test_element,1,1)
    point = 2
    result = test_term.evaluate(point)
    print(result)

if __name__ == "__main__":
    test_evaluate()
