#!/usr/bin/env python


class Box(object):
    """Box class.
    """

    class InvalidValueException(Exception):
        """
        """
        def __init__(self, ):
            """
            """
            pass

    def __init__(self, x=0, y=0, z=0, w=1, h=1, d=1):
        """Box Constructor.

        @param x x coordinate
        @param y y coordinate
        @param z z coordinate
        @param w width(x) > 0
        @param h height(y) > 0
        @param d depth(z) > 0
        """
        if not isinstance(x, int):
            raise Box.InvalidValueException()
        if not isinstance(y, int):
            raise Box.InvalidValueException()
        if not isinstance(z, int):
            raise Box.InvalidValueException()
        if not isinstance(w, int) or w <= 0:
            raise Box.InvalidValueException()
        if not isinstance(h, int) or h <= 0:
            raise Box.InvalidValueException()
        if not isinstance(d, int) or d <= 0:
            raise Box.InvalidValueException()
        self._x = x
        self._y = y
        self._z = z
        self._w = w
        self._h = h
        self._d = d

    def intersect(self, c):
        """Check intersection with the argument.

        @param c check target box object
        """
        if not Box.coord_intersect(self.x, self.w, c.x, c.w):
            return False
        if not Box.coord_intersect(self.y, self.h, c.y, c.h):
            return False
        if not Box.coord_intersect(self.z, self.d, c.z, c.d):
            return False
        return True

    @staticmethod
    def coord_intersect(c0, l0, c1, l1):
        """Check intersection of a coordinate.

        @param c0 coord-0
        @param l0 length-0
        @param c1 coord-1
        @param l1 length-1
        """
        if c0 < c1:
            if c0 + l0 > c1:
                return True
        else:
            if c1 + l1 > c0:
                return True
        return False

    def _set_x(self, value):
        if isinstance(value, int):
            self._x = value
        raise Box.InvalidValueException()

    def _get_x(self):
        return self._x

    def _set_y(self, value):
        if isinstance(value, int):
            self._y = value
        raise Box.InvalidValueException()

    def _get_y(self):
        return self._y

    def _set_z(self, value):
        if isinstance(value, int):
            self._z = value
        raise Box.InvalidValueException()

    def _get_z(self):
        return self._z

    def _set_w(self, value):
        if isinstance(value, int) and value > 0:
            self._w = value
        raise Box.InvalidValueException()

    def _get_w(self):
        return self._w

    def _set_h(self, value):
        if isinstance(value, int) and value > 0:
            self._h = value
        raise Box.InvalidValueException()

    def _get_h(self):
        return self._h

    def _set_d(self, value):
        if isinstance(value, int) and value > 0:
            self._d = value
        raise Box.InvalidValueException()

    def _get_d(self):
        return self._d

    x = property(_get_x, _set_x)
    y = property(_get_y, _set_y)
    z = property(_get_z, _set_z)
    w = property(_get_w, _set_w)
    h = property(_get_h, _set_h)
    d = property(_get_d, _set_d)
