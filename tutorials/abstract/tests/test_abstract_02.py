"""Do Unit tests."""

import unittest
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from abstract_02 import MyABC


class TestAbstractBaseClass(unittest.TestCase):
    """Test abstract base classes."""

    def setUp(self):
        """Setup."""
        self.my_instance = MyABC()
        MyABC

    def tearDown(self):
        """Tear down."""

    def test_register(self):
        """Try register method."""
        MyABC.register(dict)
        print(issubclass(dict, MyABC))
        self.assertTrue(issubclass(dict, MyABC))
        self.assertIsInstance({}, MyABC)
