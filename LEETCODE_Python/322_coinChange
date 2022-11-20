class Solution:
    def coinChange(self, coins: List[int], amount : int) -> int:
        if amount == 0:
            return 0
        
        seen = set()
        count = 0
        remainders = [amount]
        
        while remainders:
            count += 1
            temp = []
            
            for val in remainders:
                    for coin in coins:
                        rem = val - coin
                        if rem ==0:
                            return count
        
                        elif rem >0 and rem not in seen:
                            seen.add(rem)
                            temp.append(rem)
        
            remainders = temp
        return -1
            