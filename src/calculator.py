"""シンプルな計算モジュール - CI/CD検証用."""


def add(a: float, b: float) -> float:
    """2つの数値を加算する."""
    return a + b


def subtract(a: float, b: float) -> float:
    """2つの数値を減算する."""
    return a - b


def multiply(a: float, b: float) -> float:
    """2つの数値を乗算する."""
    return a * b


def divide(a: float, b: float) -> float:
    """2つの数値を除算する.

    Raises:
        ZeroDivisionError: bが0の場合
    """
    if b == 0:
        raise ZeroDivisionError("0で割ることはできません")
    return a / b

def no_mean(a: float, b: float) -> float:
    """2つの数値を除算する.

    Raises:
        ZeroDivisionError: bが0の場合
    """
    return a
