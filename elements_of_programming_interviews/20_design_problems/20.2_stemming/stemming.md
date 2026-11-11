# EPI 20.2 - Design a Solution to the Stemming Problem

## Problem

A search for "computation" should probably also match documents that
contain "computers", "compute", or "computing". With several keywords in a
query, enumerating every combination of every variant quickly becomes
impractical. Stemming maps all the variants of a word to a single common
root, applied to both queries and documents (e.g. computers, computer,
compute all become compute). Capturing every English variant is nearly
impossible, but a small set of rules handles most cases.

Design a stemming algorithm that is both fast and effective.

## Questions to clarify

- What general patterns do the example variants suggest? What kinds of
  rules would capture them?
- How do you handle cases where simply chopping a suffix gives the wrong
  root (e.g. "wolves")?
- With many suffix rules, how do you apply them efficiently to every word
  in a large corpus?
- How should exceptions to broad rules be expressed? Should rules depend on
  the shape of the remaining stem (e.g. vowel/consonant patterns)?
- Are there established stemmers you could build on or compare against?
- Could rewrite rules be learned from data rather than written by hand?
- Can surrounding words (context) help pick the correct stem?
- How do you measure "effective": over-stemming vs under-stemming, impact
  on search precision and recall?
- English only, or must the design extend to other languages?

## Your Answer

### Requirements

### Core API / Interfaces

### High-Level Design

### Data Model

### Scaling and Performance

### Trade-offs and Alternatives

### Follow-ups
