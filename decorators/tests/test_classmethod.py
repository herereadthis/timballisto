"""Do Unit tests."""

import unittest
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from classmethod import MyClass as ClassmethodClass


class TestStringMethods(unittest.TestCase):
    """Test decorators."""

    def setUp(self):
        """Setup."""
        self.first_instance = ClassmethodClass()
        self.second_instance = ClassmethodClass()

    def tearDown(self):
        """Tear down."""

    def test_create_instance(self):
        """New objects are instances of class."""
        # new objects are instances of ClassmethodClass
        self.assertIsInstance(self.first_instance, ClassmethodClass)
        self.assertIsInstance(self.second_instance, ClassmethodClass)
        # new objects have fruit property that are the same
        self.assertEqual(self.first_instance.fruit, self.second_instance.fruit)
        # new objects have fruit property that are the same as class
        self.assertEqual(self.first_instance.fruit, ClassmethodClass.fruit)
        self.assertEqual(
            self.first_instance.vegetable, self.second_instance.vegetable
        )

    def test_instance_method(self):
        """Instance method only affects instance."""
        self.first_instance.foo('radish')
        self.assertEqual(self.first_instance.vegetable, 'radish')
        self.second_instance.foo('spinach')
        self.assertEqual(self.second_instance.vegetable, 'spinach')
        self.assertNotEqual(
            self.first_instance.vegetable, self.second_instance.vegetable
        )

    def test_class_method_from_instance(self):
        """Calling classmethod from instance affects all instances."""
        self.first_instance.class_foo('orange')
        self.assertEqual(self.first_instance.fruit, ClassmethodClass.fruit)
        self.assertEqual(self.second_instance.fruit, ClassmethodClass.fruit)

    def test_class_method_from_class(self):
        """Calling classmethod from class affects all instances."""
        ClassmethodClass.class_foo('pear')
        self.assertEqual(self.first_instance.fruit, ClassmethodClass.fruit)
        self.assertEqual(self.second_instance.fruit, ClassmethodClass.fruit)


if __name__ == '__main__':
    unittest.main()
