class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(speed) == 1:
            return 1
        n = len(position)
        cars = [(position[i], speed[i]) for i in range(n)]
        cars.sort()
        s = []
        for i in range(n-1, -1, -1):
            time = (target - cars[i][0]) / cars[i][1]
            if not s or time > s[-1]:
                s.append(time)
        return len(s)

