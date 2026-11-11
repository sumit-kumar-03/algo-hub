"""
EPI 5.9 - Enumerate All Primes to n

Problem:
A prime is an integer greater than 1 whose only divisors are 1 and itself.
Given an integer n, return all primes p with 2 <= p <= n in increasing
order.

Constraints:
- 0 <= n <= 10^6
- Aim for O(n log log n) time with a sieve (trial division is O(n^1.5))

How it works (sieve of Eratosthenes):
1. Create is_prime = [False, False, True, True, ..., True] of length n + 1
2. For p from 2 to n: if is_prime[p], add p to the result and mark
   p*p, p*p + p, p*p + 2p, ... as not prime
3. Return the collected primes

Example 1:
Input: n = 18
Output: [2, 3, 5, 7, 11, 13, 17]
Explanation: Every other number up to 18 has a divisor besides 1 and itself.

Example 2:
Input: n = 1
Output: []
Explanation: There are no primes below 2.
"""

from typing import List


class Solution:
    def generate_primes(self, n: int) -> List[int]:
        """
        Lists all primes up to and including n.

        Args:
            n: Upper bound (inclusive)

        Returns:
            Primes in [2, n] in increasing order

        Time Complexity: O(n log log n)
        Space Complexity: O(n)
        """
        # TODO: Implement the sieve of Eratosthenes
        pass


def test_generate_primes():
    """Test cases for prime enumeration"""
    solution = Solution()

    # Test case 1: Book example
    assert solution.generate_primes(18) == [2, 3, 5, 7, 11, 13, 17]
    print("✓ Test 1 passed: n = 18")

    # Test case 2: No primes
    assert solution.generate_primes(0) == []
    assert solution.generate_primes(1) == []
    print("✓ Test 2 passed: n = 0, 1 -> []")

    # Test case 3: Smallest prime, and n itself prime
    assert solution.generate_primes(2) == [2]
    assert solution.generate_primes(13) == [2, 3, 5, 7, 11, 13]
    print("✓ Test 3 passed: n = 2 and n = 13 (n is included)")

    # Test case 4: Perfect square bound
    assert solution.generate_primes(49) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    print("✓ Test 4 passed: n = 49 (49 itself excluded)")

    # Test case 5: Count of primes below 10^5
    primes = solution.generate_primes(100000)
    assert len(primes) == 9592 and primes[-1] == 99991
    print("✓ Test 5 passed: 9592 primes up to 100000")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_generate_primes()
