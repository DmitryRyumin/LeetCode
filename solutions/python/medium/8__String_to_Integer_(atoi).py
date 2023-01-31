#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
8. String to Integer (atoi)
"""

# ######################################################################################################################
# Solution
# ######################################################################################################################

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()

        if not s: return 0

        sign = -1 if s[0] == '-' else 1
        if s[0] in ['-', '+']: s = s[1:]

        res = 0

        for char in s:
            if char.isdigit(): res = res * 10 + int(char)
            else: break

        res *= sign

        if res < -2 ** 31: return -2 ** 31
        if res > 2 ** 31 - 1: return 2 ** 31 - 1

        return res
