# Solution1, Source: https://leetcode.com/problems/jump-game-ii/discuss/1439932/Simple-Python-O(n)-greedy-solution
class Solution:
    def jump(self, nums: List[int]) -> int:
        cur_jump_max = next_jump_max = ret = 0
        for i in range(len(nums)-1):
            next_jump_max = max(next_jump_max, i+nums[i])
            if i == cur_jump_max:
                ret += 1
                cur_jump_max = next_jump_max
        return ret         
    
# Solution2, Source: https://leetcode.com/problems/jump-game-ii/discuss/170518/8-Lines-in-Python!-Easiest-Solution!
    def jump(self, nums):
        if len(nums) <= 1: return 0
        l, r = 0, nums[0]
        times = 1
        while r < len(nums) - 1:
            times += 1
            nxt = max(i + nums[i] for i in range(l, r + 1))
            l, r = r, nxt
        return times


#Solution3, BFS, Source:https://leetcode.com/problems/jump-game-ii/discuss/2208416/Python-Intuitive-BFS-solution-with-a-deque-explained
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        q = deque([(0,0)])
		
        visited = set([0])
        
        while q:
            cur, jumps = q.popleft()

            if cur == n - 1:
                return jumps
            
            for i in range(cur + 1, min(cur+nums[cur]+1,n)):
                if i not in visited:
                    visited.add(i)
                    q.append((i,jumps+1))