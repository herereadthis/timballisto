"""Do Unit tests."""

import unittest
from classmethod import MyClass as ClassmethodClass


class TestStringMethods(unittest.TestCase):
    """Test decorators."""

    def setUp(self):
        """Setup."""
        self.class_instance = ClassmethodClass()

    def tearDown(self):
        """Tear down."""

    def test_classmethod(self):
        """Test classmethod."""
        self.class_instance.foo('radish')
        self.assertEqual(self.class_instance.vegetable, 'radish')

        self.class_instance.class_foo('orange')
        self.assertEqual(self.class_instance.fruit, ClassmethodClass.fruit)

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
