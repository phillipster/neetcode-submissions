class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(speed) == 1:
            return 1
        n = len(position)
        cars = [(position[i], speed[i]) for i in range(n)]
        cars.sort()
        times = [(target - car[0]) / car[1] for car in cars]
        s = []
        for i in range(n-1, -1, -1):
            if not s:
                s.append(times[i])
            else:
                if times[i] > s[-1]:
                    s.append(times[i])
        return len(s)

