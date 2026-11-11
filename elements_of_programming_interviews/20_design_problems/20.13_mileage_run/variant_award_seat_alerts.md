# EPI 20.13 Extra Variant - Real-Time Award Seat Alerts

(Practice problem, not in the book. Difficulty: Medium)

## Problem

Frequent flyers often want to spend miles rather than earn them. Airlines
release a small number of "award seats" (seats bookable with points) on
each flight, and the good ones, such as business class on long-haul
routes, tend to appear without warning and disappear within minutes.

Design a service where users register watches like "two business-class
award seats from SFO to Tokyo on any day in March for at most 120,000
points each" and get notified fast enough to actually book the seats.
Compared with the mileage-run system, freshness is now the main
constraint: an alert that arrives 30 minutes late is worthless.

Assume about 2 million active watches covering 50,000 distinct
(origin, destination, date) combinations, and that availability comes from
airline and partner APIs that are rate-limited and charge per query.

## Questions to clarify

- What exactly can a watch specify: cabin, number of seats, date range,
  flexible airports, max points, partner airlines, nonstop only?
- What notification latency is "fast enough"? How do you measure it end
  to end (from seat release to the user's phone)?
- Upstream APIs are rate-limited and cost money. How do you decide which
  routes and dates to poll, and how often? Should popular routes (many
  watchers) be polled more often than obscure ones?
- Can many watches share a single upstream query? How do you index watches
  so a fresh availability result is matched to every interested user
  quickly?
- Is there any push feed (webhooks, change streams) from airlines, or is
  everything polling? How would the design change if one existed?
- How do you avoid notifying a user repeatedly about the same seats, or
  about seats that vanished again seconds later?
- If 10,000 users watch the same route, who gets notified first? Is that
  fair, and does it matter?
- Which channels (push, SMS, email) are used, and how do you keep the
  notification pipeline itself from adding minutes of delay?
- What happens when an upstream API is down or starts returning errors?
- Should premium users get faster polling? How would you enforce that?

## Your Answer

### Requirements

### Core API / Interfaces

### High-Level Design

### Data Model

### Scaling and Performance

### Trade-offs and Alternatives

### Follow-ups
