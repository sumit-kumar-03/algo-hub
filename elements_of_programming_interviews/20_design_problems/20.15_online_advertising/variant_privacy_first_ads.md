# EPI 20.15 Extra Variant - Privacy-First Advertising Without User Tracking

(Practice problem, not in the book. Difficulty: Medium)

## Problem

New regulations and browser changes mean Jingle can no longer build
long-term profiles of individual searchers: no third-party cookies, no
cross-site tracking, and users in some regions can demand that everything
about them be deleted within 30 days. Advertisers still want relevant ads
and trustworthy reports on how their campaigns perform.

Redesign Jingle's ad selection and reporting so it works with these
product and legal constraints. The ranking must rely on signals that are
allowed (the current query, coarse location, time of day, language,
perhaps on-device signals), and reporting must give advertisers useful
aggregates without exposing any individual's behavior.

## Questions to clarify

- Which signals are still allowed, and which need explicit consent? How
  does consent get recorded and enforced in the serving path?
- How good can purely contextual targeting (query and page content) be?
  How would you measure the revenue impact of losing user profiles?
- Could some personalization run on the user's device, with only coarse
  results (for example an interest category) sent to the server? What
  are the risks?
- How do you report conversions (a purchase on the advertiser's site)
  without joining user identities across sites? What delay and noise are
  acceptable in reports?
- How do you keep small aggregates (for example "3 clicks from one zip
  code") from identifying people? Minimum thresholds? Differential
  privacy? What does each cost in accuracy?
- How do you implement deletion requests across logs, data warehouses,
  backups, and trained models?
- How do fraud detection and frequency capping work without a stable
  user identifier?
- Regulations differ by country. How do you serve each region under its
  own rules without maintaining completely separate systems?

## Your Answer

### Requirements

### Core API / Interfaces

### High-Level Design

### Data Model

### Scaling and Performance

### Trade-offs and Alternatives

### Follow-ups
