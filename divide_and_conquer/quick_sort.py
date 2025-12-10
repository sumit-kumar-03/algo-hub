"""
Divide and Conquer: Quick Sort

Problem:
Given an array of integers nums, sort the array in ascending order using the Quick Sort algorithm.
Quick Sort is a Divide and Conquer algorithm that picks an element as a pivot and partitions
the given array around the picked pivot.

Constraints:
- Average Time Complexity: O(n log n)
- Worst Case Time Complexity: O(n^2) (depend on pivot selection)
- Space Complexity: O(log n) (recursion stack)

Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]

Example 2:
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
"""

from typing import List
import random

class Solution:
    def quickSort(self, nums: List[int]) -> List[int]:
        """
        Sorts an array using quick sort.
        """

        if len(nums)<2:
            return nums
        
        pivot=nums[-1]
        _lower=[nums[i] for i in range(len(nums)-1) if nums[i]<=pivot]
        _higher=[nums[i] for i in range(len(nums)-1) if nums[i]>pivot]

        return self.quickSort(_lower)+[pivot]+self.quickSort(_higher)


def test_quick_sort():
    """Test cases for quick sort implementation"""
    solution = Solution()
    
    # Test case 1: Random unsorted array
    result1 = solution.quickSort([10, 7, 8, 9, 1, 5])
    assert result1 == [1, 5, 7, 8, 9, 10]
    print("✓ Test 1 passed: [10, 7, 8, 9, 1, 5] -> [1, 5, 7, 8, 9, 10]")
    
    # Test case 2: Array with duplicates
    result2 = solution.quickSort([4, 2, 6, 2, 4])
    assert result2 == [2, 2, 4, 4, 6]
    print("✓ Test 2 passed: Duplicates handled correctly")
    
    # Test case 3: Already sorted array
    result3 = solution.quickSort([1, 2, 3, 4, 5])
    assert result3 == [1, 2, 3, 4, 5]
    print("✓ Test 3 passed: Already sorted array")
    
    # Test case 4: Reverse sorted array
    result4 = solution.quickSort([5, 4, 3, 2, 1])
    assert result4 == [1, 2, 3, 4, 5]
    print("✓ Test 4 passed: Reverse sorted array")
    
    # Test case 5: Empty array
    result5 = solution.quickSort([])
    assert result5 == []
    print("✓ Test 5 passed: Empty array")
    
    # Test case 6: Single element
    result6 = solution.quickSort([42])
    assert result6 == [42]
    print("✓ Test 6 passed: Single element")
    
    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_quick_sort()
