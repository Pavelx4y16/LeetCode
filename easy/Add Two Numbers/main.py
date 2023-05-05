# Definition for singly-linked list.
from typing import List


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if not self or not other:
            return False

        while self and other:
            if self.val != other.val:
                return False
            self = self.next
            other = other.next

        return True


def add(l1: ListNode, l2: ListNode):
    result = ListNode()
    current = result
    reminder = 0

    while l1 or l2 or reminder:
        first = l1.val if l1 else 0
        second = l2.val if l2 else 0

        _sum = first + second + reminder
        reminder = _sum // 10

        current.next = ListNode(_sum % 10)

        current = current.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return result.next
