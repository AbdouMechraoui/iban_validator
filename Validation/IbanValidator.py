import re
import string
from itertools import chain 

class IbanValidator:

    #Alphabets to digits dict
    alphas = {k : v for v, k in chain(enumerate(string.ascii_uppercase, 10), enumerate(string.ascii_lowercase, 10))}
    #ASCII to (10-35) integers used by translate
    alphas_uniCode = {ord(k): str(v) for k, v in alphas.items()}

    def get_iban_numerical(self, iban):
        """ Transofroms alphabets to their corresponding uniCodes. """
        return iban.translate(self.alphas_uniCode)

    def generate_check_digits(self, iban):
        """
        Generates check digits to compare with original check digits
        Input: 
            - iban: (string)
        Output
            - Two digits check digits: (string)
        """
        iban_num = self.get_iban_numerical(iban[4:] + iban[:2] + "00")
        #Calculate checksum
        checksum = 98 - (int(iban_num) % 97)
        return '{:0>2}'.format(checksum)

    def check_iban(self, iban):
        """ 
        Calculates iban % 97 to validate iban 
        Input: 
            - iban: (string)
        Output:
            - Valid or Invalid: (bool)
        """
        iban_num = self.get_iban_numerical(iban[4:] + iban[:4])
        return (int(iban_num) % 97 == 1)    

    def iban_validator(self, input_iban):
        """
        Combines all tests to validate iban.
        Input:
            - Input_iban: (string)
        Output: 
            - Valid or Invalid: (bool)
        """
        if self.generate_check_digits(input_iban) == input_iban[2:4] and self.check_iban(input_iban):
            return True
        else:
            return False

"""
if __name__ == '__main__':
    handleInput()
""" 