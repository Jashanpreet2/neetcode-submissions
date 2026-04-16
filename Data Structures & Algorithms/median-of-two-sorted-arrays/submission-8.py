class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        if total_len == 0:
            return    
        i = j = 0
        elements_passed = 0
        while elements_passed < total_len:
            elements_passed += 1
            
            if total_len % 2 == 0 and elements_passed == (total_len // 2):
                if len (nums1) > 0 and (len(nums2) == 0 or nums1[i] < nums2[j]):
                    if i+1 < len(nums1) and (len(nums2) == 0 or nums1[i+1] < nums2[j]):
                        return (nums1[i] + nums1[i + 1]) / 2
                    else:
                        return (nums1[i] + nums2[j]) / 2
                else:
                    if j < len(nums2) and (len(nums1) == 0 or nums2[j+1] < nums1[i]):
                        return (nums2[j] + nums2[j+1]) / 2
                    else:
                        return (nums1[i] + nums2[j]) / 2
            elif total_len % 2 == 1 and elements_passed == ((total_len//2) + 1):
                return nums1[i] if len(nums1) > 0 and (len(nums2) == 0 or nums1[i] < nums2[j]) else nums2[j]
            if i < len(nums1)-1 and (j >= len(nums2) or nums1[i] <= nums2[j]):
                i += 1
            else:
                j += 1

        