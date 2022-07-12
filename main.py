# Problem 56:
#     Powerful Digit Sum
#
# Description:
#     A googol (10^100) is a massive number: one followed by one-hundred zeros;
#     100^100 is almost unimaginably large: one followed by two-hundred zeros.
#     Despite their size, the sum of the digits in each number is only 1.
#
#     Considering natural numbers of the form, a^b, where a, b < 100,
#       what is the maximum digital sum?

from typing import Tuple


def digital_sum(x: int) -> int:
    """
    Returns the 'digital sum' of `x`.

    Args:
        x (int): Natural number

    Returns:
        (int): Digital sum of `x`

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(x) == int and x > 0
    return sum(map(int, list(str(x))))


def main(n: int) -> Tuple[int, int, int, int]:
    """
    Returns a, b, c, d, where a, b < n, and the digital sum `d` of c = a^b is the maximum of those a and b.

    Args:
        n (int): Natural number greater than 1

    Returns:
        (Tuple[int, int, int, int]):
            Tuple of a, b, c, d, where a^b = c, and d is the digital sum of c
              such that d is the maximum possible digital sum.

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(n) == int and n > 1

    # Skip a = 1, which will always have digital sum of 1
    a_max = b_max = c_max = d_max = 1

    # Loop through all possible combinations of a and b,
    #   and check for best digital sum
    # Python is fine with big integers
    for a in range(2, n):
        for b in range(1, n):
            c = a ** b
            d = digital_sum(c)
            if d > d_max:
                a_max, b_max, c_max, d_max = a, b, c, d

    return a_max, b_max, c_max, d_max


if __name__ == '__main__':
    num = int(input('Enter a natural number (greater than 1): '))
    a_best, b_best, c_best, d_best = main(num)
    print('Maximum digital sum of a^b, where a, b < {}:'.format(num))
    print('  {} ^ {} = {}'.format(a_best, b_best, c_best))
    print('  Digital sum = {}'.format(d_best))
