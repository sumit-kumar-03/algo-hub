"""
EPI 8.4 - Normalize Pathnames

Problem:
A pathname is either absolute (starts with "/") or relative to the current
directory. Names are alphanumeric and separated by "/"; "." means the
current directory and ".." means the parent directory. Repeated slashes act
like a single slash. Given a pathname, return the shortest equivalent
pathname.

Constraints:
- An empty path is invalid and must raise ValueError
- Going above the root of an absolute path ("/..") must raise ValueError
- A relative path may climb above the current directory; keep the leading
  ".." components in that case (e.g. "../a")
- The result has no trailing slash (except the root itself, "/")
- O(n) time, O(n) space

How it works (stack of path components):
1. If the path starts with "/", remember that it is absolute
2. Split on "/" and skip empty tokens and "."
3. For "..": pop the last name if there is one; if the stack is empty (or
   only holds ".." entries) in a relative path, push ".."; in an absolute
   path with nothing to pop, raise ValueError
4. For a name: push it
5. Join the stack with "/" (prefixing "/" for absolute paths)

Example 1:
Input: "/usr/lib/../bin/gcc"
Output: "/usr/bin/gcc"

Example 2:
Input: "scripts//./../scripts/awkscripts/././"
Output: "scripts/awkscripts"
Explanation: "scripts/.." cancels out, and "." and the extra slashes vanish.
"""


class Solution:
    def shortest_equivalent_path(self, path: str) -> str:
        """
        Returns the shortest pathname equivalent to path.

        Args:
            path: An absolute or relative pathname

        Returns:
            The normalized pathname

        Raises:
            ValueError: If path is empty or climbs above the root

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # TODO: Implement path normalization
        pass


def raises_value_error(fn) -> bool:
    """Returns True if calling fn raises ValueError."""
    try:
        fn()
    except ValueError:
        return True
    return False


def test_shortest_equivalent_path():
    """Test cases for pathname normalization"""
    solution = Solution()

    # Test case 1: Absolute path with ".."
    assert solution.shortest_equivalent_path("/usr/lib/../bin/gcc") == "/usr/bin/gcc"
    print("✓ Test 1 passed: Absolute path with ..")

    # Test case 2: Relative path with ".", "..", and repeated slashes
    assert (
        solution.shortest_equivalent_path("scripts//./../scripts/awkscripts/././")
        == "scripts/awkscripts"
    )
    assert solution.shortest_equivalent_path("sc//./../tc/awk/././") == "tc/awk"
    print("✓ Test 2 passed: Relative path cleanup")

    # Test case 3: Relative path climbing above the current directory
    assert solution.shortest_equivalent_path("../../a") == "../../a"
    assert solution.shortest_equivalent_path("a/../../b/../..") == "../.."
    print("✓ Test 3 passed: Leading .. components are kept")

    # Test case 4: Root and redundant root paths
    assert solution.shortest_equivalent_path("/") == "/"
    assert solution.shortest_equivalent_path("//a/./b/..//") == "/a"
    print("✓ Test 4 passed: Root handling")

    # Test case 5: Invalid paths
    assert raises_value_error(lambda: solution.shortest_equivalent_path(""))
    assert raises_value_error(lambda: solution.shortest_equivalent_path("/.."))
    assert raises_value_error(lambda: solution.shortest_equivalent_path("/a/../.."))
    print("✓ Test 5 passed: Invalid paths raise ValueError")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_shortest_equivalent_path()
