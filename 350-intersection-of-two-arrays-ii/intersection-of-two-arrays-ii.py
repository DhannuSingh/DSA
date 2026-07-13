class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Ensure nums1 is the smaller array to optimize space
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        
        counts = Counter(nums1)
        ans = []

        for num in nums2:
            if counts[num] > 0:
                ans.append(num)
                counts[num] -= 1
        
        return ans