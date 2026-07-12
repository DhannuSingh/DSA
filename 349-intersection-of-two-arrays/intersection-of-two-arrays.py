class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        res = set()
        
        for num in nums2:
            if num in set1:
                res.add(num)
                
        return list(res)
        
        # Alternatively, using built-in set operations:
        # return list(set(nums1) & set(nums2))