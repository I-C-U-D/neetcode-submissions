class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        l = []

        for i in range(len(nums)-1):
            for j in range(1,len(nums)):

                if (nums[i] + nums[j]) == target and i != j and i not in l and j not in l:
                    l.append(i)
                    l.append(j)
        
        return l
        