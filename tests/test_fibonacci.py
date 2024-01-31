import pytest

from my_library import fibonacci


@pytest.mark.parametrize(
    "n,exp",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (10, 55),
        (20, 6765),
        (30, 832040),
        (40, 102334155),
        (50, 12586269025),
        (60, 1548008755920),
        (70, 190392490709135),
        (80, 23416728348467685),
        (90, 2880067194370816120),
        (100, 354224848179261915075),
    ],
)
def test_fibonacci(n: int, exp: int) -> None:
    assert fibonacci(n) == exp
