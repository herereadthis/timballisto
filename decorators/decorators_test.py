"""Do Unit tests."""

import unittest
from classmethod import MyClass as ClassmethodClass


class TestStringMethods(unittest.TestCase):
    """Test decorators."""

    def test_classmethod(self):
        """Test classmethod."""
        my_instance = ClassmethodClass()
        my_instance.foo('blueberry')
        self.assertEqual(my_instance.vegetable, 'blueberry')

        my_instance.class_foo('orange')
        self.assertEqual(my_instance.fruit, ClassmethodClass.fruit)

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
