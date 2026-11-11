# EPI 20.1 - Design a Spell Checker

## Problem

Computing the edit distance between two given strings is a solved
building block, but a real spell checker has a harder job: given a word
that might be misspelled, it must search the whole dictionary for the words
most likely intended and present them as ranked suggestions. Plain
Levenshtein distance may also be the wrong yardstick, since it ignores
common real-world misspellings and the layout of the keyboard.

Design a spelling correction system.

## Questions to clarify

- What notion of "distance" between a typed word and a dictionary word
  should drive candidate generation, and how far away (in edits) do
  intended words usually lie?
- How do you find nearby dictionary words efficiently instead of comparing
  against every word? How many lookups does that cost for a word of length
  n over an alphabet of size m?
- Once you have a candidate set, how do you rank it so the most likely
  correction comes first?
- How would keyboard layout (adjacent-key typos) factor into ranking?
- What about people who know how a word sounds but not how it's spelled?
- Can user behavior (typing a word, then correcting it) be used as a
  signal? Where would that data come from?
- Can the dictionary be shrunk (e.g. by storing only word roots), and what
  does that imply for the query word?
- Is this an interactive (as-you-type) checker or a batch one? What are the
  latency targets?

## Your Answer

### Requirements

### Core API / Interfaces

### High-Level Design

### Data Model

### Scaling and Performance

### Trade-offs and Alternatives

### Follow-ups
