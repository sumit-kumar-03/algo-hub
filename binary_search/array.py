"""
Binary Search in Sorted Array

Problem:
Given an array of integers nums which is sorted in ascending order, and an integer 
target, write a function to search target in nums. If target exists, then return 
its index. Otherwise, return -1.

Constraints:
- You must write an algorithm with O(log n) runtime complexity.
- 1 <= nums.length <= 10^4
- -10^4 < nums[i], target < 10^4
- All integers in nums are unique
- nums is sorted in ascending order

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Binary search implementation to find target in sorted array.
        
        Args:
            nums: Sorted array of integers in ascending order
            target: Integer to search for
            
        Returns:
            Index of target if found, -1 otherwise
            
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """

        low = 0
        
        high = len(nums) - 1


        while low<=high:
            mid = (low+high)//2
            guess =nums[mid]
            if guess==target:
                return mid
            elif guess>target:
                high=mid-1
            else:
                low=mid+1

        return -1


            
                
            



def test_binary_search():
    """Test cases for binary search implementation"""
    solution = Solution()
    
    # Test case 1: Target exists in the middle
    assert solution.search([-1, 0, 3, 5, 9, 12], 9) == 4
    print("✓ Test 1 passed: Target found in middle")
    
    # Test case 2: Target does not exist
    assert solution.search([-1, 0, 3, 5, 9, 12], 2) == -1
    print("✓ Test 2 passed: Target not found")
    
    # Test case 3: Target is the first element
    assert solution.search([-1, 0, 3, 5, 9, 12], -1) == 0
    print("✓ Test 3 passed: Target at beginning")
    
    # Test case 4: Target is the last element
    assert solution.search([-1, 0, 3, 5, 9, 12], 12) == 5
    print("✓ Test 4 passed: Target at end")
    
    # Test case 5: Single element array - target found
    assert solution.search([5], 5) == 0
    print("✓ Test 5 passed: Single element found")
    
    # Test case 6: Single element array - target not found
    assert solution.search([5], -5) == -1
    print("✓ Test 6 passed: Single element not found")
    
    print("\n✅ All tests passed!")


if __name__ == "__main__":
    # Run tests
    test_binary_search()
