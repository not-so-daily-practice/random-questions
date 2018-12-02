import math


def is_prime(n):
    """
    Check if a number is prime
    :param n: number to check
    :return: bool, True if prime, False otherwise
    #time complexity of O(sqrt(n))
    """
    if type(n) is not int:
        raise TypeError("Must be an integer")

    if n < 2:
        raise Exception("Numbers less than 2 cannot be prime")

    if n == 2 or n == 3:
        # base cases
        return True

    # for all n, all divisors are <= n / 2
    # reaching sqrt(n), divisors flip and repeat, so only test until sqrt(n)

    # all integers can be expressed as 6k + i for some integer k, and i = -1, 0, 1, 2, 3, 4
    # primes are of form 6k +/- 1 (excepting 2, 3)

    if n % 2 == 0:
        # 2 divides 6k + 0, 6k + 2, 6k + 4
        # even, false
        return False

    if n % 3 == 0:
        # 3 divides 6k + 3
        return False

    # n not divisible by 2 or 3
    # check if divisible by a lower prime form 6k +/- 1 that are <= sqrt(n)
    i = 5
    w = 2
    sqrt_n = int(n ** 0.5) + 1
    while i <= sqrt_n:
        if n % i == 0:
            return False

        # add 4 (to go from 6n + 1 to 6n + 5)
        # or add 2 (to go from 6n + 5 to 6n + 7 = 6n + 6 + 1 = 6(n + 1) + 1)
        i += w
        w = 6 - w  # switch between adding 2 or 4

    return True


def is_prime_range(start, end):
    """
    Check a range of numbers for primality
    :param start: int, start of range
    :param end: int, end of range
    :return: list of bool, True if prime, False otherwise
    """
    if type(start) is not int:
        raise TypeError("Start be an integer")

    if type(end) is not int:
        raise TypeError("End be an integer")

    is_prime_list = [is_prime(n) for n in range(start, end)]

    return is_prime_list


start = 3000
end = 4001

print(list(zip(range(start, end), is_prime_range(start, end))))
