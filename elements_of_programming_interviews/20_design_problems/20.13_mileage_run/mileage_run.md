# EPI 20.13 - Implement Mileage Run

## Problem

Airlines give frequent flyers a "status" (early boarding, extra baggage,
upgrades, and so on), usually based on miles flown over the last twelve
months. To keep their status, some travelers book a round trip purely for
the miles. The destination doesn't matter; what matters is minimizing
cost per mile (cpm), the ratio of dollars spent to miles flown.

Design a system that helps users find such mileage runs.

## Questions to clarify

- How can the implied features be split into independent pieces (e.g.
  user-facing vs backend)?
- What does a user's "alert" consist of? Origin, target cpm, travel dates?
  What other formulations are reasonable (multiple origins, destinations,
  check frequency)?
- Which pages or screens does the user-facing app need?
- How should login work: build your own, or delegate?
- Server-rendered pages or a single-page app talking JSON to the server?
- Where does flight and price data come from? Scraping vs a paid or free
  data feed, and what makes scraping hard?
- Flight data rarely includes distance. How would you compute cpm?
- How are alerts matched against fresh data, and how often? What triggers
  the check?
- What needs to be persisted, and how?
- Which language, frameworks, and hosting platform would you choose?
- How are users notified when a match is found?

## Your Answer

### Requirements

### Core API / Interfaces

### High-Level Design

### Data Model

### Scaling and Performance

### Trade-offs and Alternatives

### Follow-ups
