# -*- coding: utf-8 -*-

# Using unittest import pyaefi and create a class to test the AefiUUID class
import unittest

from pyaefi.aefi_uuid import AefiUUID

class TestAefiUUID(unittest.TestCase):

    # Create a function to test the generate_aefi_id function
    def test_generate_aefi_id(self):
        # Create an instance of AefiUUID
        aefi_uuid = AefiUUID('MX')
        # Create a variable to store the result of the generate_aefi_id function
        result = aefi_uuid.generate_aefi_id('test')
        # Create a variable to store the expected result
        expected_result = '0d6011ab-2712-5fdd-8349-d1a5f4870a81'
        # Assert if the result is equal to the expected result
        self.assertEqual(str(result), expected_result)

    # Create a function to test the generate_aefi_patient_id function
    def test_generate_aefi_patient_id(self):
        # Create an instance of AefiUUID
        aefi_uuid = AefiUUID('MX')
        # Create a variable to store the result of the generate_aefi_patient_id function
        result = aefi_uuid.generate_aefi_patient_id('test')
        # Create a variable to store the expected result
        expected_result = 'c1c4695f-d842-5702-b389-18f50941e032'
        # Assert if the result is equal to the expected result
        self.assertEqual(str(result), expected_result)

# Run the test
if __name__ == '__main__':
    unittest.main()
