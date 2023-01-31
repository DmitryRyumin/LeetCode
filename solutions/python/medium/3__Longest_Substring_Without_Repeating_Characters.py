#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
3. Longest Substring Without Repeating Characters
"""

# ######################################################################################################################
# Solution
# ######################################################################################################################

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        max_len, start = 0, 0

        for i, char in enumerate(s):
            while char in char_set:
                char_set.remove(s[start])
                start += 1
            char_set.add(char)
            max_len = max(max_len, i - start + 1)

        return max_len
