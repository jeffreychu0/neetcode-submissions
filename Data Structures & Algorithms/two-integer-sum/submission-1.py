class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        addendToId = dict()

        for i in range(len(nums)):
            if nums[i] in addendToId:
                return [addendToId[nums[i]], i]

            addend = target - nums[i]
            addendToId[addend] = i

        return None


            