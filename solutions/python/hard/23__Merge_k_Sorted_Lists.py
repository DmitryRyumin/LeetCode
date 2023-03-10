#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
23. Merge k Sorted Lists
"""

# ######################################################################################################################
# Required import
# ######################################################################################################################

import heapq

from typing import List, Optional

# ######################################################################################################################
# Solution
# ######################################################################################################################

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heap.append((lists[i].val, i))

        heapq.heapify(heap)

        while heap:
            val, i = heapq.heappop(heap)
            current.next = ListNode(val)
            current = current.next
            if lists[i].next:
                heapq.heappush(heap, (lists[i].next.val, i))
                lists[i] = lists[i].next

        return dummy.next
