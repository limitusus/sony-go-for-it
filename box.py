#!/usr/bin/env python


class Box(object):
    """Box class.
    """

    def __init__(self, x=None, y=None, z=None, w=None, h=None, d=None):
        """Box Constructor.

        @param x x coordinate
        @param y y coordinate
        @param z z coordinate
        @param w width(x) > 0
        @param h height(y) > 0
        @param d depth(z) > 0
        """
        self._x = x
        self._y = y
        self._z = z
        self._w = w
        self._h = h
        self._d = d

    def _set_x(self, value):
        if isinstance(value, int):
            self._x = value
        raise

    def _get_x(self):
        return self._x

    def _set_y(self, value):
        if isinstance(value, int):
            self._y = value
        self._y = value

    def _get_y(self):
        return self._y

    def _set_z(self, value):
        if isinstance(value, int):
            self._z = value
        self._z = value

    def _get_z(self):
        return self._z

    def _set_w(self, value):
        if isinstance(value, int) and value > 0:
            self._w = value
        self._w = value

    def _get_w(self):
        return self._w

    def _set_h(self, value):
        if isinstance(value, int) and value > 0:
            self._h = value
        self._h = value

    def _get_h(self):
        return self._h

    def _set_d(self, value):
        if isinstance(value, int) and value > 0:
            self._d = value
        self._d = value

    def _get_d(self):
        return self._d

    x = property(_get_x, _set_x)
    y = property(_get_y, _set_y)
    z = property(_get_z, _set_z)
    w = property(_get_w, _set_w)
    h = property(_get_h, _set_h)
    d = property(_get_d, _set_d)
