"""calculatorモジュールのユニットテスト."""

import pytest

from src.calculator import add, divide, multiply, no_mean, subtract


class TestAdd:
    """加算のテスト."""

    def test_positive_numbers(self):
        assert add(2, 3) == 5

    def test_negative_numbers(self):
        assert add(-1, -1) == -2

    def test_zero(self):
        assert add(0, 0) == 0

    def test_float(self):
        assert add(1.5, 2.5) == 4.0


class TestSubtract:
    """減算のテスト."""

    def test_positive_numbers(self):
        assert subtract(5, 3) == 2

    def test_result_negative(self):
        assert subtract(3, 5) == -2


class TestMultiply:
    """乗算のテスト."""

    def test_positive_numbers(self):
        assert multiply(3, 4) == 12

    def test_by_zero(self):
        assert multiply(5, 0) == 0


class TestDivide:
    """除算のテスト."""

    def test_positive_numbers(self):
        assert divide(10, 2) == 5.0

    def test_float_result(self):
        assert divide(7, 2) == 3.5

    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError, match="0で割ることはできません"):
            divide(1, 0)


class TestNoMean:
    """意味のないテスト."""

    def test_no_mean(self):
        assert no_mean(1, 2) == 1
