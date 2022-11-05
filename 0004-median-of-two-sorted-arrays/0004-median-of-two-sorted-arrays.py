class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length = (len(nums1) + len(nums2))
        srt = []
        srt = (nums1 + nums2)
        srt.sort()
        if length % 2 == 1:
            return srt[length//2]
        else:
            return float(srt[length//2] + srt[(length//2) - 1]) / 2
        
        # My sorting, since it doesn't make it faster???
        """
        i1 = i2 = 0
        while i1 != len(nums1) or i2 != len(nums2):
            if i1 == len(nums1):
                srt.append(nums2[i2])
                i2 += 1
            elif i2 == len(nums2):
                srt.append(nums1[i1])
                i1 += 1
            else:
                if nums1[i1] < nums2[i2]:
                    srt.append(nums1[i1])
                    i1 += 1
                else:
                    srt.append(nums2[i2])
                    i2 += 1
        """
        