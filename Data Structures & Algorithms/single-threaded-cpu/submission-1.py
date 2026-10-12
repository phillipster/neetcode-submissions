class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        output = []
        q = [(tasks[i][0], tasks[i][1], i) for i in range(n)]
        heapq.heapify(q)
        proc = []
        time = 1
        print(q)
        while q or proc:
            while q and q[0][0] <= time:
                t = heapq.heappop(q)
                heapq.heappush(proc, (t[1], t[2]))
            if proc:
                task = heapq.heappop(proc)
                time += task[0]
                output.append(task[1])
            else:
                time = q[0][0]
                
        return output
