class Solution(object):
    def sortPeople(self, names, heights):
        ht = {}
        ans = []

        for i in range(len(names)):
            ht[heights[i]] = names[i]

        for j in range(len(ht.keys())):
            ans.append(ht[j])

        return ans[::-1]