import unittest
from unittest.mock import patch
from model.model import TaxProfileDatabase, TaxController

class TestTaxProfileDatabase(unittest.TestCase):
    
    def setUp(self):
        self.model = TaxProfileDatabase()
    
    def test_add_profile_success(self):
        profile = TaxController("users01", 1000000, 0)
        result = self.model.add_profile(profile)
        self.assertTrue(result)
        self.assertIn("users01", self.model.get_all_profiles())

if __name__ == "__main__":
    unittest.main()
