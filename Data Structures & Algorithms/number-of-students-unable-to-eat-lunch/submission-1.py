from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque(students)
        s = sandwiches[::-1]
        count = 0
        while s:
            stu = q.popleft()
            sand = s[-1]
            if stu != sand:
                count += 1
                q.append(stu)
                if count == len(q):
                    return len(q)
            else:
                count = 0
                s.pop()
        return 0