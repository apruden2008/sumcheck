from field_element import FieldElement

# Logic defining a polynomial object built from finite field elements

class Polynomial:
    """Define a polynomial object from field elements"""

    def __init__(self, coefficients):
        """
        Initialize a Polynomial object.

        Parameters:
            coefficients (list of FieldElement): A list of FieldElement objects representing the coefficients
                                                 of the polynomial. The i-th element corresponds to the coefficient
                                                 of x^i.
            **Note, this assumes that the number of coefficients == the degree of the polynomial

        Raises:
            ValueError: If any of the coefficients are not instances of FieldElement.
            ValueError: If coefficients have different moduli.

        Attributes:
            coefficients (list of FieldElement): The list of coefficients of the polynomial.
            modulus (int): The prime modulus of the field in which the polynomial operates, inferred from the coefficients.
        """
        if not all(isinstance(coef, FieldElement) for coef in coefficients):
            raise ValueError("All coefficients must be FieldElements.")
        self.coefficients = coefficients
        self.prime = coefficients[0].prime  # TODO make this into an actual test

    def __repr__(self):
        """
        Return a detailed string representation of the Polynomial object.

        Returns:
            str: A string representing the internal structure of the Polynomial, for debugging.
        """
        return f"Polynomial(coefficients={self.coefficients})"

    def __str__(self):
        """
        Return a user-friendly string representation of the Polynomial object.

        Returns:
            str: A string representing the polynomial in the form of "coef*x^i + ...".
        """
        terms = []
        for i, coeff in enumerate(self.coefficients):
            terms.append(f"{coeff}*x^{i}")
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

