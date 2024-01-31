import pytest

from my_library import is_palindrome


@pytest.mark.parametrize(
    "s,exp",
    [
        ("", True),
        ("a", True),
        ("aa", True),
        ("ab", False),
        ("aba", True),
        ("abc", False),
        ("radar", True),
        ("redder", True),
        ("renter", False),
        ("banana", False),
        ("bananab", True),
        ("Racecar", True),
        ("racecar", True),
        ("hello", False),
        ("12321", True),
        ("AManAPlanACanalPanama", True),
        ("WasItACarOrACatISaw", True),
        ("a" * 10 + "b" + "a" * 10, True),
    ],
)
def test_is_palindrome(s: str, exp: bool) -> None:
    assert is_palindrome(s) == exp
