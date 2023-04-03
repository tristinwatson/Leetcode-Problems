class Solution(object):
    def interpret(self, command):
        ans = ""
        lst = []
        lst.extend(command)

        for i in range(len(lst)):
            if lst[i] == 'G':
                ans = ans + 'G'
            elif lst[i] =='(' and lst[i+1] == ')':
                ans = ans + 'o'
            elif lst[i] =='(' and lst[i+1] == 'a':
                ans = ans + 'al'
            else:
                continue
        
        return ans