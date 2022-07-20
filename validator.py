import re

#Alphabets to digits dict
alphas = {"A": 10, "a": 10,
                "B": 11, "b": 11,
                "C": 12, "c": 12, 
                "D": 13, "d": 13,
                "E": 14, "e": 14,
                "F": 15, "f": 15,
                "G": 16, "g": 16,
                "H": 17, "h": 17,
                "I": 18, "i": 18,
                "J": 19, "j": 19,
                "K": 20, "k": 20,
                "L": 21, "l": 21,
                "M": 22, "m": 22,
                "N": 23, "n": 23,
                "O": 24, "o": 24,
                "P": 25, "p": 25,
                "Q": 26, "q": 26,
                "R": 27, "r": 27,
                "S": 28, "s": 28,
                "T": 29, "t": 29,
                "U": 30, "u": 30,
                "V": 31, "v": 31,
                "W": 32, "w": 32,
                "X": 33, "x": 33,
                "Y": 34, "y": 34,
                "Z": 35, "z": 35,
            }
            #"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9
#Get unicodes of alphas dict
alphas_uniCode = {ord(k): str(v) for k, v in alphas.items()}


def get_iban_numerical(iban):
    """ Transofroms alphabets to their corresponding uniCodes. """
    return iban.translate(alphas_uniCode)

def checkDigits(iban):
    """
    Generates check digits to compare with original check digits
    Input: 
        - iban: (string)
    Output
        - Two digits check digits: (string)
    """
    
    iban_num = get_iban_numerical(iban[4:] + iban[:2] + "00")
    #Calculate checksum
    checksum = 98 - (int(iban_num) % 97)
    return '{:0>2}'.format(checksum)

def check_iban(iban):
    """ 
    Calculates iban % 97 to validate iban 
    Input: 
        - iban: (string)
    Output:
        - Valid or Invalid: (bool)
    """
    
    iban_num = get_iban_numerical(iban[4:] + iban[:4])
    return (int(iban_num) % 97 == 1)    

def iban_validator(input_iban):
    """
    Combines all tests to validate iban.
    Input:
        - Input_iban: (string)
    Output: 
        - Valid or Invalid: (bool)
    """
    
    if checkDigits(input_iban) == input_iban[2:4] and check_iban(input_iban):
        #print("Valid IBAN!")
        return True
    else:
        #print("Invalid IBAN!")
        return False
        
def handleInput():
    """
    Handles CL user input.
    """

    print("############### IBAN Validator ###############")
    isExit = "1"

    while isExit == "1":
        input_iban=input("Enter IBAN (Only Letters and Numbers Please!): ")
        #Regex, validates country code and number of characters 
        if re.match("^(?:li|LI|Li|lI)(?:\s*[-]?[0-9a-zA-Z]){19}$", input_iban):
            #strip input spaces and dashes
            input_iban = "".join(i for i in input_iban if i.isalnum())    
            print("Entered IBAN is: ", input_iban) 
            isValid = iban_validator(input_iban)    
            print("Valid IBAN!") if isValid else  print("Invalid IBAN!")
        else:
            print("Invalid IBAN!")
        
        #Handle retries 
        isExit = input("Press 0 to exit, 1 to try again: ")
        while(not re.match("^\s*[01]{1}$", isExit)):
            print("Invalid option, try again! ")
            isExit = input("Press 0 to exit, and 1 to try again: ")
        
    print("Terminating...")


if __name__ == '__main__':
    handleInput()
    