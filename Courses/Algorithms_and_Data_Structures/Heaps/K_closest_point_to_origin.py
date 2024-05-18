class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap, res, hash = [] , [], {}
        
        heapq.heapify(heap)
        for n in points:
            x = pow(n[0],2) + pow(n[1],2)
            heapq.heappush(heap, x)
            if x in hash:    
                hash[x].append(n)
            else:
                hash[x] = [n]
        for n in range(k):
            for i in hash[heapq.heappop(heap)]:
                res.append(i)
                if len(res) == k:
                    return res
        return  res