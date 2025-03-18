from collections import defaultdict
from typing import List


class LongestConsecutiveSequence:

    ## Nlog(N) solution
    def longestConsecutiveNLogN(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        longest_sequence = 0
        counter = 1 if len(sorted_nums) > 0 else 0
        for i in range(len(sorted_nums) - 1):
            if counter > longest_sequence:
                longest_sequence = counter

            if sorted_nums[i] == sorted_nums[i + 1]:
                i += 1

            if sorted_nums[i + 1] == sorted_nums[i] + 1:
                counter += 1
            else:
                counter = 0

        return longest_sequence

    def longestConsecutiveN(self, nums: List[int]) -> int:
        already_visited_dit = defaultdict(lambda: False)
        longest_length = 0

        for num in nums:
            already_visited_dit[num] = False

        for num in nums:
            sequence_length = 1

            ## Forward
            nextnum = num + 1
            while nextnum in already_visited_dit and not already_visited_dit[nextnum]:
                sequence_length += 1
                already_visited_dit[nextnum] = True
                nextnum += 1

            ##Backward
            prev_num = num - 1
            while prev_num in already_visited_dit and not already_visited_dit[prev_num]:
                sequence_length += 1
                already_visited_dit[prev_num] = True
                prev_num -= 1

            longest_length = max(longest_length, sequence_length)

        return longest_length


if __name__ == '__main__':
    solution = LongestConsecutiveSequence()
    print(solution.longestConsecutiveNLogN([100, 4, 200, 1, 3, 2]))
    print(solution.longestConsecutiveNLogN([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    print(solution.longestConsecutiveNLogN([1, 0, 1, 2]))

    assert solution.longestConsecutiveNLogN([100, 4, 200, 1, 3, 2]) == 4, "x must be equal to 4"
    assert solution.longestConsecutiveNLogN([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9, "x must be equal to 9"
    assert solution.longestConsecutiveNLogN([1, 0, 1, 2]) == 3, "x must be equal to 3"

    print(solution.longestConsecutiveN([100, 4, 200, 1, 3, 2]))
    print(solution.longestConsecutiveN([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    print(solution.longestConsecutiveN([1, 0, 1, 2]))

    assert solution.longestConsecutiveN([100, 4, 200, 1, 3, 2]) == 4, "x must be equal to 4"
    assert solution.longestConsecutiveN([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9, "x must be equal to 9"
    assert solution.longestConsecutiveN([1, 0, 1, 2]) == 3, "x must be equal to 3"
