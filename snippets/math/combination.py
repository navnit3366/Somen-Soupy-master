# -*- coding: utf-8 -*-

'''Snippets for combination.
'''

# Usage:
# combination = Combination(max_value=10 ** 5 + 100)
# combination.count_nCr(n, r)
# combination.count_nHr(n, r)


class Combination:
    ''' Count the total number of combinations.
        nCr % mod.
        nHr % mod = (n + r - 1)Cr % mod.

        Args:
            max_value: Max size of list. The default is 500,050
            mod      : Modulo. The default is 10 ** 9 + 7.

        Landau notation: O(n)

        See:
        http://drken1215.hatenablog.com/entry/2018/06/08/210000
    '''

    def __init__(self, max_value=500050, mod=10 ** 9 + 7):
        self.max_value = max_value
        self.mod = mod
        self.fac = [0 for _ in range(self.max_value)]
        self.finv = [0 for _ in range(self.max_value)]
        self.inv = [0 for _ in range(self.max_value)]

        self.fac[0] = 1
        self.fac[1] = 1
        self.finv[0] = 1
        self.finv[1] = 1
        self.inv[1] = 1

        for i in range(2, self.max_value):
            self.fac[i] = self.fac[i - 1] * i % self.mod
            self.inv[i] = self.mod - self.inv[self.mod % i] * (self.mod // i) % self.mod
            self.finv[i] = self.finv[i - 1] * self.inv[i] % self.mod

    def count_nCr(self, n, r):
        '''Count the total number of combinations.
            nCr % mod.
            nHr % mod = (n + r - 1)Cr % mod.

        Args:
            n   : Elements. Int of number (greater than 1).
            r   : The number of r-th combinations. Int of number
                  (greater than 0).

        Returns:
            The total number of combinations.

        Landau notation: O(1)
        '''

        if n < r:
            return 0
        if n < 0 or r < 0:
            return 0

        return self.fac[n] * (self.finv[r] * self.finv[n - r] % self.mod) % self.mod

    def count_nHr(self, n, r):
        return self.count_nCr(n + r - 1, r)


def nCr(n: int, r: int, mod=10 ** 9 + 7):
    '''Count the total number of combinations.
        nCr % mod.
        nHr % mod = (n + r - 1)Cr % mod.

    Args:
        n   : Elements. Int of number (greater than 1).
        r   : The number of r-th combinations. Int of number
                (greater than 0).

    Returns:
        The total number of combinations.

    Landau notation: O(n)
    '''    

    if n < r:
        return 0
    if n < 0 or r < 0:
        return 0

    result = 1

    for i in range(n, n - r, - 1):
        result *= i
        result %= mod

    for i in range(1, r + 1):
        result *= pow(i, mod - 2, mod)
        result %= mod

    return result
