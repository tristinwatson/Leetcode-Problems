class Solution(object):
    def sortSentence(self, s):
        ans = []
        tokens = s.split(" ")
        i = 0

        while len(ans) != len(tokens):
            for j in range(len(tokens)):
                if int(tokens[j][-1]) == i + 1:
                    ans.append([j][:-1])
                    i +=1
        
        return " ".join(ans)