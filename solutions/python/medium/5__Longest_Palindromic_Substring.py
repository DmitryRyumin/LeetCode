#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
5. Longest Palindromic Substring
"""

# ######################################################################################################################
# Solution
# ######################################################################################################################

class Solution:
    def longestPalindromicSubstring(self, s: str) -> str:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        ans = ''

        for i in range(n):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j <= 2 or dp[j + 1][i - 1]):
                    dp[j][i] = 1
                    if i - j + 1 > len(ans):
                        ans = s[j:i + 1]

        return ans
