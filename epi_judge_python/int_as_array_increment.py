from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    carry = 1
    for index in range(len(A)-1, -1, -1):
        A[index] = ((A[index] + carry) % 10)
        if (A[index] == 0) and carry:
            carry = 1
        else:
            carry = 0
    if carry == 1:
        A.insert(0, 1)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
