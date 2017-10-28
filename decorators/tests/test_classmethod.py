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
        """Test classmethod."""
        self.assertIsInstance(self.first_instance, ClassmethodClass)
        self.assertIsInstance(self.second_instance, ClassmethodClass)

    def test_instance_method(self):
        """Test classmethod."""
        self.first_instance.foo('radish')
        self.assertEqual(self.first_instance.vegetable, 'radish')
        self.second_instance.foo('spinach')
        self.assertEqual(self.second_instance.vegetable, 'spinach')

    def test_class_method_from_instance(self):
        """Test classmethod."""
        self.first_instance.class_foo('orange')
        self.assertEqual(self.first_instance.fruit, ClassmethodClass.fruit)
        self.assertEqual(self.second_instance.fruit, ClassmethodClass.fruit)

    def test_class_method_from_class(self):
        """Test classmethod."""
        ClassmethodClass.class_foo('pear')
        self.assertEqual(self.first_instance.fruit, ClassmethodClass.fruit)
        self.assertEqual(self.second_instance.fruit, ClassmethodClass.fruit)

    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)


if __name__ == '__main__':
    unittest.main()
