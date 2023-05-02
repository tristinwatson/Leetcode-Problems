class Solution(object):
    def maximum69Number(self, num):
        ans = ""
        string = str(num)
        pos = string.find("6")

        for i in range(len(string)):
            if pos == i:
                ans += "9"
            else:
                ans += string[i]
        
        return int(ans)