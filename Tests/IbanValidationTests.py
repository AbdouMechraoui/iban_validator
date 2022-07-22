
from Validation.IbanValidator import IbanValidator
import unittest

class IbanValidatorTests(unittest.TestCase):
    
    def raw_input_to_alphanumeric(self, iban):
        """ Takes in raw iban, which may contain lower case, special characters
            and returns all caps alphanumeric string. 
            Input:
                - iban: (string)
            Output:
                - processed_iban: (string)
        """
        processed_iban = "".join(i for i in iban if i.isalnum())    
        processed_iban = processed_iban.upper()
        return processed_iban
    
    def test_success_cases(self):
        """ Tests success cases, where validate_iban returns true. 
            Raises 'AssertionError' when test fails. 
        """
        success_cases = [ 
                    "LI21 0881 0000 2324 013A A", 
                    "li21 0881 0000 2324-013A a",
                    "li21-0881-0000-2324-013aa", 
                    "Li21 0881 0000 2324 013Aa",
                    "lI21 08810000 2324 013 AA",
                    "LI61 0880 0795 4349 9883 1"
                    ]

        val = IbanValidator()
        for i, test_case in enumerate(success_cases):
            iban = self.raw_input_to_alphanumeric(test_case) 
            self.assertTrue(val.validate_iban(iban), "Failure in 'success cases' list, case no: "+ str(i+1))

    def test_failure_cases(self):
        """ Tests failure cases, where validate_iban returns false. 
            Raises 'AssertionError' when test fails. 
        """
        failure_cases = [
                        "DE5 9290501010001149590",
                        "de592905010ase51149590", 
                        "LI21@0881#0000$23244013$aa",
                        "DE21 4579 6456 4575 LI34 5",
                        "LT12 1000 0111 0100 1000",
                        "NL94 ABNA 1196 7204 60"
                        ]

        val = IbanValidator()
        for i, test_case in enumerate(failure_cases):
            iban = self.raw_input_to_alphanumeric(test_case)  
            self.assertFalse(val.validate_iban(iban), "Failure in 'failure cases' list, case no: "+ str(i+1))

    
if __name__ == '__main__':
    unittest.main()
    