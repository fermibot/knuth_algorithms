from typing import List


def vol_01_chapter_01_algorithm_e(m: int, n: int, print_q: bool = False) -> int:
    """Algorithm E: Euler's method of finding GCD"""
    while m % n > 0:
        m, n = n, m % n
        if print_q:
            print(m, n, m % n)
    return n


def vol_01_exercise_01_01_001(a, b, c, d):
    """exchanging 4 variables"""
    r, b, c, d = b, c, d, a
    a = r
    return a, b, c, d


def vol_01_exercise_01_01_002(m: int, n: int) -> int:
    """Algorithm F, a modified version of algorithm E"""
    # TODO: Revisit this one
    return 0


def vol_01_exercise_01_01_006_pre(n: int, m: int) -> int:
    r = 0
    while m % n > 0:
        r += 1
        m, n = n, m % n
    return r


def vol_01_exercise_01_01_006(r_in: int = 100) -> List[int]:
    count_list = []
    for r in range(1, r_in + 1):
        count_list.append(vol_01_exercise_01_01_006_pre(r, 5))
    return count_list


def vol_01_chapter_01_page_0015(m: int, n: int):
    a = b1 = 0
    a1 = b = 1
    c = m
    d = n
    r = c % d
    while r != 0:
        q = c // d
        r = c % d
        c, d = d, r
        t, a1 = a1, a
        a = t - q * a
        t, b1 = b1, b
        b = t - q * b
    return a * m + b + n


def vol_01_exercise_01_01_008(r: int):
    for n in range(1, r):
        n_sum, n3_sum = 0, 0
        for i in range(n):
            n_sum += i
            n3_sum += i ** 3
        n2_sum = n_sum ** 2
        print(n3_sum, n2_sum, n3_sum == n2_sum)


def vol_01_exercise_01_01_011(r: int):
    for n in range(1, r + 1):
        print(n)
        sum_x = 0
        for i in range(n + 1):
            print(i)
            sum_x += ((-1) ** i)((2 * i + 1) ** 3) / ((2 * i + 1) ** 4 + 4)
        print(sum_x)


if __name__ == '__main__':
    vol_01_exercise_01_01_011(10)
