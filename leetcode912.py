# 912. Sort an Array

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # quick sort implementation -> TLE :(
        
        """
        def partition(arr, l, r):
            # deterministic, always select the first
            rand = random.randint(l, r)
            piv = arr[rand]
            arr[l], arr[rand] = arr[rand], arr[l]
            i = l + 1
            j = l + 1

            while j <= r:
                if arr[j] <= piv:
                    arr[j], arr[i] = arr[i], arr[j]
                    i += 1
                j += 1
            # arr[l] is the piv itself 
            arr[l], arr[i-1] = arr[i-1], arr[l]
            
            return i - 1

        def quicksort(arr, l, r):
            if l < r:
                ind = partition(arr, l, r)
                quicksort(arr, l, ind - 1)
                quicksort(arr, ind + 1, r) 

        quicksort(nums, 0, len(nums)-1)
        return nums
        """

        # heap sort instead then which guarantees n log n
        for i in range(len(nums) // 2, -1, -1):
            self.max_heapify(nums, i, len(nums))
        
        for i in range(len(nums) - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.max_heapify(nums, 0, i)
        
        return nums
    
    def max_heapify(self, nums, i, n):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < n and nums[left] > nums[largest]:
            largest = left
        if right < n and nums[right] > nums[largest]:
            largest = right
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            self.max_heapify(nums, largest, n)
