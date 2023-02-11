#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
24 Swap Nodes in Pairs
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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head and head.next:
            first_node = head
            second_node = head.next
            prev.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            head = first_node.next
            prev = first_node

        return dummy.next
