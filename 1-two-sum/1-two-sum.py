class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = 0
        for n in nums:
            nums2 = list(nums)
            nums2.remove(n)


            for n2 in nums2:
                if n + n2 == target:
                    a = 1
                    break
            if a == 1:
                break
        if nums.index(n) != nums.index(n2):        
            result = [nums.index(n), nums.index(n2)]
        else:
            result = []
            result.append(nums.index(n))
            nums.remove(n)
            result.append(nums.index(n) + 1)
        return result
