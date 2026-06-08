class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        w1 = {}
        w2 = {}
        if len(s) != len(t):
            return False
        for i in s:
            w1[i] = w1.get(i,0)+1 #frequency loop, goes through each character in the word and updates its counter
        for i in t:
            w2[i] = w2.get(i,0)+1 #frequency loop, goes through each character in the word and updates its counter
        if w1 == w2:
            return True
        return False