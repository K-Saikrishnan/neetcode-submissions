class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}

        for char in s:
            count[char] = count.setdefault(char, 0) + 1
        for char in t:
            count[char] = count.setdefault(char, 0) - 1
        
        return all(not v for v in count.values())

