# hashmap implementation - my solution
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
    
# ---------------------------------------------- solution 2 ---------------------------------------------------
# sorting implementation (copied)

# If the lengths of the two strings differ, return False immediately because they cannot be anagrams.
# Sort both strings.
# Compare the sorted versions of the strings:
# If they are equal, return True.
# Otherwise, return False.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t) #returns sorted version of original iterable without mutation (modifying original)
    

# ---------------------------------------------- solution 3 ---------------------------------------------------
# Hash Map 
# If the two strings have different lengths, return False immediately.
# Create two hash maps to store character frequencies for each string.
# Iterate through both strings at the same time:
# Increase the character count for s[i] in the first map.
# Increase the character count for t[i] in the second map.
# After building both maps, compare them:
# If the maps are equal, return True.
# Otherwise, return False.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. If the lengths are different, they cannot be anagrams.
        if len(s) != len(t):
            return False

        # 2. Create two empty dictionaries to store character counts.
        countS = {}  # counts for string s
        countT = {}  # counts for string t

        # 3. Go through each index of the strings
        for i in range(len(s)):
            char_s = s[i]  # character from s at position i
            char_t = t[i]  # character from t at position i

            # --- Update countS for char_s ---
            if char_s in countS:
                # if we have seen this character before, increase its count
                countS[char_s] += 1
            else:
                # if this is the first time, set its count to 1
                countS[char_s] = 1

            # --- Update countT for char_t ---
            if char_t in countT:
                countT[char_t] += 1
            else:
                countT[char_t] = 1

        # 4. If the two dictionaries of counts are the same,
        #    then s and t have the same characters with the same frequencies.
        return countS == countT

# ---------------------------------------------- solution 4 ---------------------------------------------------
# Hash table - using array
# If the lengths of the strings differ, return False immediately.
# Create a frequency array count of size 26 initialized to zero.
# Iterate through both strings:
# Increment the count at the index corresponding to s[i].
# Decrement the count at the index corresponding to t[i].
# After processing both strings, scan through the count array:
# If any value is not zero, return False because the frequencies differ.
# If all values are zero, return True since the strings are anagrams.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26

        for i in range(len(s)):
            # ord(): single character converted to asci integer
            # ord('A') returns 65
            # ord('a') returns 97
            # ord('$') returns 36
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
            
        return True
    


