from collections import defaultdict
from typing import List


class TopKFrequentElements:

    def find_top_k_frequent_elements(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = defaultdict(int)
        counterArray = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            frequencyMap[num] += 1

        for key, frequency in frequencyMap.items():
            counterArray[frequency].append(key)

        result = []
        for i in reversed(counterArray):
            for j in i:
                if len(result) < k:
                    result.append(j)
                else:
                    return result

        return result


if __name__ == '__main__':
    sol = TopKFrequentElements()
    print(sol.find_top_k_frequent_elements([1, 1, 1, 2, 2, 3], 2))
    print(sol.find_top_k_frequent_elements([1], 1))
