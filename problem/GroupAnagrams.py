from collections import defaultdict
from typing import List


class GroupAnagrams:

    def find_Anagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)

        return list(anagram_map.values())

    def find_Anagrams_RegularDict(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map.setdefault(sorted_word, []).append(word)

        return list(anagram_map.values())


if __name__ == '__main__':
    sol = GroupAnagrams()
    print(sol.find_Anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(sol.find_Anagrams([""]))
    print(sol.find_Anagrams(["a"]))

    print(sol.find_Anagrams_RegularDict(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(sol.find_Anagrams_RegularDict([""]))
    print(sol.find_Anagrams_RegularDict(["a"]))
