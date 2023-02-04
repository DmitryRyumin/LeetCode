#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
17 Letter Combinations of a Phone Number
"""

# ######################################################################################################################
# Required import
# ######################################################################################################################

from typing import List

# ######################################################################################################################
# Solution
# ######################################################################################################################

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        result = ['']

        for digit in digits:
            new_result = []
            for res in result:
                for char in mapping[digit]: new_result.append(res + char)
            result = new_result

        return result
