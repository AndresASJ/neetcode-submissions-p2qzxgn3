class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1 #last elem of m
        j = n-1 #lest elem of n
        k = m+n-1 #last elem of m+n

        while i>=0 and j>= 0: #until either array is empty
            if nums1[i] > nums2[j]:  #if nums1 [at array size 4] is greater than nums2[at array size 2] at their specific element
                nums1[k] = nums1[i]  #update the last elem of nums [which is normally at 6 elem]
                i -= 1 #lower the array size of nums1[not inlcuding the two zeros at the end]

            else:  
                nums1[k] =nums2[j] #update nums1 at position k with nums2 position j
                j -= 1 #decrement j
            k -=1 #at the end of the while cycle, update k
        nums1[:j+1] = nums2[:j+1]        #add the rest of nums2 to nums1 at j+1 [because python sclicing stop at the number so we do j+1 to include j]