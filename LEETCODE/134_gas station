class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:        
        
        def detect(curr,start):
            while curr > 0:
                for i in range(start,len(gas)+start+1):
                    if i >= len(gas):
                        curr = curr-cost[i-len(gas)]+gas[i-len(gas)]
                    else:
                        curr = curr-cost[i] + gas[i]
                return True
            return False
        
        curr = 0
        for i in range(len(gas)):
            if gas[i] >= cost[i]:
                if detect(curr,i):
                    return i
                else:
                    return -1