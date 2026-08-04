class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for index, num in enumerate(nums):
            if (target - num) in my_dict:
                return [my_dict[target - num], index]

            my_dict[num] = index
        
        return []
