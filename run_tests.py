"""
Run every problem file in the repo and summarize the results.

Each problem file is a standalone script whose tests run under
`if __name__ == "__main__":` and print "All tests passed!" on success.
This runner executes them in parallel and sorts each file into:

  PASS     - printed "All tests passed"
  TODO     - failed, and the file still contains a "# TODO" stub (not attempted yet)
  FAIL     - failed, and no "# TODO" remains (an attempted solution is wrong)
  TIMEOUT  - did not finish in time

Usage:
  python3 run_tests.py                          # everything
  python3 run_tests.py fundamentals             # one folder (any path prefix works)
  python3 run_tests.py elements_of_programming_interviews/05_arrays -v
  python3 run_tests.py -v                       # list every file with its status
  python3 run_tests.py --show-failures          # print error output for FAIL/TIMEOUT

Exits with status 1 if any file is FAIL or TIMEOUT, so TODO stubs never break a run.
"""

import argparse
import subprocess
import sys
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKIP_DIRS = {".git", "__pycache__", ".venv", "venv"}
PASS_MARKER = "All tests passed"
TODO_MARKER = "# TODO"
STATUSES = ("PASS", "TODO", "FAIL", "TIMEOUT")
ICONS = {"PASS": "✅", "TODO": "⬜", "FAIL": "❌", "TIMEOUT": "⏱️"}


def find_problem_files(targets):
    """Collects problem files under the given paths (default: whole repo)."""
    roots = [ROOT / t for t in targets] if targets else [ROOT]
    files = set()
    for root in roots:
        if not root.exists():
            sys.exit(f"Path not found: {root}")
        candidates = [root] if root.is_file() else root.rglob("*.py")
        for path in candidates:
            rel = path.relative_to(ROOT)
            if path == Path(__file__).resolve() or SKIP_DIRS & set(rel.parts):
                continue
            files.add(path)
    return sorted(files, key=sort_key)


def sort_key(path):
    """Sorts numerically on section numbers so 4.3 comes before 4.11."""
    key = []
    for part in path.relative_to(ROOT).parts:
        head = part.split("_", 1)[0]
        nums = head.split(".")
        if all(n.isdigit() for n in nums):
            key.append((0, tuple(int(n) for n in nums), part))
        else:
            key.append((1, (), part))
    return key


def run_file(path, timeout):
    """Runs one problem file and classifies the outcome."""
    try:
        result = subprocess.run(
            [sys.executable, "-B", str(path)],  # -B: don't write __pycache__
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=path.parent,
        )
    except subprocess.TimeoutExpired:
        return path, "TIMEOUT", f"Timed out after {timeout}s"

    if PASS_MARKER in result.stdout and result.returncode == 0:
        return path, "PASS", ""
    status = "TODO" if TODO_MARKER in path.read_text(encoding="utf-8") else "FAIL"
    output = (result.stdout + result.stderr).strip().splitlines()
    return path, status, "\n".join(output[-8:])


def group_name(path):
    """Groups by source folder and chapter, e.g. 'fundamentals/03_recursion'."""
    parts = path.relative_to(ROOT).parts
    return "/".join(parts[:2]) if len(parts) > 2 else parts[0]


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("paths", nargs="*", help="folders or files to run (relative to repo root)")
    parser.add_argument("-v", "--verbose", action="store_true", help="list every file with its status")
    parser.add_argument("--show-failures", action="store_true", help="print output for FAIL/TIMEOUT files")
    parser.add_argument("--timeout", type=float, default=30, help="seconds per file (default: 30)")
    parser.add_argument("-j", "--jobs", type=int, default=8, help="files to run in parallel (default: 8)")
    args = parser.parse_args()

    files = find_problem_files(args.paths)
    if not files:
        sys.exit("No problem files found.")

    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        results = list(pool.map(lambda f: run_file(f, args.timeout), files))

    by_group = defaultdict(list)
    for path, status, output in results:
        by_group[group_name(path)].append((path, status, output))

    width = max(len(g) for g in by_group)
    print(f"{'Folder':<{width}}  {'PASS':>4}  {'TODO':>4}  {'FAIL':>4}  {'TIME':>4}  {'Done':>6}")
    print("-" * (width + 32))
    for group, items in by_group.items():
        counts = Counter(status for _, status, _ in items)
        done = f"{counts['PASS']}/{len(items)}"
        print(
            f"{group:<{width}}  {counts['PASS']:>4}  {counts['TODO']:>4}  "
            f"{counts['FAIL']:>4}  {counts['TIMEOUT']:>4}  {done:>6}"
        )
        if args.verbose:
            for path, status, _ in items:
                print(f"    {ICONS[status]} {status:<7} {path.relative_to(ROOT)}")

    totals = Counter(status for _, status, _ in results)
    print("-" * (width + 32))
    print("Total: " + ", ".join(f"{totals[s]} {s}" for s in STATUSES) + f" ({len(results)} files)")

    problems = [(p, s, o) for p, s, o in results if s in ("FAIL", "TIMEOUT")]
    if problems and args.show_failures:
        print("\nFailures:")
        for path, status, output in problems:
            print(f"\n{ICONS[status]} {path.relative_to(ROOT)}\n{output}")
    elif problems:
        print("\nNeeds attention: " + ", ".join(str(p.relative_to(ROOT)) for p, _, _ in problems))
        print("Run with --show-failures for details.")

    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
