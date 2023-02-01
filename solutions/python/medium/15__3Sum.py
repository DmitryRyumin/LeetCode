#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
15. 3Sum
"""

# ######################################################################################################################
# Required import
# ######################################################################################################################

from typing import List

# ######################################################################################################################
# Solution
# ######################################################################################################################

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]: left += 1
                    while left < right and nums[right] == nums[right + 1]: right -= 1
                elif s < 0: left += 1
                else: right -= 1

        return result
