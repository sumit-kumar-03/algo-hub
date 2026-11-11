# EPI 20.9 - Design TeraSort and PetaSort

## Problem

Modern datasets are enormous; a large social network may hold trillions of
distinct items. How would you sort one billion strings of 1,000 bytes each?
How about one trillion of them?

## Questions to clarify

- Roughly how many bytes is each dataset? Does the billion-string case fit
  in one machine's RAM? On one machine's disk? What about the
  trillion-string case?
- If the data fits on disk but not in memory, how do you sort it in pieces
  and combine the results efficiently?
- Are there existing tools that already do large on-disk sorts well?
- Once the data is spread over many machines, what does "sorted" even
  mean? What operations (e.g. lookups) must the result support?
- Is sorting each machine's portion independently enough? Why or why not?
- If a single machine merges everything, what becomes the bottleneck?
- How would you assign key ranges to machines so each gets a balanced
  share? How do you pick range boundaries without sorting everything
  first? When could that step be skipped?
- How does data move between machines during the reorganization, and can
  it be done without a central coordinator?
- After sorting, how is a lookup for a given string routed?
- How do you handle skewed data, machine failures, and stragglers?

## Your Answer

### Requirements

### Core API / Interfaces

### High-Level Design

### Data Model

### Scaling and Performance

### Trade-offs and Alternatives

### Follow-ups
