import pytest


class Tests:

    def test_set_equality(self):
        s1 = {'a', 'b', 'c'}
        s2 = {'c', 'b', 'a'}
        assert s1 == s2

    @pytest.mark.parametrize("a, b, expected", [(0, 5, 0), (1, 5, 5), (2, 5, 10), (-3, 5, -15)])
    def test_set_parametrized(self, a, b, expected):
        assert a * b == expected

    def test_set_negative(self):
        s1 = {'a', 'b', 'c'}
        s2 = {'a', 'b'}
        try:
            assert s1 == s2
        except AssertionError:
            pass

    def test_int_transformation(self):
        assert int(3.14e-10) == 0

    @pytest.mark.parametrize("actual, expected", [(-37, 6), (9, 4), (-123, 7)])
    def test_int_bit_length(self, actual, expected):
        assert actual.bit_length() == expected

    def test_int_negative(self):
        a = 3
        b = "two"
        try:
            a + b
        except TypeError:
            pass
