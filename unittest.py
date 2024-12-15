import unittest
from controller import TaxController, TaxProfileDatabase

class TestTaxProfileDatabase(unittest.TestCase):
    
    def setUp(self):
        """Set up the database and profiles for each test"""
        self.db = TaxProfileDatabase()
        self.tax1 = TaxController(name="John Doe", income=50000, deductions=10000)
        self.tax2 = TaxController(name="Jane Doe", income=60000, deductions=15000)
    
    def test_add_profile(self):
        """Test adding a profile to the database"""
        self.db.add_profile(self.tax1)
        self.assertEqual(len(self.db.profiles), 1)
        self.assertEqual(self.db.get_profile("John Doe"), self.tax1)

    def test_get_profile(self):
        """Test getting a profile by name"""
        self.db.add_profile(self.tax1)
        profile = self.db.get_profile("John Doe")
        self.assertEqual(profile, self.tax1)
        self.assertIsNone(self.db.get_profile("Nonexistent"))
    
    def test_get_all_profiles(self):
        """Test getting all profiles"""
        self.db.add_profile(self.tax1)
        self.db.add_profile(self.tax2)
        profiles = self.db.get_all_profiles()
        self.assertEqual(len(profiles), 2)
        self.assertIn(self.tax1, profiles)
        self.assertIn(self.tax2, profiles)
    
    def test_check_profiles_name(self):
        """Test checking if a profile exists by name"""
        self.db.add_profile(self.tax1)
        self.assertTrue(self.db.check_profiles_name("John Doe"))
        self.assertFalse(self.db.check_profiles_name("Nonexistent"))
    
    def test_update_profile_name(self):
        """Test updating the profile name"""
        self.db.add_profile(self.tax1)
        self.assertTrue(self.db.update_profile_name("John Doe", "John Smith"))
        self.assertEqual(self.db.get_profile("John Smith"), self.tax1)
        self.assertFalse(self.db.update_profile_name("John Smith", "Jane Doe"))
    
    def test_update_profile_income(self):
        """Test updating the income of a profile"""
        self.db.add_profile(self.tax1)
        self.db.update_profile_income("John Doe", 55000)
        self.assertEqual(self.tax1._income, 55000)
    
    def test_update_profile_deductions(self):
        """Test updating the deductions of a profile"""
        self.db.add_profile(self.tax1)
        self.db.update_profile_deductions("John Doe", 12000)
        self.assertEqual(self.tax1._deductions, 12000)
    
    def test_update_profile_name_to_existing(self):
        """Test updating the profile name to an existing name"""
        self.db.add_profile(self.tax1)
        self.db.add_profile(self.tax2)
        # Trying to rename to an existing profile name
        result = self.db.update_profile_name("John Doe", "Jane Doe")
        self.assertFalse(result)
        self.assertEqual(self.db.get_profile("John Doe"), self.tax1)
        self.assertEqual(self.db.get_profile("Jane Doe"), self.tax2)

if __name__ == '__main__':
    unittest.main()
