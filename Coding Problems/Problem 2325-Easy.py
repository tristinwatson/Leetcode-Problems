class Solution(object):
    def decodeMessage(self, key, message):
        ht = {" ": " "}
        alph = string.ascii_lowercase
        result = ""
        i = 0
        
        for char in key:
            if char not in ht:
                ht[char] = alph[i]
                i += 1
            
        for j in message:
            result = result + ht[j]
            
        return result