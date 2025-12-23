import unittest
from my_windward_app.rotation import get_rotation_for_date


class testRotationLogic(unittest.TestCase):
    
    def test_first_day_of_school(self):
        """Test that Aug 25, 2025 is Day 1 (Monday)"""
        # Aug 25, 2025 is a Monday. Should be Day 1. 
        result = get_rotation_for_date(8, 25)
        self.assertEqual(result, 1, (1, 'mon'))

    def test_weekend(self):
        """Test that a Saturday returns None"""
        # Aug 30, 2025 is a Saturday. Should be None.
        result = get_rotation_for_date(8, 30)
        self.assertIsNone(result)

    def test_labor_day_holiday(self):
        """Test that Labor Day (Sept 1) returns None"""
        # Sept 1, 2025 is Labor Day (No School).
        result = get_rotation_for_date(9, 1)
        self.assertIsNone(result)

    def test_day_after_labor_day(self):
        """Test the schedule shift after a holiday"""
        # Sept 2, 2025 is Tuesday.
        # The schedule says: Week of Sept 1 is [No School, 6, 1, 2, 3]
        # So Tuesday (index 1) should be Day 6.
        result = get_rotation_for_date(9, 2)
        self.assertEqual(result, (6, 'tue'))

    if __name__ == '__main__':
        print("🦁 Running Windward App Logic Tests...")
        unittest.main()