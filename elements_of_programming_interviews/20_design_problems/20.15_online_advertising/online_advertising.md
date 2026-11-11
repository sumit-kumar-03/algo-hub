# EPI 20.15 - Design an Online Advertising System

## Problem

Jingle, a successful search engine startup, has many customers asking to
show paid ads for their products and services next to search results.

Design Jingle's advertising system.

## Questions to clarify

- Who are the stakeholders (searchers, advertisers, Jingle itself), and
  what does each want from the system?
- What are the major subsystems? What do advertisers interact with, and
  what decides which ads appear on a search?
- What must advertisers be able to do: create ads, organize campaigns,
  restrict when and where ads run, set budgets, bid on keywords, view
  reports?
- How do advertisers authenticate?
- When automation isn't enough (e.g. overriding keyword limits), how do
  advertisers reach support, and what tools do support staff need?
- What technology stack would you use for the advertiser-facing side?
- How does the ad server decide which ads are "relevant" to a search?
  Which signals beyond keywords could it use (history, bid, time of day,
  locale, browser)?
- What data structure lets the ad server choose ads quickly?
- How are ads inserted into the results page without slowing down search
  results?
- How do you guard against inappropriate images or keywords pointing at
  bogus sites?
- How are ad images served at scale, and what is shown if no ad matches?

## Your Answer

### Requirements

### Core API / Interfaces

### High-Level Design

### Data Model

### Scaling and Performance

### Trade-offs and Alternatives

### Follow-ups
