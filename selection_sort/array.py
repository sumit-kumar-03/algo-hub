"""
Selection Sort Algorithm

Problem:
Given an array of integers, sort the array in ascending order using the 
selection sort algorithm. Selection sort works by repeatedly finding the 
minimum element from the unsorted portion and placing it at the beginning.

Constraints:
- You must implement the selection sort algorithm
- 0 <= nums.length <= 10^4
- -10^4 < nums[i] < 10^4

How it works:
1. Find the minimum element in the unsorted portion
2. Swap it with the first element of the unsorted portion
3. Move the boundary of the unsorted portion one element to the right
4. Repeat until the array is sorted

Example 1:
Input: nums = [64, 25, 12, 22, 11]
Output: [11, 12, 22, 25, 64]
Explanation: 
Step 1: [11, 25, 12, 22, 64] (11 swapped with 64)
Step 2: [11, 12, 25, 22, 64] (12 swapped with 25)
Step 3: [11, 12, 22, 25, 64] (22 swapped with 25)
Step 4: [11, 12, 22, 25, 64] (25 stays)
Step 5: [11, 12, 22, 25, 64] (64 stays)

Example 2:
Input: nums = [5, 2, 9, 1, 5, 6]
Output: [1, 2, 5, 5, 6, 9]
"""

from typing import List


class Solution:
    def smallestSort(self, nums: List[int]) -> List[int]:
        smallest=nums[0]
        smallest_index=0

        for i in range(1,len(nums)):
            if nums[i]<smallest:
                smallest=nums[i]
                smallest_index=i
        
        return smallest_index
        

        
        
    def selectionSort(self, nums: List[int]) -> List[int]:
        """
        Selection sort implementation to sort array in ascending order.
        
        Args:
            nums: Array of integers to be sorted
            
        Returns:
            Sorted array in ascending order
            
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """

        sorted_list=[]
        cloned_list=list(nums)

        for i in range(len(nums)):
            smallest_index=self.smallestSort(cloned_list)
            sorted_list.append(cloned_list.pop(smallest_index))

        return sorted_list


def test_selection_sort():
    """Test cases for selection sort implementation"""
    solution = Solution()
    
    # Test case 1: Regular unsorted array
    nums1 = [64, 25, 12, 22, 11]
    expected1 = [11, 12, 22, 25, 64]
    assert solution.selectionSort(nums1) == expected1
    print("✓ Test 1 passed: Regular unsorted array")
    
    # Test case 2: Array with duplicates
    nums2 = [5, 2, 9, 1, 5, 6]
    expected2 = [1, 2, 5, 5, 6, 9]
    assert solution.selectionSort(nums2) == expected2
    print("✓ Test 2 passed: Array with duplicates")
    
    # Test case 3: Already sorted array
    nums3 = [1, 2, 3, 4, 5]
    expected3 = [1, 2, 3, 4, 5]
    assert solution.selectionSort(nums3) == expected3
    print("✓ Test 3 passed: Already sorted array")
    
    # Test case 4: Reverse sorted array
    nums4 = [5, 4, 3, 2, 1]
    expected4 = [1, 2, 3, 4, 5]
    assert solution.selectionSort(nums4) == expected4
    print("✓ Test 4 passed: Reverse sorted array")
    
    # Test case 5: Single element array
    nums5 = [42]
    expected5 = [42]
    assert solution.selectionSort(nums5) == expected5
    print("✓ Test 5 passed: Single element array")
    
    # Test case 6: Empty array
    nums6 = []
    expected6 = []
    assert solution.selectionSort(nums6) == expected6
    print("✓ Test 6 passed: Empty array")
    
    # Test case 7: Array with negative numbers
    nums7 = [-5, 3, -1, 7, -8, 0]
    expected7 = [-8, -5, -1, 0, 3, 7]
    assert solution.selectionSort(nums7) == expected7
    print("✓ Test 7 passed: Array with negative numbers")
    
    print("\n✅ All tests passed!")


if __name__ == "__main__":
    # Run tests
    test_selection_sort()
