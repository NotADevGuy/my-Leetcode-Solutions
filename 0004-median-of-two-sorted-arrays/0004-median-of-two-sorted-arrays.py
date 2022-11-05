class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length = (len(nums1) + len(nums2))
        srt = (nums1 + nums2)
        srt.sort()
        print(srt)
        print(srt[length//2], srt[(length//2) - 1], srt[length//2]+ srt[(length//2) - 1])
        if length % 2 == 1:
            return srt[length//2]
        else:
            return float(srt[length//2] + srt[(length//2) - 1]) / 2