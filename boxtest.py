#!/usr/bin/env python


import unittest
import box
from box import Box


class BoxTestCase(unittest.TestCase):
    """Testcase for Box class.
    """

    def setUp(self):
        self.base_box = Box()
        pass

    def tearDown(self):
        pass

    def test_invalid_x(self, ):
        """Failure test of invalid constructor value of x.
        """
        self.assertRaises(Box.InvalidValueException, Box, x=1.0)
        self.assertRaises(Box.InvalidValueException, Box, x=0.1)
        self.assertTrue(Box(x=1))

    def test_invalid_y(self, ):
        """Failure test of invalid constructor value of y.
        """
        self.assertRaises(Box.InvalidValueException, Box, y=1.0)
        self.assertRaises(Box.InvalidValueException, Box, y=0.1)
        self.assertTrue(Box(y=1))

    def test_invalid_z(self, ):
        """Failure test of invalid constructor value of z.
        """
        self.assertRaises(Box.InvalidValueException, Box, z=1.0)
        self.assertRaises(Box.InvalidValueException, Box, z=0.1)
        self.assertTrue(Box(z=1))

    def test_invalid_w(self, ):
        """Failure test of invalid constructor value of w.
        """
        self.assertRaises(Box.InvalidValueException, Box, w=1.0)
        self.assertRaises(Box.InvalidValueException, Box, w=0.1)
        self.assertRaises(Box.InvalidValueException, Box, w=0)
        self.assertRaises(Box.InvalidValueException, Box, w=-1)
        self.assertTrue(Box(w=1))

    def test_invalid_h(self, ):
        """Failure test of invalid constructor value of w.
        """
        self.assertRaises(Box.InvalidValueException, Box, h=1.0)
        self.assertRaises(Box.InvalidValueException, Box, h=0.1)
        self.assertRaises(Box.InvalidValueException, Box, h=0)
        self.assertRaises(Box.InvalidValueException, Box, h=-1)
        self.assertTrue(Box(h=1))

    def test_invalid_d(self, ):
        """Failure test of invalid constructor value of w.
        """
        self.assertRaises(Box.InvalidValueException, Box, d=1.0)
        self.assertRaises(Box.InvalidValueException, Box, d=0.1)
        self.assertRaises(Box.InvalidValueException, Box, d=0)
        self.assertRaises(Box.InvalidValueException, Box, d=-1)
        self.assertTrue(Box(d=1))

    def test_inclusive_no_touch(self, ):
        """
        """
        c_inner = Box(x=0, y=0, z=0, w=1, h=2, d=3)
        c_outer = Box(x=-1, y=-1, z=-1, w=3, h=4, d=5)
        self.assertTrue(c_inner.intersect(c_outer))
        self.assertTrue(c_outer.intersect(c_inner))

    def test_inclusive_touch_low(self, ):
        """
        """
        c_outer1 = Box(x=0, y=0, z=0, w=2, h=2, d=2)
        self.assertTrue(self.base_box.intersect(c_outer1))
        self.assertTrue(c_outer1.intersect(self.base_box))

    def test_inclusive_touch_high(self, ):
        """
        """
        c_outer1 = Box(x=-1, y=-1, z=-1, w=2, h=2, d=2)
        self.assertTrue(self.base_box.intersect(c_outer1))
        self.assertTrue(c_outer1.intersect(self.base_box))

    def test_exclusive(self, ):
        """
        """
        c_outer1 = Box(x=-2, y=-2, z=-2, w=1, h=1, d=1)
        self.assertFalse(self.base_box.intersect(c_outer1))
        self.assertFalse(c_outer1.intersect(self.base_box))
        c_outer2 = Box(x=2, y=2, z=2, w=1, h=1, d=1)
        self.assertFalse(self.base_box.intersect(c_outer2))
        self.assertFalse(c_outer2.intersect(self.base_box))
        c_outer3 = Box(x=0, y=0, z=2, w=1, h=1, d=1)
        self.assertFalse(self.base_box.intersect(c_outer2))
        self.assertFalse(c_outer2.intersect(self.base_box))
        c_outer4 = Box(x=0, y=0, z=-2, w=1, h=1, d=1)
        self.assertFalse(self.base_box.intersect(c_outer2))
        self.assertFalse(c_outer2.intersect(self.base_box))

    def test_coord_intersect(self, ):
        """test case for coord_intersect().
        """
        self.assertFalse(Box.coord_intersect(0, 2, -1, 1))
        self.assertFalse(Box.coord_intersect(0, 2, -2, 1))
        self.assertFalse(Box.coord_intersect(0, 2, 2, 2))
        self.assertFalse(Box.coord_intersect(0, 2, 3, 2))

        self.assertTrue(Box.coord_intersect(0, 2, -1, 2))
        self.assertTrue(Box.coord_intersect(0, 2, 0, 1))
        self.assertTrue(Box.coord_intersect(0, 2, 1, 2))
        self.assertTrue(Box.coord_intersect(0, 2, 1, 1))

    def test_intersect(self, ):
        """
        """
        c0 = Box(x=0, y=0, z=0, w=2, h=2, d=2)
        # Targets
        c1 = Box(x=-1, y=-1, z=-1, w=2, h=2, d=2)
        self.assertTrue(c0.intersect(c1))
        self.assertTrue(c1.intersect(c0))
        c2 = Box(x=-1, y=-1, z=0, w=2, h=2, d=2)
        self.assertTrue(c0.intersect(c2))
        self.assertTrue(c2.intersect(c0))
        c3 = Box(x=-1, y=-1, z=1, w=2, h=2, d=2)
        self.assertTrue(c0.intersect(c3))
        self.assertTrue(c3.intersect(c0))
        c4 = Box(x=-1, y=0, z=-1, w=2, h=2, d=2)
        self.assertTrue(c0.intersect(c4))
        self.assertTrue(c4.intersect(c0))
        c5 = Box(x=-1, y=0, z=0, w=2, h=2, d=2)
        self.assertTrue(c0.intersect(c5))
        self.assertTrue(c5.intersect(c0))
        c6 = Box(x=-1, y=0, z=1, w=2, h=2, d=2)
        self.assertTrue(c0.intersect(c6))
        self.assertTrue(c6.intersect(c0))
        c7 = Box(x=-1, y=1, z=-1, w=2, h=2, d=2)
        self.assertTrue(c0.intersect(c7))
        self.assertTrue(c7.intersect(c0))
        c8 = Box(x=-1, y=1, z=0, w=2, h=2, d=2)
        self.assertTrue(c0.intersect(c8))
        self.assertTrue(c8.intersect(c0))
        c9 = Box(x=-1, y=1, z=1, w=2, h=2, d=2)
        self.assertTrue(c0.intersect(c9))
        self.assertTrue(c9.intersect(c0))
        c10 = Box(x=0, y=-1, z=-1, w=2, h=2, d=2)
        self.assertTrue(c0.intersect(c10))
        self.assertTrue(c10.intersect(c0))
        c11 = Box(x=0, y=-1, z=0, w=2, h=2, d=2)
        self.assertTrue(c0.intersect(c11))
        self.assertTrue(c11.intersect(c0))
        c12 = Box(x=0, y=-1, z=1, w=2, h=2, d=2)
        self.assertTrue(c0.intersect(c12))
        self.assertTrue(c12.intersect(c0))
        c13 = Box(x=0, y=0, z=-1, w=2, h=2, d=2)
        self.assertTrue(c0.intersect(c13))
        self.assertTrue(c13.intersect(c0))
        c14 = Box(x=0, y=0, z=0, w=2, h=2, d=2)
        self.assertTrue(c0.intersect(c14))
        self.assertTrue(c14.intersect(c0))
        c15 = Box(x=0, y=0, z=1, w=2, h=2, d=2)
        self.assertTrue(c0.intersect(c15))
        self.assertTrue(c15.intersect(c0))
        c16 = Box(x=0, y=1, z=-1, w=2, h=2, d=2)
        self.assertTrue(c0.intersect(c16))
        self.assertTrue(c16.intersect(c0))
        c17 = Box(x=0, y=1, z=0, w=2, h=2, d=2)
        self.assertTrue(c0.intersect(c17))
        self.assertTrue(c17.intersect(c0))
        c18 = Box(x=0, y=1, z=1, w=2, h=2, d=2)
        self.assertTrue(c0.intersect(c18))
        self.assertTrue(c18.intersect(c0))
        c19 = Box(x=1, y=-1, z=-1, w=2, h=2, d=2)
        self.assertTrue(c0.intersect(c19))
        self.assertTrue(c19.intersect(c0))
        c20 = Box(x=1, y=-1, z=0, w=2, h=2, d=2)
        self.assertTrue(c0.intersect(c20))
        self.assertTrue(c20.intersect(c0))
        c21 = Box(x=1, y=-1, z=1, w=2, h=2, d=2)
        self.assertTrue(c0.intersect(c21))
        self.assertTrue(c21.intersect(c0))
        c22 = Box(x=1, y=0, z=-1, w=2, h=2, d=2)
        self.assertTrue(c0.intersect(c22))
        self.assertTrue(c22.intersect(c0))
        c23 = Box(x=1, y=0, z=0, w=2, h=2, d=2)
        self.assertTrue(c0.intersect(c23))
        self.assertTrue(c23.intersect(c0))
        c24 = Box(x=1, y=0, z=1, w=2, h=2, d=2)
        self.assertTrue(c0.intersect(c24))
        self.assertTrue(c24.intersect(c0))
        c25 = Box(x=1, y=1, z=-1, w=2, h=2, d=2)
        self.assertTrue(c0.intersect(c25))
        self.assertTrue(c25.intersect(c0))
        c26 = Box(x=1, y=1, z=0, w=2, h=2, d=2)
        self.assertTrue(c0.intersect(c26))
        self.assertTrue(c26.intersect(c0))
        c27 = Box(x=1, y=1, z=1, w=2, h=2, d=2)
        self.assertTrue(c0.intersect(c27))
        self.assertTrue(c27.intersect(c0))

if __name__ == '__main__':
    unittest.main()
