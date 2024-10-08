from field_element import FieldElement
from polynomial import Polynomial
from term import Term
from prover import Prover

def main():

    # Get user input for the prime field, and cast that value into an integer
    # field_modulus = int(input("Enter a value for the field modulus that the polynomial is defined over: "))

    # Query the user for the number of total terms (non-constant) in the polynomial
    # term_count = int(input("Enter the number of terms in the polynomial. Note that each term is associated with a different variable: "))

    # Query the user for a constant term, if it exists
    # poly_const = int(input("What is the constant term? If none, input '0': "))

    # Initialize a list for polynomial terms with the constant
    # poly_terms = [(Term(FieldElement(poly_const, field_modulus), 0, 0))]

    # Generate the Polynomial object from the poly_terms list
    # Iterate through the (non-constant) terms of the polynomial and convert the coefficients to field elements
    # Then, convert those field elements & exponents into a full term, and append to the poly_terms list
    # for i in range(term_count):

        # Query the user for the coefficient of the ith term of the polynomial
        # term_coeff = int(input(f"Enter a value of the coefficient for the term {i+1}: "))

        # Query the user for the exponent, or degree, of the ith term
        # term_power = int(input(f"Enter the degree of the variable for the term {i+1}: "))

        # Convert the coefficient to a field element
        # fe = FieldElement(term_coeff, field_modulus)

        # Create a Term object with the coefficient, variable number, and exponent/power
        # Note that right now this logic assumes each term has a different variable
        # pt = Term(fe, (i+1), term_power)

        # Add the terms to the list defined above
        # poly_terms.append(pt)
    
    # poly = Polynomial(poly_terms)

    # Print the polynomial string representation to the console

    # print("Your polynomial is: \n")
    # print(str(poly))

    # Initialize a list that 
    # eval_point = []
    
    # Query user for input on the evaluation point

    # for i in range(term_count):
    #     # Query the user for the value of each variable in turn
    #     value = int(input(f"Enter the value of the variable {i+1}: ")) % field_modulus
    #     eval_point.append(value)
    # 
    # print(eval_point)
    # print(poly.evaluate(eval_point))
    print("hi")

if __name__ == '__main__':
    main()

