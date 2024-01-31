def is_palindrome(input_string: str) -> bool:
    input_string = input_string.lower()
    return input_string == input_string[::-1]


def fibonacci(n: int, memo: dict = {}) -> int:
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]
