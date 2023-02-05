#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
20. Longest Common Prefix
"""

# ######################################################################################################################
# Solution
# ######################################################################################################################

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                if not stack or stack.pop() != mapping[char]: return False
            else: stack.append(char)

        return not stack