from field_element import FieldElement
from term import Term
from polynomial import Polynomial

# A prover class for the sumcheck protocol

class Prover:
    def __init__(self, polynomial):
        """
        Initialize the Prover with a multivariate polynomial.

        Parameters:
            polynomial: Polynomial object representing the multivariate polynomial.

        Raises:
            TypeError: If the input is not a polynomial object

        Attributes: 
            polynomial: the polynomial object, representing the polynomial to be evaluated
        """
        if not isinstance(polynomial, Polynomial):
            raise TypeError(f"Expected a Polynomial object, but got {type(polynomial).__name__}.")
        self.polynomial = polynomial

    def evaluate_polynomial(self, point):
        """
        Evaluate the polynomial at a given point.

        Parameters:
            point: A field element as the point of evaluation for the polynomial
            
        Returns:
            The polynomial evaluated at the given point.

        """
        return self.polynomial.evaluate(point)

    def _generate_hypercube_points(self, dims = 0):
        """
        Generate all points in the Boolean hypercube {0, 1}^n.

        Parameters:
            dims_to_reduce: The number of dimensions over which to generate the Boolean hypercube

        Returns: 
            A generator of all points in the Boolean hypercube.
        """
        if dims >= len(self.polynomial.var_terms):
            raise ValueError("Cannot reduce to less dimensions than variables")
        n = self.polynomial.dims() - dims

        for i in range(2**n):
            yield [int(x) for x in bin(i)[2:].zfill(n)]
    
    def get_hypercube_points(self):
        """
        Getter for the generated Boolean hypercube points for the polynomial to be proven

        Returns:
            Generator for the hypercube points for the given polynomial
        """
        return self._generate_hypercube_points()

    def sum_hypercube(self, dims = 0):
        """
        Sum the polynomial over the Boolean hypercube {0, 1}^n.

        Returns:
            The sum of the evaluations of the polynomial over the Boolean hypercube
        """
        total_sum = FieldElement(0, self.polynomial.prime)
        for point in self._generate_hypercube_points(dims):
            total_sum += self.evaluate_polynomial(point)
        return total_sum

    def send_claimed_sum(self):
        """
        Prover sends the claimed sum (S) to the Verifier.

        Returns:
            The sum over the boolean hypercube for a given Polynomial to be sent to the verifier
        """
        return self.sum_hypercube()

    def generate_univariate_polynomial(self, variable):
        """
        Prover chooses one variable to leave free and generates a new univariate polynomial by evaluating other variables over boolean hypercube

        Parameters:
            variable: the variable in the multivariate polynomial to be left free

        Returns:
            A new Polynomial object with a single variable
        """
        if variable <= 0 or variable > len(self.polynomial.var_terms):
            raise ValueError("Cannot create a univariate polynomial from a term that doesn't exist. Please check the variable number argument and try again")
        # TODO redo all this as list comprehension
        new_terms = []
        old_terms = []
        for term in self.polynomial.terms:
            if term.var_number == variable:
                new_terms.append(term)    
            else:
                old_terms.append(term)
        # Assumes you go in variable order
        terms_to_evaluate = Polynomial(old_terms)

        # Create a new constant term for the univariate polynomial by evaluating & summing all boolean inputs for other variables
        new_constant = Prover(terms_to_evaluate).sum_hypercube()
        # Convert the above into a Term object
        new_constant_term = Term(new_constant, 0, 1)

        # Create the new variable coefficient by multiplying the variable left free by two times the number of variables that have been fixed
        new_var_coefficient =2**len(terms_to_evaluate.var_terms)
        # Turn the result above into Field Element
        new_var_coefficient_fe = FieldElement(new_var_coefficient, self.polynomial.prime)
        # Turn the result above into a Term, using the `var_number` passed in as an argument (TODO need to keep the power)
        new_var_term = Term(new_var_coefficient, variable, 1)

        # Combine those terms into a new univariate polynomial and return this polynomial
        univariate_poly = Polynomial([new_constant_term, new_var_term])
        return(univariate_poly)
        
    def send_univariate_polynomial(self, fixed_variable):
        """
        Prover sends the univariate polynomial to the Verifier after fixing one variable.

        Parameters:
            fixed_variable: The variable that is fixed (0 or 1).

        Returns:
            A new Polynomial object with one variable fixed
        """

