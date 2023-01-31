#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
7. Reverse Integer
"""

# ######################################################################################################################
# Solution
# ######################################################################################################################

class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sign = 1 if x >= 0 else -1
        x *= sign

        while x > 0:
            res = res * 10 + x % 10
            x //= 10

        res *= sign

        if res > 2 ** 31 - 1 or res < -2 ** 31:
            return 0

        return res
