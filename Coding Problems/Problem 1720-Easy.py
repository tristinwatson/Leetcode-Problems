class Solution(object):
    def decode(self, encoded, first):
        ans = [first]

        for i in range(len(encoded)):
            ans.append(ans[-1] ^ encoded[i])
        
        return ans