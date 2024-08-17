from field_element import FieldElement
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

    def generate_hypercube_points(self):
        """
        Generate all points in the Boolean hypercube {0, 1}^n.

        Parameters:
            dim: the dimension of the hypercube, aka the number of unique variables

        Returns: 
            A generator of all points in the Boolean hypercube.
        """

        n = self.polynomial.dims()
        print(n)

        for i in range(2**n):
            yield [int(x) for x in bin(i)[2:].zfill(n)]
    
    def get_hypercube_points(self):
        """
        Getter for the generated Boolean hypercube points for the polynomial to be proven

        Returns:
            Generator for the hypercube points for the given polynomial
        """
        return self.generate_hypercube_points()

    def sum_hypercube(self):
        """
        Sum the polynomial over the Boolean hypercube {0, 1}^n.

        Returns:
            The sum of the evaluations of the polynomial over the Boolean hypercube
        """
        total_sum = FieldElement(0, self.polynomial.prime)
        for point in self.generate_hypercube_points():
            total_sum += self.evaluate_polynomial(point)
        return total_sum

    def send_claimed_sum(self):
        """
        Prover sends the claimed sum (S) to the Verifier.
        """
        return self.sum_hypercube()

    def send_univariate_polynomial(self, fixed_variable):
        """
        Prover sends the univariate polynomial to the Verifier after fixing one variable.

        :param fixed_variable: The variable that is fixed (0 or 1).
        :return: A new Polynomial object with one variable fixed.
        """
        # Create a univariate polynomial by fixing one variable
        fixed_poly = self.polynomial.fix_variable(fixed_variable)
        return fixed_poly

