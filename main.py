import re
from Validation.IbanValidator import IbanValidator 

def handle_input():
    """
    Handles CL user input.
    """
    val = IbanValidator()

    print("############### IBAN Validator ###############")
    is_exit = "1"

    while is_exit == "1":
        input_iban = input("Enter IBAN (Only Letters and Numbers Please!): ")
        iban = "".join(i for i in input_iban if i.isalnum()) 
        iban = iban.upper()

        print("Entered IBAN is: ", iban) 
        is_valid = val.validate_iban(iban) 
        print("Valid IBAN!") if is_valid else  print("Invalid IBAN!")
        
        #Handle retries 
        is_exit = input("Press 0 to exit, 1 to try again: ")
        while(not re.match("^\s*[01]{1}$", is_exit)):
            print("Invalid option, try again! ")
            is_exit = input("Press 0 to exit, and 1 to try again: ")
        
    print("Terminating...")


if __name__ == '__main__':
    handle_input()
    