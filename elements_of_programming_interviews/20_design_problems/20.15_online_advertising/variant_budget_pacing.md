# EPI 20.15 Extra Variant - Global Ad Budget Enforcement and Pacing

(Practice problem, not in the book. Difficulty: Medium)

## Problem

Jingle's advertisers set daily budgets, for example "spend at most $500
per day on this campaign." Ads are served from thousands of ad servers in
a dozen regions, each making its own decision in a few milliseconds, and
an advertiser pays per click. Clicks arrive seconds to minutes after the
ad was shown, and some are later thrown out as invalid.

Design the system that keeps each campaign's spend within its budget and
spreads the spend evenly across the day (so a campaign doesn't burn its
whole budget at 6 a.m.). The focus is consistency under distribution:
servers can't make a synchronous call to a central counter on every ad
request, yet overspending costs Jingle money (advertisers aren't billed
beyond their budget) and underspending loses revenue.

## Questions to clarify

- What overspend is acceptable: zero, 1%, 5%? Who absorbs it?
- How fresh does each ad server's view of remaining budget need to be?
  What happens if a region is partitioned from the others for an hour?
- Is spend counted at impression time, click time, or both? How do you
  account for clicks that haven't arrived yet for ads already shown?
- Could you hand each region or server a slice of the budget (a lease)
  and rebalance periodically? How big should the slices be?
- What does "pacing evenly" mean when traffic is not uniform during the
  day? How would you forecast traffic and throttle participation?
- How do you handle a budget change made by the advertiser in the middle
  of the day, or a campaign that is paused?
- How are counters stored and aggregated (stream processing, sharded
  counters, CRDTs)? What is the source of truth for billing?
- Invalid clicks are refunded later. How does that feed back into the
  remaining budget?
- How would you test and monitor that pacing works (dashboards, alerts
  on overspend)?

## Your Answer

### Requirements

### Core API / Interfaces

### High-Level Design

### Data Model

### Scaling and Performance

### Trade-offs and Alternatives

### Follow-ups
