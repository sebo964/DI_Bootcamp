class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        def isVowel(c):
            return c in "aeiou"

        def isVowelString(s):
            for c in s:
                if not isVowel(c):
                    return False
            return True

        def countVowelStrings(s):
            if len(s) == 0:
                return 0
            if isVowelString(s):
                return 1
            return countVowelStrings(s[1:]) + countVowelStrings(s[:-1])

        count = 0
        for i in range(left, right + 1):
            count += countVowelStrings(words[i])
        return count
