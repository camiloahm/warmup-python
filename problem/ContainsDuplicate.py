from typing import List, Set


class ContainsDuplicate:

    def contains_duplicates(self, nums:List[int])-> bool:
        setCounter=set()
        for num in nums:
            if num not in setCounter:
                setCounter.add(num)
            else:
                return True
        return False


if __name__ == '__main__':
    sol=ContainsDuplicate()
    print(sol.contains_duplicates([1,2,3,1]))
    print(sol.contains_duplicates([1,2,3,4]))
    print(sol.contains_duplicates([1,1,1,3,3,4,3,2,4,2]))