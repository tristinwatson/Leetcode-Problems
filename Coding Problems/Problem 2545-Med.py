class Solution(object):
    def sortTheStudents(self, score, k):
        ans = []
        score2 = list(score)

        while len(ans) < len(score):
            hi, hold = 0, 0

            for i in range(len(score2)):
                if hi < score2[i][k]:
                    hi  = score2[i][k]
                    hold = i

            upd = score2.pop(hold)
            ans.append(upd)

        return ans