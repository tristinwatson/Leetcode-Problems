class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        ans = arrivalTime + delayedTime

        if ans >= 24:
            ans -= 24

        return ans