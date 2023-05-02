class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        ans = 0
        key = None

        if ruleKey == 'type':
            key = 0
        elif ruleKey == 'color':
            key = 1
        elif ruleKey == 'name':
            key = 2

        for i in range(len(items)):
            if items[i][key] == ruleValue:
                ans += 1

        return ans