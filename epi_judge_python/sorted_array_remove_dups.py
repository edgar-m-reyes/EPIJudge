import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
# def delete_duplicates_not_efficient(A: List[int]) -> int:
#     if not A:
#         return
#     nums = set(A)
#     for index, num in enumerate(sorted(nums)):
#         A[index] = num
#     for _ in range(index+1, len(A)):
#         A.pop()

def delete_duplicates(A: List[int]) -> int:
    last_invalid = 0
    seen = set()
    for index, num in enumerate(A):
        if num not in seen:
            if index != last_invalid:
                A[index], A[last_invalid] = A[last_invalid], A[index]
            last_invalid += 1
            seen.add(num)
    for _ in range(last_invalid, len(A)):
        A.pop()

# def delete_duplicates(A: List[int]) -> int: # book answer doesn't work ??
#     if not A:
#         return 0
    
#     last_valid = 1
#     for index in range(last_valid, len(A)):
#         if A[last_valid] - 1 != A[index]:
#             A[last_valid] = A[index]
#             last_valid += 1

#     return last_valid

@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
