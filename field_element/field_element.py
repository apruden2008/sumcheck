# An implementation of the (multilinear) sumcheck protocol in Python

# First, define a primality test to ensure that all our fields are prime fields
# Prime fields are almost always what we will work with in cryptography

def is_prime(n):
    """Return True if n is a prime number, otherwise False."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Define a field element class

class FieldElement:
    """Represents an element of a finite field."""

    def __init__(self, value, prime):
        """Initialize field element by defining it's value and the prime modulus"""
        assert 0 <= value < prime, "Value not in field range"
        assert is_prime(prime) == True, "Value is not prime"
        self.value = value
        self.prime = prime
        # TODO need to handle the negative numbers

    def __add__(self, other):
        """
        Add two field elements.

        Args:
            other (FieldElement): The field element to add.

        Returns:
            FieldElement: A new field element representing the sum.

        Raises:
            AssertionError: If the elements are from different fields.
        """        
        assert self.prime == other.prime, "Cannot add two numbers in different fields"
        value = (self.value + other.value) % self.prime
        return FieldElement(value, self.prime)

    def __sub__(self, other):
        """
        Subtract one field element from another.

        Args:
            other (FieldElement): The field element to subtract.

        Returns:
            FieldElement: A new field element representing the difference.

        Raises:
            AssertionError: If the elements are from different fields.
        """
        assert self.prime == other.prime, "Cannot subtract two numbers in different fields"
        value = (self.value - other.value) % self.prime
        return FieldElement(value, self.prime)

    def __mul__(self, other):
        """
        Multiply two finite field elements.

        Args: 
            other(FieldElement): the field element to multiply.

        Returns: 
            FieldElement: A new field element representing the product.

        Raises:
            AssertionError: If the elements are from two different fields 
        """
        assert self.prime == other.prime, "Cannot multiply two numbers in different fields"
        value = (self.value * other.value) % self.prime
        return FieldElement(value, self.prime)

    def __truediv__(self, other):
        """
        Divide one field element by another.

        Args:
            other (FieldElement): The field element to divide by.

        Returns:
            FieldElement: A new field element representing the quotient.

        Raises:
            AssertionError: If the elements are from different fields.
        """
        assert self.prime == other.prime, "Cannot divide two numbers in different fields"
        value = (self.value * pow(other.value, self.prime - 2, self.prime)) % self.prime
        return FieldElement(value, self.prime)

    def __pow__(self, exponent):
        """
        Raise the field element to a power.

        Args:
            exponent (int): The exponent to raise the element to.

        Returns:
            FieldElement: A new field element representing the power.
        """
        value = pow(self.value, exponent, self.prime)
        return FieldElement(value, self.prime)

    def __eq__(self, other):
        """
        Check if two field elements are equal.

        Args:
            other (FieldElement): The field element to compare with.

        Returns:
            bool: True if the elements are equal, False otherwise.
        """
        if other is None:
            return False
        return self.value == other.value and self.prime == other.prime

    def __ne__(self, other):
        """
        Check if two field elements are not equal.

        Args:
            other (FieldElement): The field element to compare with.

        Returns:
            bool: True if the elements are not equal, False otherwise.
        """
        return not (self == other)

    def __repr__(self):
        """
        Return the string representation of the field element

        Returns: 
            string: The string representation of the field element
        """
        return f"FieldElement({self.value}, {self.prime})"

