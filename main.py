import re
from Validation.IbanValidator import IbanValidator 

def handle_input():
    """
    Handles CL user input.
    """
    val = IbanValidator()

    print("############### IBAN Validator ###############")
    isExit = "1"

    while isExit == "1":
        input_iban=input("Enter IBAN (Only Letters and Numbers Please!): ")
        #Regex, validates country code and number of characters 
        if re.match("^(?:li|LI|Li|lI)(?:\s*[-]?[0-9a-zA-Z]){19}$", input_iban):
            #strip input spaces and dashes
            input_iban = "".join(i for i in input_iban if i.isalnum())    
            print("Entered IBAN is: ", input_iban) 
            isValid = val.iban_validator(input_iban)    
            print("Valid IBAN!") if isValid else  print("Invalid IBAN!")
        else:
            print("Entered IBAN is: ", input_iban) 
            print("Invalid IBAN!")
        
        #Handle retries 
        isExit = input("Press 0 to exit, 1 to try again: ")
        while(not re.match("^\s*[01]{1}$", isExit)):
            print("Invalid option, try again! ")
            isExit = input("Press 0 to exit, and 1 to try again: ")
        
    print("Terminating...")


if __name__ == '__main__':
    handle_input()
    