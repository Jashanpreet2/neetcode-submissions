class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = list(count.values())
        heapq.heapify_max(heap)
        q = deque()
        time = 0
        while heap or q:
            time += 1
            if heap:
                taskcount = heapq.heappop_max(heap)-1
                if taskcount > 0:
                    q.append([taskcount, time+n])
            if q and q[0][1] <= time:
                heapq.heappush_max(heap, q.popleft()[0])
        return time
