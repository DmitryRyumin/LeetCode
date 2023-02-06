#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
22 Generate Parentheses
"""

# ######################################################################################################################
# Required import
# ######################################################################################################################

from typing import List

# ######################################################################################################################
# Solution
# ######################################################################################################################

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(result, current, left, right, max_):
            if len(current) == 2 * max_:
                result.append(current)
                return
            if left < max_:
                backtrack(result, current + '(', left + 1, right, max_)
            if right < left:
                backtrack(result, current + ')', left, right + 1, max_)

        result = []
        backtrack(result, '', 0, 0, n)

        return result
