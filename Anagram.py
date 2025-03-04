from typing import Dict


class Anagram:

    def isAnagram(self, s: str, t: str) -> bool:

        s = s.strip()
        t = t.strip()

        if len(t) != len(s):
            return False

        # Convert s to array and add to dictionary to count each letter
        characters_word1 = list(s)
        characters_word2 = list(t)
        word1_dictionary = {}
        word2_dictionary = {}

        for character in characters_word1:
            if character in word1_dictionary:
                word1_dictionary[character] = word1_dictionary[character] + 1
            else:
                word1_dictionary[character] = 1

        for character in characters_word2:
            if character in word2_dictionary:
                word2_dictionary[character] = word2_dictionary[character] + 1
            else:
                word2_dictionary[character] = 1

        for key, value in word1_dictionary.items():
            if key not in word2_dictionary or value != word2_dictionary[key]:
                return False

        return True


if __name__ == '__main__':
    anagram = Anagram()
    print(anagram.isAnagram("anagram", "nagaram"))
    print(anagram.isAnagram("rat", "car"))
