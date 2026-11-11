"""
EPI 19.3 Extra Variant - Build Water Molecules from H and O Threads
(Practice problem, not in the book. Difficulty: Hard)
Builds on: Coordinating threads with shared state and blocking; here the
threads must be grouped (two H with one O) rather than strictly alternated.

Problem:
Atom threads arrive at a WaterFactory one at a time, in any order. Each
hydrogen thread calls hydrogen(release) and each oxygen thread calls
oxygen(release), where release() records that the atom joined a
molecule. Make the threads wait so that atoms are released in complete
molecules: in the output, every consecutive group of three releases
(positions 0-2, 3-5, ...) must contain exactly two "H" and one "O". A
thread must not release until it can form a molecule with two other
waiting atoms, and atoms of the next molecule must not slip in before
the current molecule's three releases are done.

Constraints:
- The test starts 2m hydrogen threads and m oxygen threads (1 <= m <= 30)
- Each thread calls exactly one method once
- No busy waiting
- Target: O(1) work per atom besides waiting

How it works (one possible approach):
1. A semaphore with 2 permits gates hydrogens and one with 1 permit gates
   oxygens, so at most 2 H and 1 O are "in the current molecule"
2. Each admitted atom waits at a 3-party barrier; when it trips, the
   molecule is complete, so the atom calls release()
3. Each atom waits at the barrier once more (all three have released),
   then returns its semaphore permit, letting the next molecule's atoms in
(A single Condition with counters for waiting H and O also works.)

Example 1:
Input: arrival order "HOH"
Output: a release order such as "HHO" or "OHH" (any order within the
molecule is fine)

Example 2:
Input: arrival order "OOHHHH"
Output: e.g. "OHHOHH" or "HOHHHO"; never "OOHHHH", because the first
three releases would contain two oxygens
"""

import random
import threading
from typing import Callable, List


class WaterFactory:
    def __init__(self) -> None:
        # TODO: Set up the synchronization primitives
        pass

    def hydrogen(self, release: Callable[[], None]) -> None:
        """
        Waits until this hydrogen can join a molecule, then calls release().

        Time Complexity: O(1) besides waiting
        Space Complexity: O(1)
        """
        # TODO: Implement hydrogen
        pass

    def oxygen(self, release: Callable[[], None]) -> None:
        """
        Waits until this oxygen can join a molecule, then calls release().

        Time Complexity: O(1) besides waiting
        Space Complexity: O(1)
        """
        # TODO: Implement oxygen
        pass


def simulate(arrivals: str, stagger: float = 0.0) -> str:
    """Starts one thread per atom in the given order; returns the releases."""
    out: List[str] = []
    factory = WaterFactory()
    threads = []
    for atom in arrivals:
        if atom == "H":
            target = lambda: factory.hydrogen(lambda: out.append("H"))
        else:
            target = lambda: factory.oxygen(lambda: out.append("O"))
        t = threading.Thread(target=target, daemon=True)
        t.start()
        threads.append(t)
        if stagger:
            threading.Event().wait(stagger)
    for t in threads:
        t.join(5.0)
    assert not any(t.is_alive() for t in threads), "atom threads did not finish"
    return "".join(out)


def valid_molecules(released: str, m: int) -> bool:
    if len(released) != 3 * m:
        return False
    return all(
        sorted(released[i : i + 3]) == ["H", "H", "O"]
        for i in range(0, len(released), 3)
    )


def test_build_water_molecules():
    """Test cases for building water molecules"""

    # Test case 1: A single molecule
    assert valid_molecules(simulate("HOH"), 1)
    print("✓ Test 1 passed: One molecule from H, O, H")

    # Test case 2: Oxygens arrive first, slowly
    assert valid_molecules(simulate("OOHHHH", stagger=0.02), 2)
    print("✓ Test 2 passed: Two oxygens wait for hydrogens")

    # Test case 3: Hydrogens arrive first, slowly
    assert valid_molecules(simulate("HHHHHHOOO", stagger=0.02), 3)
    print("✓ Test 3 passed: Six hydrogens wait for oxygens")

    # Test case 4: An incomplete set leaves the extra atoms waiting
    out: List[str] = []
    factory = WaterFactory()
    lone = [
        threading.Thread(target=factory.hydrogen, args=(lambda: out.append("H"),), daemon=True),
        threading.Thread(target=factory.oxygen, args=(lambda: out.append("O"),), daemon=True),
    ]
    for t in lone:
        t.start()
    for t in lone:
        t.join(0.3)
    assert all(t.is_alive() for t in lone), "atoms returned without a molecule"
    assert out == [], "atoms were released without a full molecule"
    print("✓ Test 4 passed: H + O alone are never released")

    # Test case 5: Shuffled arrivals, many molecules
    rng = random.Random(19)
    for m in (5, 12, 30):
        atoms = list("HHO" * m)
        rng.shuffle(atoms)
        assert valid_molecules(simulate("".join(atoms)), m)
    print("✓ Test 5 passed: Shuffled arrivals for 5, 12 and 30 molecules")

    # Test case 6: Repeated runs
    for rep in range(10):
        atoms = list("HHO" * 8)
        rng.shuffle(atoms)
        assert valid_molecules(simulate("".join(atoms)), 8)
    print("✓ Test 6 passed: 10 repeated shuffled runs")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_build_water_molecules()
