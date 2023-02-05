#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
19 Remove Nth Node From End of List
"""

# ######################################################################################################################
# Required import
# ######################################################################################################################

from typing import Optional

# ######################################################################################################################
# Solution
# ######################################################################################################################

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        slow = fast = dummy

        for i in range(n): fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next
