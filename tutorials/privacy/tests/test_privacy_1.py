"""Do Unit tests."""

import unittest
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from privacy_1 import PrivacyClass


class TestPrivacyClass(unittest.TestCase):
    """Test decorators."""

    def setUp(self):
        """Setup."""
        self.public_string = 'hello world'
        self.protected_string = 'lorem ipsum'
        self.private_string = 'reindeer games'
        self.test_instance = PrivacyClass(
            self.private_string, self.protected_string, self.public_string
        )

    def tearDown(self):
        """Tear down."""

    def test_instance_public(self):
        """Instance returns public attributes."""
        self.assertTrue(hasattr(self.test_instance, 'public_attribute'))
        self.assertEqual(
            self.test_instance.public_attribute, self.public_string)

    def test_public_mutability(self):
        """Public attributes are mutable."""
        new_str = 'Friday Friday Friday'
        self.test_instance.public_attribute = new_str
        self.assertEqual(self.test_instance.public_attribute, new_str)

    def test_instance_protected(self):
        """Instance returns protected attributes."""
        self.assertTrue(hasattr(self.test_instance, '_protected_attribute'))
        self.assertEqual(
            self.test_instance._protected_attribute, self.protected_string)

    def test_pprotected_mutability(self):
        """Protected attributes are mutable."""
        new_str = 'Friday Friday Friday'
        self.test_instance._protected_attribute = new_str
        self.assertEqual(self.test_instance._protected_attribute, new_str)

    def test_instance_private(self):
        """Instance does not return private attributes."""
        with self.assertRaises(AttributeError):
            self.assertEqual(
                self.test_instance.__private_attribute, self.private_string)


if __name__ == '__main__':
    unittest.main()
