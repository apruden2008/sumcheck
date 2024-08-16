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
        Get all of the generated Boolean hypercube points for polynomial

        Returns:
            we'll find out
        """
        return self.generate_hypercube_points()

    def sum_hypercube(self):
        """
        Sum the polynomial over the Boolean hypercube {0, 1}^n.

        :return: The sum over the Boolean hypercube.
        """
        n = len(self.polynomial.coefficients)
        total_sum = 0
        for point in self.generate_hypercube_points(n):
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

