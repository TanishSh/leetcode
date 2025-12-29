# hash table
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        li = [] # hashmap
        for s in strs:
            count = [0] * 26
            for index, char in enumerate(s):
                count[ord(char) - ord('a')] += 1
            li.append(count)

        output = []
        output.append([strs[0]])

        unique_elements_index = [[0, len(output)-1]]
        
        for i in range(1, len(strs)):
            found = False
            for index, (u_i_li, u_i_output) in enumerate(unique_elements_index): # unique index
                item_exists = any(strs[i] in sublist for sublist in output)
                if i != u_i_li and not item_exists and li[i] == li[u_i_li]: 
                    output[u_i_output].append(strs[i])
                    Found = True
                    break
            
            item_exists = any(strs[i] in sublist for sublist in output)
            if not found and not item_exists:   
                output.append([strs[i]])
                unique_elements_index.append([i, len(output)-1])

        return output

        

