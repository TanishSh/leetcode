# hashmap implementation
from collections import Counter # import to create dict with counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # creates dict with key as the unqiue values in string, and 
        # values as the counter for those keys
        s_hash = Counter(s) 
        t_hash = Counter(t)

        # length of dict are different means, not same # of keys -> not same characters
        if len(s_hash) != len(t_hash):
            return False

        for key, value in s_hash.items():
            # character doesn't exist in t, so s & t are different
            if key not in t_hash:
                return False
            # same characters, but count of characters different, so not anagram
            if t_hash[key] != value:
                return False

        return True
    

# sorting implementation (copied)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)