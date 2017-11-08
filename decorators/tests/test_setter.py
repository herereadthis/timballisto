"""Do Unit tests."""

import unittest
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from setter import SetterDecoratorClass


class TestSetter(unittest.TestCase):
    """Test decorators."""

    def setUp(self):
        """Setup."""
        self.initial_value = 42
        self.my_instance = SetterDecoratorClass(self.initial_value)

    def tearDown(self):
        """Tear down."""

    def test_get_set_initial_condition(self):
        """Test getter and setter if value under 1000."""
        self.assertEqual(self.my_instance.x, self.initial_value)
        new_value = 73
        self.my_instance.x = new_value
        self.assertEqual(self.my_instance.x, new_value)

    def test_get_set_excess_condition(self):
        """Test getter and setter if value over 1000."""
        self.assertEqual(self.my_instance.x, self.initial_value)
        new_value = 1001
        self.my_instance.x = new_value
        self.assertNotEqual(self.my_instance.x, new_value)


if __name__ == '__main__':
    unittest.main()
