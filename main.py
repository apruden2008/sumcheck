from field_element import FieldElement
from polynomial import Polynomial
from term import Term
from prover import Prover

def main():

# TODO At some point, make this a flag so you can actually input field elements if you want
    # Take user input for the first field element
    # value1 = int(input("Enter the value for the first field element: "))
    # modulus1 = int(input("Enter the modulus for the first field element: "))
    
    ## Create the first field element
    #fe1 = FieldElement(value1, modulus1)
    #
    ## Take user input for the second field element
    #value2 = int(input("Enter the value for the second field element: "))
    #modulus2 = int(input("Enter the modulus for the second field element: "))
    #
    ## Create the second field element
    #fe2 = FieldElement(value2, modulus2)
    #
    ## Check if both field elements are in the same field (same modulus)
    #if modulus1 != modulus2:
    #    print("Error: The moduli for the two field elements must be the same.")
    #    return
    #
    ## Perform the addition operation
    #result = fe1 + fe2
    #
    # Print the result
    # print(f"The result of adding {fe1} and {fe2} is: {result}")

    # Take user input for polynomial degree

    test_modulus = 7
    test_field_elements = [FieldElement(1, test_modulus),
                           FieldElement(2, test_modulus),
                           FieldElement(3, test_modulus)]

    test_terms = [Term(test_field_elements[0], 1, 1), 
                  Term(test_field_elements[1], 2, 1),
                  Term(test_field_elements[2], 3, 1)]
    
    test_poly = Polynomial(test_terms)
    print("testing polynomial methods\n")
    # print(test_poly.degree())
    print(str(test_poly))
    print(repr(test_poly))
    # print(test_poly.evaluate(4))
    print("#########\n")

    # print("testing prover methods\n")
    # test_prover = Prover(test_poly)
    # claimed_value = test_prover.evaluate_polynomial(4) 
    # print(claimed_value)
    # hypercube_points = test_prover.get_hypercube_points()
    # for point in hypercube_points:
    #     print(point)

if __name__ == '__main__':
    main()

