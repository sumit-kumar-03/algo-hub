# EPI 20.13 Extra Variant - Global Low-CPM Fare Search at Scale

(Practice problem, not in the book. Difficulty: Hard)

## Problem

The mileage-run site has become popular, and the company now wants an
open search page: "show me the lowest cost-per-mile round trips departing
from any of these airports in the next 90 days," answered in under
300 ms, for about 20,000 searches per second at peak.

Fares come from global distribution systems (GDSs) that charge per query,
are slow (often seconds per request), and limit the ratio of searches to
bookings. Querying them live for every user search is impossible, so most
answers must come from a fare cache that is inevitably somewhat stale.
Design the fare ingestion, caching, and search system, and decide how
stale is acceptable and how the user is protected from booking a fare that
no longer exists.

## Questions to clarify

- How many (origin, destination, date) combinations exist, and how many
  are worth caching? How do you prioritize refreshes within a fixed
  upstream query budget?
- What staleness is acceptable for display, and what freshness is
  required at booking time? How do you verify a price just before
  purchase, and what does the user see if it changed?
- How do you precompute or index "lowest cpm from airport X in date
  range D" so the query is fast? What does the storage layout look like?
- Distance per itinerary (including connections) is needed for cpm. Where
  is it computed and stored?
- How do you shard and replicate the cache across regions? Is eventual
  consistency between regions acceptable?
- How do you detect that a cached fare is probably wrong (for example,
  many verification failures on one route) and refresh it early?
- How do you handle a sudden spike, such as a "mistake fare" going viral
  and everyone searching the same route at once?
- What metrics tell you whether the cache is "good enough" (hit rate,
  price accuracy, booking failure rate)?
- How would costs change if the GDS dropped its price per query by 10x,
  or raised it?

## Your Answer

### Requirements

### Core API / Interfaces

### High-Level Design

### Data Model

### Scaling and Performance

### Trade-offs and Alternatives

### Follow-ups
