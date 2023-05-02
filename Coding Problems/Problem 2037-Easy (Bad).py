class Solution(object):
    def minMovesToSeat(self, seats, students):
        ans = 0

        while len(students) > 0:
            seat, seatInd, stu, stuInd = 0, 0, 0, 0

            for i in range(len(seats)):
                if seat <= seats[i]:
                    seat = seats[i]
                    seatInd = seats.index(seats[i])

            hiSeat = seats.pop(seatInd)

            for j in range(len(students)):
                if stu <= students[j]:
                    stu = students[j]
                    stuInd = students.index(students[i])
                
            hiStu = students.pop(stuInd)

            ans += ans(hiSeat - hiStu)

        return ans

            