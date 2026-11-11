# EPI 20.15 Extra Variant - Real-Time Bidding Ad Exchange

(Practice problem, not in the book. Difficulty: Hard)

## Problem

Jingle wants to sell ad slots on thousands of partner websites, not just
next to its own search results. Every time a page loads, an auction must
run: Jingle's exchange sends a bid request describing the slot to dozens
of external bidders (demand-side platforms), collects their bids, picks a
winner, and returns the winning ad, all within about 100 ms of the page
asking. Peak traffic is around 2 million auctions per second worldwide.

Design the exchange. Compared with the original problem, Jingle no longer
chooses ads itself: it runs a strict-deadline, fan-out auction against
outside systems it does not control, and must bill correctly for
billions of auctions per day.

## Questions to clarify

- What is the latency budget breakdown: network to the exchange, fan-out
  to bidders, waiting for bids, choosing a winner, returning the ad? What
  happens to bids that arrive late?
- How do you choose which bidders to ask for each request, given that
  asking everyone is expensive for both sides (traffic shaping)?
- Which auction type (first price, second price) and floor prices do you
  use, and how does that affect bidder behavior?
- Where are exchange servers located relative to publishers and bidders?
  How do you keep cross-region calls out of the critical path?
- How do you protect the exchange from a slow or misbehaving bidder
  (timeouts, circuit breakers, per-bidder quotas)?
- How are wins, impressions, and clicks logged so that billing between
  publishers, bidders, and Jingle is exact? What if a log record is lost
  or duplicated?
- How do you detect fraudulent publishers (bots generating fake page
  views) and bidders that don't pay?
- How do you test changes to auction logic safely when every millisecond
  and every cent matters (shadow traffic, A/B tests)?
- How does the system degrade under overload: drop requests, ask fewer
  bidders, or shorten the deadline?

## Your Answer

### Requirements

### Core API / Interfaces

### High-Level Design

### Data Model

### Scaling and Performance

### Trade-offs and Alternatives

### Follow-ups
