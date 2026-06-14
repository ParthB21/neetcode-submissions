class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #mapping the charCount to list of anagrams
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1 #ascii value of char - a, so a - a will be 0.
            res[tuple(count)].append(s) #change to tuple cuz list can't be key
        return list(res.values())