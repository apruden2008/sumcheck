from field_element import FieldElement

# Define a term class

class Term:
    """Define a term, which is the combination of Field Element and variable"""

    def __init__(self, coefficient, var_number, var_power):
        """
        Initialize a Term object

        Parameters:
            coefficient: a Field Element coefficient for the given variable
            var_number: an int identifying which variable in the equation
            var_power: an int representing the power that variable is raised to (between 0 and 5)

        Raises:
            ValueError: If any of the coefficients are not instances of FieldElement.
            ValueError: If var_number is less than or equal to zero
        
        Attributes:
            coefficient: a Field element representing the coefficient of the term

        """
        # if not(isinstance(coefficient, FieldElement)):
            # raise ValueError("Coefficient must be a FieldElement.")
        self.coefficient = coefficient
        if var_number <= 0:
            raise ValueError("Variable number must be greater than zero.")
        self.var_number = int(var_number)
        if var_power > 10 & var_power <0: 
            raise ValueError("Power must be an integer value between 0 and 10.")
        self.var_power = int(var_power)

    def __repr__(self): 
        """
        Return a detailed string representation of the Polynomial object.

        Returns:
            str: A string representing the internal structure of the Term, for debugging.
        """
        return f"Term(coefficient={self.coefficient}, number={self.var_number}, power={self. var_power})"

    def __str__(self):
        """
        Return a user-friendly string representation of a Term object

        Returns:
            str: A string representing the term in the form of "coef*(x_var_number)^var_power".
        """
        return f"{self.coefficient}*(x_{self.var_number})^{self.var_power}"

    def coefficient(self):
        """
        Return the coefficient of the term as a FieldElement
        """
        return self.coefficient
