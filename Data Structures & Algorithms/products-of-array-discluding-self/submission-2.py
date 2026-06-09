class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # this is highly inefficient surely there's a better way
        
        sol = []
        prod = 1
        zeroCount = 0
        
        for i in nums:
            if i==0:
                zeroCount+=1
                continue
            prod *=i
        
        for i in nums:
            if zeroCount == 0:
                #temp = int(prod/i)
                sol.append(prod // i)

            elif zeroCount > 1:
                sol.append(0)
            
            else:
                if i == 0:
                    sol.append(prod)
                else:
                    sol.append(0)
        return sol