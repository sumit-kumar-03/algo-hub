# EPI 20.16 - Design a Recommendation System

## Problem

Jingle wants more page views on its news site. A product manager proposes
adding a sidebar to every article with clickable snippets of other articles
that a reader of the current one is likely to enjoy.

Design a system that automatically generates this sidebar of related
articles.

## Questions to clarify

- Which part is actually hard: rendering the sidebar or choosing the
  articles?
- What is the simplest thing that could work, with no algorithms at all
  (e.g. popular or recent articles)?
- Could human editors or existing metadata (meta tags, titles) supply
  topic tags?
- How would you discover which candidate articles readers actually like?
  Could you experiment on a subset of readers?
- How would you measure textual similarity between two articles? Which
  words should count for more, and which should be ignored?
- What are the pitfalls of purely textual similarity (e.g. the same word
  meaning different things in different contexts)?
- How could the reading behavior of many users be used instead of, or in
  addition to, article text? Where would that data come from?
- What does that behavioral approach require in order to work well?
- How do you handle brand-new articles with no reading history?
- How is success measured (click-through, page views per session)?

## Your Answer

### Requirements

### Core API / Interfaces

### High-Level Design

### Data Model

### Scaling and Performance

### Trade-offs and Alternatives

### Follow-ups
