class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_map = {}
        for i in s:
            hash_map[i] = hash_map.get(i, 0)
            hash_map[i] += 1
        for i in t:
            if i not in hash_map.keys() or hash_map[i] == 0:
                return False
            else:
                hash_map[i] -= 1
        return True
