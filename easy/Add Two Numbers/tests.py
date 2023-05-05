from utils.utils import _test
from main import add, ListNode


def generate_list(l):
    result = ListNode(l[0])
    current = result
    for i in range(1, len(l)):
        current.next = ListNode(l[i])
        current = current.next

    return result


def test_standard_1():
    _test(func=add, expected=generate_list([7, 0, 8]), l1=generate_list([2, 4, 3]), l2=generate_list([5, 6, 4]))


def test_standard_2():
    _test(func=add, expected=ListNode(), l1=ListNode(), l2=ListNode())


def test_standard_3():
    _test(func=add, expected=generate_list([8, 9, 9, 9, 0, 0, 0, 1]), l1=generate_list([9] * 7), l2=generate_list([9] * 4))
