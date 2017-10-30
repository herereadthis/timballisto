"""Do Unit tests."""

import unittest
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from property import MyClass as PropertyClass


class TestStringMethods(unittest.TestCase):
    """Test decorators."""

    def setUp(self):
        """Setup."""
        self.test_string = 'hello world'
        self.first_instance = PropertyClass(self.test_string)

    def tearDown(self):
        """Tear down."""

    def test_instance_method(self):
        """Instance method returns string from constructor."""
        self.assertEqual(self.first_instance.get_function(), self.test_string)
        self.assertNotEqual(self.first_instance.get_function, self.test_string)
        self.assertEqual(
            self.first_instance.get_function.__class__.__name__,
            'instancemethod'
        )

    def test_property_method(self):
        """Property attribute returns string from constructor."""
        self.assertEqual(self.first_instance.get_property, self.test_string)
        with self.assertRaises(TypeError):
            self.first_instance.get_property()
        self.assertEqual(
            self.first_instance.get_property.__class__.__name__, 'str')


if __name__ == '__main__':
    unittest.main()
