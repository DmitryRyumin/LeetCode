#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
16 3Sum Closest
"""

# ######################################################################################################################
# Required import
# ######################################################################################################################

from typing import List

# ######################################################################################################################
# Solution
# ######################################################################################################################

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue
            left, right = i + 1, len(nums) - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if abs(s - target) < abs(closest - target): closest = s
                if s < target: left += 1
                elif s > target: right -= 1
                else: return target

        return closest
