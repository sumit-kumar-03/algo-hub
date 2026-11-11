# EPI 20.13 Extra Variant - Elite Status Qualification Planner

(Practice problem, not in the book. Difficulty: Medium)

## Problem

Reaching elite status is rarely about miles alone. Real loyalty programs
combine several thresholds (qualifying miles, qualifying segments,
qualifying dollars, sometimes a minimum number of flights on the airline's
own planes), and each fare class earns a different fraction of each.
Rules differ between programs and change every year.

Design a planner where a user enters their current progress, home
airport(s), target status, deadline, and constraints (for example "only
weekends", "at most 2 trips", "no red-eyes"), and the system proposes the
cheapest set of itineraries that gets them over every threshold in time.
Unlike the mileage-run system, the product is now an optimization over
combinations of trips with program-specific rules, not a single cpm
alert.

## Questions to clarify

- Which programs and statuses are supported at launch? How are their
  earning rules represented so non-engineers can update them each year?
- How does the system know a user's current progress: manual entry,
  linking the loyalty account, or parsing confirmation emails? What are
  the security implications of each?
- What does "cheapest" mean when trips also cost time? Should the user
  be able to trade dollars for fewer days away?
- The search space (routes x dates x fare classes x combinations of trips)
  is huge. How do you prune it? Is an exact answer needed or is a good
  heuristic acceptable?
- Is planning interactive (answer in a few seconds) or a background job
  that emails a plan later? How does that choice change the architecture?
- Fares change constantly. How long is a plan valid, and how do you
  re-check it before the user books?
- How do you explain a recommendation so users trust it ("this trip
  earns 4 segments and 3,200 qualifying dollars")?
- How do you test that the rules engine computes earnings correctly?
- What happens when a program changes its rules mid-year?

## Your Answer

### Requirements

### Core API / Interfaces

### High-Level Design

### Data Model

### Scaling and Performance

### Trade-offs and Alternatives

### Follow-ups
