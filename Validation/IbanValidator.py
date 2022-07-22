import re
import string
from itertools import chain 

class IbanValidator:

    #Alphabets to digits dict
    ALPHAS = {k : v for v, k in chain(enumerate(string.ascii_uppercase, 10))}
    #ASCII to (10-35) integers used by translate
    ALPHAS_UNICODE = {ord(k): str(v) for k, v in ALPHAS.items()}

    def verify_iban_format(self, iban):
        """ Verifies country code and length """
        return (re.match("^(?:LI)(?:\s*[-]?[0-9A-Z]){19}$", iban) != None)

    def convert_iban_to_numerics(self, iban):
        """ Converts alphabets to their corresponding nummerics. """
        return iban.translate(self.ALPHAS_UNICODE)

    def compare_check_digits(self, iban):  
        """
        Compares original check digits and generated check digits.
        Input: 
            - iban: (string)
        Output
            - original_check_digits == generated_check_digits: (boolean)
        """
        iban_num = self.convert_iban_to_numerics(iban[4:] + iban[:2] + "00")
        #Calculate check_digits
        orig_check_digits = iban[2:4]
        gen_check_digits = '{:0>2}'.format(98 - (int(iban_num) % 97))
        return orig_check_digits == gen_check_digits

    def verify_iban_remainder(self, iban):
        """ 
        Calculates iban % 97 to validate iban 
        Input: 
            - iban: (string)
        Output:
            - Valid or Invalid: (bool)
        """
        iban_num = self.convert_iban_to_numerics(iban[4:] + iban[:4])
        return (int(iban_num) % 97 == 1)    

    def validate_iban(self, iban):
        """
        Combines all tests to validate iban.
        Input:
            - Input_iban: (string)
        Output: 
            - Valid or Invalid: (bool)
        """
        return (self.verify_iban_format(iban)
            and self.compare_check_digits(iban) 
            and self.verify_iban_remainder(iban))
