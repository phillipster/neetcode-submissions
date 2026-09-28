class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque()
        counts = [0]*26
        for item in tasks:
            counts[ord(item)-ord('A')] += 1
        h = []
        for i in range(26):
            if counts[i] > 0:
                heapq.heappush_max(h, counts[i])
        cycle = 0
        while h or q:
            cycle += 1
            if h:
                cur = heapq.heappop_max(h)
                cur -= 1
                if cur > 0:
                    q.append((cycle, cur))
            if q:
                cooled = q[0]
                if cooled[0] + n == cycle:
                    heapq.heappush_max(h, cooled[1])
                    q.popleft()

        
        return cycle
