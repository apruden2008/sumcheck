from field_element import FieldElement

# Define a term class
# TODO improve this with decorators

class Term:
    """Define a term, which is the combination of Field Element and variable"""

    def __init__(self, coefficient, var_number, var_exponent):
        """
        Initialize a Term object

        Parameters:
            coefficient: a Field Element coefficient for the given variable
            var_number: an int identifying which variable in the equation
            var_exponent: an int representing the exponent that variable is raised to (between 0 and 5)

        Raises:
            ValueError: If any of the coefficients are not instances of FieldElement.
            ValueError: If var_number is less than or equal to zero
        
        Attributes:
            coefficient: a Field element representing the coefficient of the term

        """
        # if not(isinstance(coefficient, FieldElement)):
            # raise ValueError("Coefficient must be a FieldElement.")
        self.coefficient = coefficient
        if var_number < 0:
            raise ValueError("Variable number must be greater than zero.")
        self.var_number = int(var_number)
        if var_exponent > 10 & var_exponent <0: 
            raise ValueError("exponent must be an integer value between 0 and 10.")
        self.var_exponent = int(var_exponent)

    def __repr__(self): 
        """
        Return a detailed string representation of the Term object.

        Returns:
            str: A string representing the internal structure of the Term, for debugging.
        """
        return f"Term(coefficient={self.coefficient}, number={self.var_number}, exponent={self. var_exponent})"

    def __str__(self):
        """
        Return a user-friendly string representation of a Term object

        Returns:
            str: A string representing the term in the form of "coef*(x_var_number)^var_exponent".
        """
        if self.var_number == 0:
            return f"{self.coefficient}"
        return f"{self.coefficient}*(x_{self.var_number})^{self.var_exponent}"

    def coefficient(self):
        """
        Return the coefficient of the term as a FieldElement
        """
        return self.coefficient

    def exponent(self):
        """
        Return the exponent of the variable
        """
        return self.var_exponent

    def evaluate(self, point):
        """
        Evaluate the term at a given point
        """
        point = FieldElement(point, self.coefficient.prime)
        if self.var_number == 0:
            return self.coefficient
        return self.coefficient * point**self.var_exponent
