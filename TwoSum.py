from typing import List


# https://leetcode.com/problems/two-sum/description/
class TwoSum:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        for outer_index, val_outer in enumerate(nums):
            for inner_index, val_inner in enumerate(nums):
                if outer_index != inner_index:
                    if val_outer + val_inner == target:
                        return [outer_index, inner_index]
                else:
                    break

    def two_sum_efficient(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        n = len(nums)
        # Build the hash table
        for i in range(n):
            num_map[nums[i]] = i

        # Find the complement
        for i in range(n):
            complement = target - nums[i]
            if complement in num_map and num_map[complement] != i:
                return [i, num_map[complement]]
        return []  # No solution found


if __name__ == '__main__':
    sol = TwoSum()
    print(sol.two_sum([2, 7, 11, 15], 9))
    print(sol.two_sum([3, 2, 4], 6))
    print(sol.two_sum([3, 3], 6))
    print(sol.two_sum_efficient([2, 7, 11, 15], 9))
    print(sol.two_sum_efficient([3, 2, 4], 6))
    print(sol.two_sum_efficient([3, 3], 6))
