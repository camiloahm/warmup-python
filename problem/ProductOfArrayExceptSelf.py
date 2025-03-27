import logging
from typing import List

"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""


class ProductOfArrayExceptSelf:

    def bruteProductOfArrayExceptSelf(self, nums: List[int]) -> List[int]:

        result: List[int] = []
        for i in range(len(nums)):
            helper = 1
            for j in range(len(nums)):
                if i != j:
                    helper *= nums[j]
            result.append(helper)

        return result

    def productOfArrayExceptSelf(self, nums: List[int]) -> List[int]:
        left = {}
        right = {}
        result = []

        for i in range(len(nums)):
            if i == 0:
                left[i] = 1
            else:
                left[i] = left[i - 1] * nums[i - 1]

        for i in reversed(range(len(nums))):
            if i == len(nums) - 1:
                right[i] = 1
            else:
                right[i] = right[i + 1] * nums[i + 1]

        for i in range(len(nums)):
            result.append(left[i] * right[i])

        return result


if __name__ == '__main__':
    solution = ProductOfArrayExceptSelf()

    resultTestCase1 = solution.bruteProductOfArrayExceptSelf([1, 2, 3, 4])
    resultTestCase2 = solution.bruteProductOfArrayExceptSelf([-1, 1, 0, -3, 3])
    print(resultTestCase1)
    print(resultTestCase2)

    expectedTestCase1: List[int] = [24, 12, 8, 6]
    assert resultTestCase1 == expectedTestCase1, f"Elements are not equal {resultTestCase1} != {expectedTestCase1}"
    expectedTestCase2: List[int] = [0, 0, 9, 0, 0]
    assert resultTestCase2 == expectedTestCase2, f"Elements are not equal {resultTestCase2} != {expectedTestCase2}"

    print(solution.productOfArrayExceptSelf([1, 2, 3, 4]))
    print(solution.productOfArrayExceptSelf([-1, 1, 0, -3, 3]))
    # assert solution.productOfArrayExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    # assert solution.productOfArrayExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
