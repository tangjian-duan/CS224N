class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums = {}
        nums[2] = ['a','b','c']
        nums[3] = ['d','e','f']
        nums[4] = ['g','h','i']
        nums[5] = ['j','k','l']
        nums[6] = ['m','n','o']
        nums[7] = ['p','q','r','s']
        nums[8] = ['t','u','v']
        nums[9] = ['w','x','y','z']
        output = []
        s = ''
        def backtrack(digits):
            if len(digits) == 0:
                output.append(s)
                return
            num = int(digits[0])
            for i in nums[num]:
                s += i
                backtrack(digits[1:])
        return output

s = Solution()
aa = s.uniquePaths('23')
