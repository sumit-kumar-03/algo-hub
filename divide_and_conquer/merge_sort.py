"""
Divide and Conquer: Merge Sort

Problem:
Given an array of integers nums, sort the array in ascending order using the Merge Sort algorithm.
Merge Sort is a classic Divide and Conquer algorithm that splits the array into two halves,
recursively sorts them, and then merges the sorted halves.

Constraints:
- You must write an algorithm with O(n log n) time complexity.
- Space complexity should be O(n).

Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]

Example 2:
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
"""

from typing import List

class Solution:

    def merge(self, left: List[int], right: List[int]) -> List[int]:

        i=0
        j=0
        merged_list=[]

        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                merged_list.append(left[i])
                i+=1
            else:
                merged_list.append(right[j])
                j+=1

        while i<len(left):
            merged_list.append(left[i])
            i+=1

        while j<len(right):
            merged_list.append(right[j])
            j+=1

        return merged_list

    def mergeSort(self, nums: List[int]) -> List[int]:
        """
        Sorts an array using merge sort.
        """


        # Base case: A list of 0 or 1 elements is already sorted
        if len(nums) <= 1:
            return nums
            
        mid=len(nums)//2
        left=nums[:mid]
        right=nums[mid:]

        left_merged  = self.mergeSort(left)
        right_merged = self.mergeSort(right)
        
        return self.merge(left_merged,right_merged)


def test_merge_sort():
    """Test cases for merge sort implementation"""
    solution = Solution()
    
    # Test case 1: Random unsorted array
    nums1 = [5, 2, 3, 1]
    sorted1 = solution.mergeSort(nums1)
    
    if sorted1 == []:
        print("⚠️  Warning: mergeSort returned empty list. Implementation missing.")
        return

    assert sorted1 == [1, 2, 3, 5]
    print("✓ Test 1 passed: [5, 2, 3, 1] -> [1, 2, 3, 5]")
    
    # Test case 2: Array with duplicates
    nums2 = [5, 1, 1, 2, 0, 0]
    assert solution.mergeSort(nums2) == [0, 0, 1, 1, 2, 5]
    print("✓ Test 2 passed: Duplicates handled correctly")
    
    # Test case 3: Already sorted array
    nums3 = [1, 2, 3, 4]
    assert solution.mergeSort(nums3) == [1, 2, 3, 4]
    print("✓ Test 3 passed: Already sorted array")
    
    # Test case 4: Reverse sorted array
    nums4 = [4, 3, 2, 1]
    assert solution.mergeSort(nums4) == [1, 2, 3, 4]
    print("✓ Test 4 passed: Reverse sorted array")
    
    # Test case 5: Empty array
    assert solution.mergeSort([]) == []
    print("✓ Test 5 passed: Empty array")
    
    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_merge_sort()
