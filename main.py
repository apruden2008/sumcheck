from field_element import FieldElement

def main():

    # Take user input for the first field element
    value1 = int(input("Enter the value for the first field element: "))
    modulus1 = int(input("Enter the modulus for the first field element: "))
    
    # Create the first field element
    fe1 = FieldElement(value1, modulus1)
    
    # Take user input for the second field element
    value2 = int(input("Enter the value for the second field element: "))
    modulus2 = int(input("Enter the modulus for the second field element: "))
    
    # Create the second field element
    fe2 = FieldElement(value2, modulus2)
    
    # Check if both field elements are in the same field (same modulus)
    if modulus1 != modulus2:
        print("Error: The moduli for the two field elements must be the same.")
        return
    
    # Perform the addition operation
    result = fe1 + fe2
    
    # Print the result
    print(f"The result of adding {fe1} and {fe2} is: {result}")

if __name__ == '__main__':
    main()


