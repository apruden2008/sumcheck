from field_element import FieldElement
from polynomial import Polynomial
from term import Term
from prover import Prover

def main():

    # Get user input for the prime field, and cast that value into an integer
    field_modulus = int(input("Enter a value for the field modulus that the polynomial is defined over: "))

    # Query the user for the number of total terms (non-constant) in the polynomial
    term_count = int(input("How many non-constant terms is the polynomial comprised of?: "))

    # Query the user for a constant term, if it exists
    poly_const = int(input("What is the constant term? If none, input '0': "))

    # Initialize a list for polynomial terms
    poly_terms = []

    # Iterate through the (non-constant) terms of the polynomial and convert the coefficients to field elements
    # Then, convert those field elements & exponents into a full term, and append to the poly_terms list
    for i in range(term_count):

        # Query the user for the coefficient of the ith term of the polynomial
        term_coeff = int(input("What is the value of the coefficient for the first term: "))

        # Query the user for the exponent, or degree, of the ith term
        term_power = int(input("What is the degree of the variable in this term: "))

        # Convert the coefficient to a field element
        fe = FieldElement(term_coeff, field_modulus)

        # Create a Term object with the coefficient, variable number, and exponent/power
        pt = Term(fe, 1, term_power)

        # Add the terms to the list defined above
        poly_terms.append(pt)
    
    # Add the constant term to the poly_terms list
    poly_terms.append(Term(FieldElement(poly_const, field_modulus), 0, 0))

    # Generate the Polynomial object from the poly_terms list
    poly = Polynomial(poly_terms)

    # Print the polynomial string representation to the console
    print(str(poly))

if __name__ == '__main__':
    main()

