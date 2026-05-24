# Discover Algorithm Design Guide for Website and App Designers
## A product-safe design translation inspired by the public xAI X algorithm repository

Version: 1.0
Owner: Product, design, engineering, and AI assistants
Status: Reference guide for discovery feeds, explore pages, recommendation shelves, marketplace ranking, content hubs, and personalized dashboards.
Scope: Websites, mobile apps, SaaS dashboards, content products, ecommerce discovery, creator platforms, learning platforms, AI-assisted product surfaces, and internal recommendation tools.

---

## 0. Purpose

This guide explains how a modern discover algorithm can be understood by website and application designers without requiring them to implement the production machine learning system.

It uses the public [xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) repository as a reference pattern. That repository describes the X "For You" feed as a pipeline that gathers user context, retrieves candidate posts from followed and global sources, hydrates those candidates with metadata, filters ineligible items, scores remaining items, ranks them, and applies final selection checks.

This guide translates that pattern into design decisions:

- What the discovery surface should feel like.
- Which user controls should exist.
- Which signals should be captured.
- Which safety, privacy, performance, and optimization rules should constrain ranking.
- How designers should communicate algorithmic behavior to engineers and AI coding assistants.

This is not a clone specification for X, xAI, or any private production system. It is a public-safe design model for building trustworthy discovery experiences.

---

## 1. Designer Mental Model

A discovery algorithm is not one magic score. It is a product pipeline.

Use this simple model:

```text
User request
-> user context
-> candidate sources
-> candidate hydration
-> eligibility filters
-> scoring
-> ranking and blending
-> final safety checks
-> rendered discovery surface
-> feedback loop
```

For designers, each stage maps to a visible product question:

| Pipeline stage | Designer question | Example design output |
| :--- | :--- | :--- |
| User request | Why is this person opening Discover now? | Default state, search intent, tab selection, location in journey |
| User context | What should the product remember safely? | Followed topics, saved items, recent interactions, explicit preferences |
| Candidate sources | Where can relevant items come from? | Following, trending, editorial collections, similar items, sponsored inventory |
| Candidate hydration | What metadata is needed before display? | Author, thumbnail, price, freshness, availability, trust labels |
| Eligibility filters | What should never appear here? | Blocked users, unavailable items, unsafe content, duplicates, already dismissed content |
| Scoring | What does "good for this user now" mean? | Relevance, quality, freshness, diversity, business constraints |
| Ranking and blending | How should the page avoid repetition? | Mixed content types, topic variety, ad separation, creator variety |
| Final checks | What must be verified before rendering? | Policy compliance, access rights, age gates, content warnings |
| Feedback loop | How can the user correct the system? | Hide, mute, follow topic, save, report, "less like this" |

---

## 2. xAI Reference Pattern in Product Terms

The public xAI repository describes these major concepts:

- `Home Mixer`: the orchestration layer that assembles the feed.
- `Thunder`: an in-network candidate source for recent posts from followed accounts.
- `Phoenix Retrieval`: an out-of-network candidate source that retrieves relevant posts from a larger corpus.
- `Phoenix Ranking`: a model that predicts engagement probabilities and ranks candidates.
- Filtering: duplicate, age, viewer-authored, blocked, muted, previously seen, subscription, visibility, and policy checks.

Translated for product and design teams:

| xAI concept | Design translation | Use in a website or app |
| :--- | :--- | :--- |
| Home Mixer | Discovery page controller | Decides which modules, cards, shelves, and ranking rules apply to this request |
| Thunder | Familiar source | Items from followed creators, saved brands, subscribed topics, team workspace, or recent collaborators |
| Phoenix Retrieval | Expansion source | Items the user does not follow yet but is likely to find useful |
| Hydration | Display readiness | Fetching labels, media, status, price, availability, permissions, and trust context |
| Filters | Guardrails | Removing unsafe, blocked, repeated, expired, private, or inaccessible items |
| Scoring | Relevance estimate | Predicting which items are most useful, engaging, or task-relevant |
| Ranking | Presentation order | Sorting and blending candidates into a usable screen |
| Post-selection filters | Final trust pass | Last check before showing content to the user |

Design rule:

> The interface should expose enough control for trust, but not expose sensitive ranking internals, private signals, or system-abuse details.

---

## 3. Discovery Surface Types

Different products need different discovery patterns.

| Surface | Best for | Default ranking shape |
| :--- | :--- | :--- |
| Infinite feed | Social, content, news, creator apps | Personalized relevance with strong freshness and safety gates |
| Explore grid | Visual media, portfolios, marketplaces | Topic clusters, novelty, thumbnails, fast scanning |
| Recommendation shelf | Ecommerce, streaming, learning | Contextual retrieval around the current item or task |
| Search plus discovery | Knowledge bases, SaaS, docs | Query relevance first, personalized boosts second |
| Dashboard suggestions | B2B, productivity, internal tools | Task urgency, permissions, business rules, low noise |
| Onboarding discover | New users with little history | Explicit preferences, starter topics, editorial fallback |

Do not use the same ranking recipe for every surface. A homepage feed can optimize for exploration. A checkout recommendation area must optimize for confidence, fit, and low distraction. An admin dashboard should optimize for actionability, not entertainment.

---

## 4. Candidate Sources

Designers should define candidate sources before ranking is discussed.

Recommended source map:

| Source | Purpose | Design notes |
| :--- | :--- | :--- |
| Following or subscribed | Familiarity and trust | Keep a visible path back to known creators, brands, teams, or topics |
| Similarity retrieval | Relevant expansion | Use when the user has enough behavior or an active item context |
| Trending or popular | Shared momentum | Limit dominance so the surface does not become generic |
| Editorial or curated | Quality floor | Useful for new users, sensitive topics, launches, or seasonal collections |
| Recent or fresh | Timeliness | Combine with quality filters so freshness does not reward low-value content |
| Sponsored or promoted | Business model | Separate policy, labeling, brand safety, pacing, and user controls |
| Cold-start fallback | First session usability | Ask lightweight preferences and provide resettable defaults |

Avoid hidden single-source feeds. A good discovery surface blends known, adjacent, fresh, and diverse candidates.

---

## 5. Signals Designers Should Specify

A discover algorithm needs signal design. Every tracked signal should have a product reason, retention rule, and privacy review.

| Signal | What it can mean | Design caution |
| :--- | :--- | :--- |
| Click or tap | Interest, curiosity, or accidental action | Do not over-weight single taps |
| Dwell time | Reading or viewing depth | Account for idle tabs, autoplay, and long media |
| Save or bookmark | Strong future intent | Make saved state easy to undo |
| Like or favorite | Positive preference | May be social signaling, not only personal preference |
| Share | Strong endorsement or utility | Treat private shares differently from public reposts |
| Comment or reply | High effort engagement | May be disagreement, support, or moderation risk |
| Hide or dismiss | Negative preference | Apply quickly and visibly |
| Follow topic or creator | Durable preference | Provide management controls |
| Report | Safety signal | Route to moderation and reduce similar exposure cautiously |
| Purchase or conversion | Business outcome | Avoid turning the feed into only revenue optimization |
| Search query | Active intent | Handle sensitive queries with extra privacy care |

Design rule:

> Prefer explicit controls over guessing when the cost of being wrong is high.

---

## 6. Scoring Model for Product Planning

Designers can use a simple conceptual score before engineering chooses the final implementation:

```text
final_score =
  relevance
  * quality
  * safety_eligibility
  * freshness
  * diversity_adjustment
  * user_control_adjustment
  * business_constraint_adjustment
```

Where:

- `relevance` means the item matches the user's current context or long-term preferences.
- `quality` means the item is complete, useful, available, trustworthy, and well-presented.
- `safety_eligibility` means the item passes policy, privacy, permission, and age checks.
- `freshness` means the item is timely enough for the surface.
- `diversity_adjustment` prevents repeated authors, topics, formats, or price bands from dominating.
- `user_control_adjustment` applies mutes, blocks, hides, follows, and explicit preferences.
- `business_constraint_adjustment` handles availability, inventory, monetization, and contractual rules without overriding safety or user trust.

This model is intentionally simple. It helps designers discuss tradeoffs without pretending the UI file contains the full recommendation system.

---

## 7. Ranking and Blending Rules

A ranked list can still feel bad if it is repetitive, unsafe, or opaque.

Apply blending after scoring:

- Limit repeated creators, brands, sellers, authors, or teams.
- Limit repeated topics in the first viewport.
- Mix familiar and exploratory items.
- Separate sponsored placements with clear labels and frequency caps.
- Avoid placing sensitive or intense content next to unrelated light content.
- Avoid showing too many near-identical thumbnails or headlines.
- Preserve enough novelty for discovery, but keep enough relevance for trust.
- Make the first viewport useful without requiring endless scroll.

For website and app design, the first viewport matters most. It should communicate the surface's promise immediately: useful, fresh, safe, and controllable.

---

## 8. User Controls and Trust Features

Discovery systems need visible correction mechanisms.

Minimum controls:

- Hide this item.
- Show less like this.
- Follow or unfollow topic.
- Mute topic, creator, brand, seller, or author.
- Report item.
- Manage recommendations or personalization.
- Clear recent history where applicable.
- Explain basic recommendation reason in plain language, such as "Because you follow this topic" or "Similar to saved items."

Do not expose private ranking weights, abuse-sensitive thresholds, internal model prompts, moderation internals, or security controls. Explanations should help users understand and steer the product, not teach manipulation.

---

## 9. Privacy and Security Rules

Discovery design must respect security boundaries from the first wireframe.

Mandatory rules:

- Collect only signals needed for the discovery purpose.
- Keep private credentials, model keys, API keys, ranking services, and moderation services server-side.
- Never ship private scoring logic, access-control decisions, or sensitive filters as client-only code.
- Apply authorization before retrieval, hydration, scoring, and rendering.
- Do not rank or display private content unless the viewer is allowed to access it.
- Avoid using sensitive attributes unless there is a lawful, reviewed, user-benefiting reason.
- Separate analytics identifiers from direct personal identity where possible.
- Define retention periods for interaction logs and recommendation traces.
- Add abuse controls for scraping, automation, spam, coordinated manipulation, and fake engagement.
- Label sponsored or promoted content clearly.
- Keep model and ranking logs free of secrets, private content dumps, and unnecessary personal data.
- Provide reporting and moderation paths for user-generated content.

Security principle:

> A recommendation result is still a data access decision. Treat it like one.

---

## 10. Performance and Optimization Rules

Discovery surfaces must feel fast even when ranking is complex.

Design with these constraints:

- Render a useful first viewport quickly.
- Use skeleton states only when they reduce confusion.
- Cache safe, non-private candidate pools where appropriate.
- Precompute expensive embeddings, item quality signals, and availability metadata when possible.
- Hydrate only metadata required for the current page or card state.
- Use pagination, cursor-based loading, or controlled infinite scroll.
- Avoid loading full media before it is near the viewport.
- Track duplicate impressions so the same item does not keep returning.
- Define latency budgets for retrieval, hydration, scoring, ranking, and rendering.
- Provide deterministic fallback modules when personalization is unavailable.

Optimization rule:

> Optimize for perceived relevance and fast correction, not only raw engagement.

---

## 11. AI and LLM-Assisted Discovery

If AI models are used for classification, embeddings, summaries, search expansion, or moderation, add extra controls.

Required safeguards:

- Keep model calls server-side when private data, credentials, or policy decisions are involved.
- Sanitize user-generated content before using it in prompts or logs.
- Treat retrieved content as untrusted input.
- Do not let content text override system, safety, or ranking instructions.
- Store only necessary embeddings and metadata.
- Review generated explanations before showing them in sensitive surfaces.
- Add cost controls, quotas, and timeout behavior.
- Provide non-AI fallback behavior when the model service fails.
- Do not claim certainty when the model is only predicting preference or relevance.

Useful AI-supported tasks:

- Topic classification.
- Duplicate or near-duplicate detection.
- Content quality estimation.
- Safe summary generation.
- Semantic retrieval.
- Similar-item grouping.
- Moderation triage.
- Cold-start preference mapping.

---

## 12. Designer Deliverables

Before implementation, designers should provide:

- Surface type and target user journey.
- Candidate source map.
- First-viewport layout.
- Card metadata requirements.
- Empty, loading, error, and low-confidence states.
- User controls for correction and reporting.
- Explicit preference management flow.
- Sponsored content placement and labeling rules, if applicable.
- Safety and privacy constraints.
- Diversity and repetition rules.
- Cold-start behavior.
- Success metrics and anti-metrics.

Anti-metrics are behaviors the product should avoid optimizing for, such as rage clicks, doom scrolling, unsafe exposure, low-quality viral loops, accidental taps, or revenue at the cost of user trust.

---

## 13. Implementation Handoff Template

Use this template when asking an AI coding assistant or engineering team to build a discovery surface:

```markdown
Build a discovery surface for [product area].

Audience:
- [target users]

Surface type:
- [feed, grid, shelf, search plus discovery, dashboard suggestions, onboarding discover]

Candidate sources:
- [following/subscribed]
- [similarity retrieval]
- [trending/popular]
- [curated/editorial]
- [sponsored/promoted if applicable]
- [cold-start fallback]

Signals:
- Positive: [save, click, dwell, follow, purchase, etc.]
- Negative: [hide, mute, report, skip, etc.]
- Explicit preferences: [topics, categories, brands, creators, etc.]

Filters:
- [blocked, muted, already seen, unavailable, unsafe, private, duplicate, expired, etc.]

Ranking goals:
- Primary: [relevance, task completion, quality, freshness, etc.]
- Diversity: [topic, creator, format, price, category, etc.]
- Business constraints: [inventory, sponsored labels, contractual rules, etc.]

User controls:
- [hide, less like this, mute, follow topic, report, manage recommendations, clear history]

Security and privacy:
- Keep secrets server-side.
- Apply authorization before retrieval and rendering.
- Do not expose private ranking internals or sensitive moderation details.
- Minimize and retain only necessary interaction data.

Performance:
- First viewport target: [latency target]
- Loading pattern: [skeleton, cached fallback, pagination, etc.]
- Media strategy: [lazy loading, thumbnails, responsive sizes]

Success metrics:
- [useful engagement, conversion, saves, completion, retention, satisfaction]

Anti-metrics:
- [spam amplification, repeated content, accidental taps, unsafe exposure, low-quality engagement]
```

---

## 14. Review Checklist

Before shipping a discovery feature, verify:

- The first screen clearly communicates why these items are being shown.
- The surface has at least one familiar source and one safe exploration source.
- Users can correct recommendations without leaving the flow.
- Block, mute, hide, report, and access-control rules are respected.
- Sponsored content is labeled and paced.
- Private data is not exposed in the client, logs, URLs, analytics, or generated explanations.
- The system has a cold-start path for new users.
- The system avoids repeated authors, topics, formats, and near-duplicate items.
- The first viewport loads within the product's performance budget.
- There is a fallback when ranking, retrieval, or AI services fail.
- Metrics include trust and safety signals, not only engagement.
- Documentation avoids claims that require private proof.

---

## 15. Source Notes

Primary reference:

- [xai-org/x-algorithm](https://github.com/xai-org/x-algorithm): public repository describing the X "For You" feed recommendation system.
- [Phoenix README](https://github.com/xai-org/x-algorithm/blob/main/phoenix/README.md): public architecture notes for retrieval and ranking.

Use those references for high-level architecture inspiration only. For your own product, adapt the pipeline to your users, content type, privacy obligations, safety needs, and performance budget.
