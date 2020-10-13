import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap =[]
        for i in stones:
            heap.append(-1*i)
        heapq.heapify(heap)
    
        while len(heap) >= 2:
           
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            
            if x != y:
                heapq.heappush(heap,-1*abs(y-x))
                
        if len(heap) >= 1:
            return -1*heap[-1]
        else:
            return 0
            
