#!/usr/bin/env python


import unittest
import box
from box import Box


class BoxTestCase(unittest.TestCase):
    """Testcase for Box class.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_invalid_x(self, ):
        """Failure test of invalid constructor value of x.
        """
        self.assertRaises(Box.InvalidValueException, Box, x=1.0)
        self.assertRaises(Box.InvalidValueException, Box, x=0.1)
        Box(x=1)

    def test_invalid_y(self, ):
        """Failure test of invalid constructor value of y.
        """
        self.assertRaises(Box.InvalidValueException, Box, y=1.0)
        self.assertRaises(Box.InvalidValueException, Box, y=0.1)
        Box(y=1)

    def test_invalid_z(self, ):
        """Failure test of invalid constructor value of z.
        """
        self.assertRaises(Box.InvalidValueException, Box, z=1.0)
        self.assertRaises(Box.InvalidValueException, Box, z=0.1)
        Box(z=1)

    def test_invalid_w(self, ):
        """Failure test of invalid constructor value of w.
        """
        self.assertRaises(Box.InvalidValueException, Box, w=1.0)
        self.assertRaises(Box.InvalidValueException, Box, w=0.1)
        self.assertRaises(Box.InvalidValueException, Box, w=0)
        self.assertRaises(Box.InvalidValueException, Box, w=-1)
        Box(w=1)

    def test_invalid_h(self, ):
        """Failure test of invalid constructor value of w.
        """
        self.assertRaises(Box.InvalidValueException, Box, h=1.0)
        self.assertRaises(Box.InvalidValueException, Box, h=0.1)
        self.assertRaises(Box.InvalidValueException, Box, h=0)
        self.assertRaises(Box.InvalidValueException, Box, h=-1)
        Box(h=1)

    def test_invalid_d(self, ):
        """Failure test of invalid constructor value of w.
        """
        self.assertRaises(Box.InvalidValueException, Box, d=1.0)
        self.assertRaises(Box.InvalidValueException, Box, d=0.1)
        self.assertRaises(Box.InvalidValueException, Box, d=0)
        self.assertRaises(Box.InvalidValueException, Box, d=-1)
        Box(d=1)

    @unittest.skip("Test for non-implemented method")
    def test_inclusive_no_touch(self, ):
        """
        """
        c_inner = Box(x=0, y=0, z=0, w=1, h=2, d=3)
        c_outer = Box(x=-1, y=-1, z=-1, w=3, h=4, d=5)
        self.assertEqual(c_inner.intersect(c_outer), True)
        self.assertEqual(c_outer.intersect(c_inner), True)

"""
    def test_default_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')
"""


if __name__ == '__main__':
    unittest.main()
