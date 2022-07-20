
from validator import iban_validator
import re



def handleTests():
    """
    Handles tests.
    """
    test_ibans = ["DE59290501010001149590", "LI21 0881 0000 2324 013A A", "li21 0881 0000 2324-013A a",
    "de592905010ase51149590", "li21-0881-0000-2324-013aa", "LI21@0881#0000$23244013$aa",
    "Li21 0881 0000 2324 013Aa"]

    test_results = ["Invalid IBAN!", "Valid IBAN!", "Valid IBAN!", "Invalid IBAN!", "Valid IBAN!",
    "Invalid IBAN!", "Valid IBAN!"]

    for i in range(len(test_ibans)):

        input_iban=test_ibans[i]
        #Regex, validates country code and number of characters 
        if re.match("^(?:li|LI|Li|lI)(?:\s*[-]?[0-9a-zA-Z]){19}$", input_iban):
            #strip input spaces and dashes
            input_iban = "".join(i for i in input_iban if i.isalnum())    
            isValid = iban_validator(input_iban)    
            if isValid: result = "Valid IBAN!"  
            else:  result = "Invalid IBAN!"
        else:
            result = "Invalid IBAN!"
        
        assert result == test_results[i], "Test "+(i + 1 )+" Failed!"
    
    print("All tests completed successfully!")
        

if __name__ == '__main__':
    handleTests()
    