from term import Term

# Logic defining a polynomial object built from finite field elements

class Polynomial:
    """Define a polynomial object from field elements"""

    def __init__(self, terms):
        """
        Initialize a Polynomial object

        Parameters:
            terms (list of Terms): A list of Term objects representing terms of the polynomial. 

        Raises:
            ValueError: If any of the terms are not instances of a Term

        Attributes:
            terms: a list of terms that make up the polynomial
        """
        if not all(isinstance(tm, Term) for tm in terms):
            raise ValueError("All coefficients must be Terms.")
        self.terms = terms
        self.prime = terms[0].coefficient.prime  # TODO make this into an actual test

    def __repr__(self):
        """
        Return a detailed string representation of the Polynomial object.

        Returns:
            str: A string representing the internal structure of the Polynomial, for debugging.
        """
        return f"Polynomial(terms={self.terms})"

    def __str__(self):
        """
        Return a user-friendly string representation of the Polynomial object.

        Returns:
            str: A string representing the polynomial in the form of "coef*x^i + ...".
        """
        terms = []
        for i, term in enumerate(self.terms):
            terms.append(f"{term}")
        return " + ".join(terms)

    def evaluate(self, x):
        """
        Return an evaluation of the polynomial at a given point

        Returns: 
            The result as a Field Element from a given evaluation of a polynomial
        """

        result = FieldElement(0, self.prime)
        x = FieldElement(x, self.prime)  # Convert x to a FieldElement
        for i, coeff in enumerate(self.coefficients):
            result += coeff * (x ** i)
        return result

    def degree(self):
        """
        Return the degree of the polynomial.

        Returns:
            int: The degree of the polynomial, which is the highest power of x with a non-zero coefficient.
        """
        return len(self.coefficients) - 1

