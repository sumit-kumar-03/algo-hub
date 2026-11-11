"""
Recursion: Calculate Factorial

Problem:
Write a function to calculate the factorial of a non-negative integer n.
The factorial of n (denoted as n!) is the product of all positive integers less than or equal to n.
By definition, 0! = 1.

Constraints:
- 0 <= n <= 20 (for integer return type limits in some languages, though Python handles large ints)
- You must use recursion.

Example 1:
Input: n = 5
Output: 120
Explanation: 5! = 5 * 4 * 3 * 2 * 1 = 120

Example 2:
Input: n = 0
Output: 1
Explanation: 0! = 1 by definition
"""

class Solution:
    def factorial(self, n: int) -> int:
        """
        Calculates the factorial of n recursively.
        
        Args:
            n: Non-negative integer
            
        Returns:
            Factorial of n
            
        Time Complexity: O(n)
        Space Complexity: O(n) (due to recursion stack)
        """

        if n <= 1:
            return 1
        return n * self.factorial(n - 1)


def test_factorial():
    """Test cases for factorial implementation"""
    solution = Solution()
    
    # Test case 1: Standard positive integer
    assert solution.factorial(5) == 120
    print("✓ Test 1 passed: factorial(5) == 120")
    
    # Test case 2: Base case
    assert solution.factorial(0) == 1
    print("✓ Test 2 passed: factorial(0) == 1")
    
    # Test case 3: Smallest positive integer
    assert solution.factorial(1) == 1
    print("✓ Test 3 passed: factorial(1) == 1")
    
    # Test case 4: Slightly larger number
    assert solution.factorial(6) == 720
    print("✓ Test 4 passed: factorial(6) == 720")
    
    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_factorial()
