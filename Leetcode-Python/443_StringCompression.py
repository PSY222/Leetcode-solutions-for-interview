class Solution1:
    def compress(self, chars: List[str]) -> int:
        count = 1
        left = 0

        for right in range(1,len(chars)+1):
            if right < len(chars) and chars[right-1] == chars[right]:
                count += 1
            else:
                chars[left] = chars[right-1]
                left += 1
                if count > 1:
                    for c in str(count):
                        chars[left] = c
                        left += 1
                count = 1

        return left
    

class Solution2:
    def compress(self, chars: List[str]) -> int:
        walker, runner = 0, 0
        while runner < len(chars):
		
            chars[walker] = chars[runner]
            count = 1
			
            while runner + 1 < len(chars) and chars[runner] == chars[runner+1]:
                runner += 1
                count += 1
			
            if count > 1:
                for c in str(count):
                    chars[walker+1] = c
                    walker += 1
            
            runner += 1
            walker += 1
        
        return walker