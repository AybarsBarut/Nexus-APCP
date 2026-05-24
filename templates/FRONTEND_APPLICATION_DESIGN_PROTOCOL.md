# Frontend Application Design Protocol
## AI-ready rules for building polished, usable, and maintainable application frontends

Version: 1.0
Owner: Product, design, engineering, and AI assistants
Status: Reference protocol for websites, dashboards, SaaS tools, internal tools, mobile-responsive web apps, AI-assisted interfaces, and frontend refactors.
Scope: Public-safe frontend planning, UI generation, implementation checks, design-system consistency, accessibility, performance, and responsive verification.

---

## 0. Purpose

This protocol helps AI coding assistants design and implement better frontend experiences instead of producing generic screens.

Use it when a task includes:

- Building a new website, web app, dashboard, admin panel, landing page, form, editor, marketplace, profile, content surface, or design system.
- Improving the visual quality of an existing frontend.
- Translating a product idea into an interface.
- Making an AI-generated UI feel coherent, intentional, and production-ready.
- Choosing a frontend learning or implementation path for a project.

The goal is not decoration. The goal is useful software that looks deliberate, works across devices, communicates hierarchy clearly, and respects the underlying web platform.

---

## 1. Source Synthesis

This protocol synthesizes public frontend learning and design-prompt patterns from:

- [Front-end Developer Handbook 2019](https://frontendmasters.com/guides/front-end-handbook/2019/), which frames frontend work around HTML, CSS, JavaScript, DOM, browser behavior, tooling, and the importance of learning foundations before abstractions.
- [roadmap.sh Frontend Developer Roadmap](https://roadmap.sh/pdfs/roadmaps/frontend.pdf), which maps the field across internet fundamentals, semantic HTML, accessibility, CSS layout, responsive design, JavaScript, frameworks, build tools, testing, security, performance, browser APIs, and deployment-adjacent skills.
- [Front-End Web Development: The Big Nerd Ranch Guide](https://www.academia.edu/40448728/Front_end_developer_book_big_nerd_ranch), used only as a high-level public reference for project-based browser learning, developer tooling, forms, validation, DOM updates, asynchronous data, modules, and application architecture. Do not copy protected book text, exercises, examples, or project content.
- [Design Prompts](https://www.designprompts.dev/), treated as an inspiration model for style exploration: the same product data can be rendered through many visual systems when prompts specify layout, typography, color, spacing, component behavior, and interaction tone.

The resulting rules are original, condensed, and safe for public repository use.

---

## 2. Frontend Mental Model

A frontend is the product surface where structure, behavior, content, and visual judgment meet.

Use this model before writing UI code:

```text
User intent
-> information architecture
-> interaction flow
-> semantic structure
-> responsive layout
-> visual hierarchy
-> component states
-> accessibility
-> performance
-> browser verification
```

Each stage should have a visible implementation outcome:

| Stage | Designer question | Implementation outcome |
| :--- | :--- | :--- |
| User intent | Why is the user here now? | Primary task, default screen, empty state, success path |
| Information architecture | What must be understood first? | Navigation, headings, grouping, page regions |
| Interaction flow | What can the user do next? | Buttons, forms, menus, keyboard paths, error recovery |
| Semantic structure | Does the markup describe the content? | Landmarks, headings, labels, lists, buttons, forms |
| Responsive layout | Does it work from phone to wide desktop? | Fluid grids, breakpoints, stable dimensions, non-overlap |
| Visual hierarchy | Where should the eye go first? | Type scale, contrast, spacing, weight, position |
| Component states | What happens before, during, and after action? | Loading, hover, focus, active, disabled, empty, error, success |
| Accessibility | Can more users operate it reliably? | Keyboard support, focus order, contrast, labels, reduced motion |
| Performance | Does it feel fast and stay fast? | Image handling, code splitting, bundle discipline, metrics |
| Browser verification | Did the actual UI render as intended? | Screenshot checks, interaction tests, responsive QA |

---

## 3. Foundational Skill Order

AI assistants should prefer foundation-aware frontend work. Do not hide weak UI decisions behind a framework or component library.

Recommended order:

1. Understand the product goal, user type, data shape, and primary workflow.
2. Define semantic HTML structure and page hierarchy.
3. Design CSS layout with flexbox, grid, responsive constraints, and stable spacing.
4. Add interaction with JavaScript or the project's framework.
5. Use framework and component abstractions only after the underlying UI behavior is clear.
6. Add tooling: package manager, formatter, linter, build tool, test runner, and browser verification.
7. Measure and improve accessibility, performance, and responsive behavior.

Important principle:

```text
Learn and preserve the browser primitives first.
Use abstractions to speed delivery, not to avoid understanding the UI.
```

---

## 4. Design Brief Intake

Before implementing a significant frontend, capture the design brief in compact form.

| Field | Required answer |
| :--- | :--- |
| Product type | SaaS, dashboard, ecommerce, portfolio, editor, game, learning app, content site, internal tool, etc. |
| Primary user | Beginner, expert, admin, creator, buyer, analyst, operator, student, etc. |
| Main task | The one action or decision the screen must support first. |
| Content density | Sparse, moderate, dense, command-center, editorial, immersive, etc. |
| Brand tone | Quiet, premium, technical, playful, clinical, bold, trustworthy, experimental, etc. |
| Device priority | Mobile-first, desktop-first, tablet-heavy, kiosk, embedded webview, etc. |
| Data states | Loading, empty, partial, many items, error, permission denied, success. |
| Visual assets | Product photos, screenshots, illustrations, icons, charts, maps, generated images, none yet. |
| Constraints | Existing design system, library, accessibility target, performance budget, browser support, deadline. |

If the user gives no visual direction, infer one from the product domain. A finance dashboard, developer console, and children's learning app should not share the same visual language.

---

## 5. UI Quality Rules

### 5.1 Layout

- Use layout to explain the product, not merely to fill space.
- Put the primary workflow in the first viewport when building an app or tool.
- Use cards for repeated objects, modals, and genuinely framed tools. Avoid card-inside-card nesting.
- Use full-width sections or unframed layouts for page structure.
- Align related elements on a consistent grid.
- Keep dense tools calm: smaller headings, predictable controls, visible filters, scannable tables, and restrained decoration.
- Give fixed-format UI elements stable dimensions with `min-width`, `max-width`, `aspect-ratio`, grid tracks, or container constraints.

### 5.2 Visual Hierarchy

- Establish one primary focal point per screen.
- Use size, weight, spacing, and contrast before adding decorative effects.
- Do not make every panel visually loud.
- Keep supporting text shorter than the controls and data it supports.
- Reserve hero-scale typography for true hero sections.
- Make status, errors, warnings, and destructive actions visually distinct without relying on color alone.

### 5.3 Typography

- Choose type based on use case: readable sans-serif for apps, serif or editorial pairings for content-led pages, monospace for code and technical data.
- Use a small, consistent type scale.
- Do not scale font size directly with viewport width.
- Set letter spacing to `0` unless a local design system already requires otherwise.
- Prevent text overflow in buttons, cards, tabs, sidebars, and badges.
- Use line length constraints for prose and denser grids for operational data.

### 5.4 Color

- Build a palette with roles: background, surface, border, text, muted text, primary action, secondary action, success, warning, danger, focus.
- Avoid one-note palettes where the whole UI is only variations of one hue family.
- Use neutral surfaces for dense applications and stronger color only for priority, state, and brand moments.
- Verify contrast for text, icons, controls, and focus states.
- Use color tokens or CSS variables so future changes are coherent.

### 5.5 Components

- Prefer familiar controls: icon buttons for common tools, segmented controls for modes, menus for option sets, tabs for peer views, switches for binary settings, sliders or steppers for numeric tuning, and tables or lists for comparison.
- Use icons from the existing project icon library when available.
- Every interactive component needs hover, focus, active, disabled, loading, and error states when relevant.
- Keep button labels action-oriented.
- Do not use decorative controls that look clickable but are not.
- Avoid inventing a new component when a standard pattern would be clearer.

### 5.6 Motion

- Use motion to clarify cause and effect: open, close, reorder, save, transition, feedback.
- Keep durations short for app workflows.
- Respect reduced motion preferences.
- Avoid motion that blocks input, hides state, or makes repeated work tiring.

### 5.7 Assets

- Websites and games should use meaningful visual assets when the subject matter benefits from inspection, mood, product understanding, or gameplay.
- Prefer real product/place/object screenshots or photos when accuracy matters.
- Use generated bitmap images for mood, illustration, backgrounds, textures, mockups, and fictional assets.
- Avoid purely atmospheric images when users need to inspect the actual product.
- Optimize image dimensions, formats, alt text, loading behavior, and layout stability.

---

## 6. Accessibility Rules

Accessibility is a core frontend quality gate, not a final polish task.

Required checks:

- Semantic landmarks and heading order make sense.
- Buttons are buttons, links are links, labels are connected to form controls.
- Keyboard navigation reaches every control in a logical order.
- Focus states are visible.
- Text contrast and non-text contrast are sufficient.
- Forms show inline validation with clear recovery.
- Errors are announced or placed where users can find them.
- Dynamic content updates are not confusing to screen readers.
- Reduced motion is respected.
- Touch targets are usable on mobile.

Do not ship a beautiful UI that cannot be operated.

---

## 7. Performance Rules

Good frontend design includes speed.

Design and implementation should consider:

- Critical content renders quickly.
- Images are sized, compressed, lazy-loaded where appropriate, and do not cause layout shift.
- Fonts are limited and loaded responsibly.
- JavaScript is split by route or feature when the app is large.
- Animations avoid expensive layout work.
- Tables, feeds, and galleries handle large data sets with pagination, virtualization, or progressive loading.
- Network errors, slow loading, and offline or retry states are designed.
- Lighthouse, browser DevTools, or project-specific performance checks are used when the surface is user-facing.

---

## 8. Engineering Rules

Follow the existing project stack and design system first.

When adding or changing frontend code:

- Inspect existing components, tokens, CSS conventions, routing, state management, and test patterns.
- Prefer local conventions over introducing new libraries.
- Add a library only when it materially improves accessibility, domain logic, charting, 3D, forms, tables, maps, dates, or complex interaction.
- Keep CSS scoped and maintainable.
- Use design tokens for spacing, color, border radius, shadows, z-index, typography, and motion.
- Avoid fragile absolute positioning for normal page layout.
- Keep business logic out of presentational components where the codebase already separates concerns.
- Use framework-native patterns for data loading, routing, suspense, error boundaries, and hydration.

---

## 9. AI Frontend Implementation Workflow

AI assistants should use this workflow for frontend tasks:

```text
1. Read project context and existing UI patterns.
2. Identify product type, user, primary task, and device priority.
3. Select or infer a visual direction.
4. Draft the information architecture and component inventory.
5. Implement the smallest complete usable screen or flow.
6. Add all relevant states, not only the happy path.
7. Verify responsive layout at mobile, tablet, and desktop widths.
8. Verify keyboard navigation and focus.
9. Run tests, linting, type checks, and build checks available in the repo.
10. Use browser screenshots or visual inspection for significant UI work.
```

For substantial visual changes, never finish after code compiles. Verify what the browser actually renders.

---

## 10. Design Style Prompt Template

Use this template when asking an AI assistant to design or refactor a frontend.

```text
Design a [product type] frontend for [primary user] whose main task is [main task].

Visual direction:
- Tone: [quiet, premium, technical, playful, editorial, utilitarian, etc.]
- Style reference: [SaaS operations, Swiss minimal, editorial, luxury, terminal, brutalist, warm human, etc.]
- Density: [sparse, moderate, dense, command-center]
- Device priority: [mobile-first, desktop-first, responsive parity]

Interface requirements:
- Use semantic HTML and accessible controls.
- Build a clear visual hierarchy with one primary focal point.
- Use a coherent type scale, color roles, spacing system, and component states.
- Include loading, empty, error, success, hover, focus, active, and disabled states where relevant.
- Make the layout responsive without overlap or text clipping.
- Use meaningful visual assets when they improve comprehension.
- Follow the existing project framework, components, and design tokens.
- Verify in the browser across mobile and desktop widths.

Avoid:
- Generic marketing layout when this is an app or tool.
- Nested cards, one-note palettes, text overflow, weak contrast, missing focus states, and decorative UI with no product purpose.
```

---

## 11. Reusable Style Directions

These are compact, original style directions for AI-assisted frontend work. They are not copied from any external prompt library.

| Style | Best for | Direction |
| :--- | :--- | :--- |
| SaaS Operations | Dashboards, CRMs, admin tools | Quiet surfaces, dense but readable grids, restrained borders, clear filters, strong empty states, practical icons, low ornament. |
| Swiss Minimal | Portfolios, documentation, content products | Precise alignment, strong whitespace, clear typography, black-white-neutral base, restrained accent color, grid-first composition. |
| Editorial Product | Publications, creator platforms, story-led products | Strong headlines, generous reading rhythm, image-led modules, article cards, thoughtful captions, elegant section transitions. |
| Technical Console | Developer tools, monitoring, AI systems | Monospace accents, compact metrics, clear status color roles, terminal-inspired details, fast scanning, direct controls. |
| Premium Utility | Finance, legal, healthcare, B2B | Calm contrast, high trust, careful spacing, conservative typography, clear confirmation states, minimal decorative motion. |
| Warm Human | Education, wellness, community, onboarding | Soft but not childish color, friendly illustrations or photos, conversational empty states, larger touch targets, forgiving forms. |
| Bold Launch | Startup landing pages, product announcements | First-viewport product signal, strong headline, real product imagery, focused CTA, visible next-section preview, crisp social proof. |
| Data Studio | Analytics, BI, operations rooms | Dense dashboards, stable chart containers, visible legends, filter bars, comparison tables, export actions, explainable states. |
| Creative Tool | Editors, builders, media tools | Full-bleed workspace, compact toolbars, icon-first controls, inspector panels, non-shifting canvas, keyboard-friendly actions. |
| Commerce Catalog | Marketplaces, ecommerce, booking | Product-first media, comparison filters, trust signals, availability states, clear pricing, quick actions, accessible cards. |

Select one primary direction. Mixing too many styles produces visual noise.

---

## 12. Screen-Type Guidance

### 12.1 Application Dashboard

- Start with the user's current operational question.
- Put filters, date ranges, and primary actions where they are easy to repeat.
- Use charts only when they answer a decision.
- Design empty, loading, stale-data, permission, and export states.
- Keep decorative marketing sections out of the work surface.

### 12.2 Landing Page

- Make the product, brand, person, venue, or offer obvious in the first viewport.
- Use real or generated visual media that reveals the actual subject.
- Keep the hero focused and leave a hint of the next section visible.
- Use supporting copy for value propositions instead of overloading the headline.
- Connect claims to visible evidence, screenshots, testimonials, examples, or workflows.

### 12.3 Forms and Onboarding

- Ask only what is needed now.
- Group fields by decision, not database schema.
- Preserve entered data during errors.
- Show validation near the problem.
- Offer clear back, skip, save, and cancel behavior where appropriate.

### 12.4 Tables and Lists

- Prioritize scan speed.
- Keep columns meaningful and avoid low-value metadata.
- Provide sorting, filtering, pagination, search, bulk actions, and row states when the data set warrants them.
- Use truncation carefully and provide access to full content.
- Make selected, hovered, focused, disabled, and loading rows visually clear.

### 12.5 Editors and Builder Interfaces

- Keep the canvas stable.
- Use icon buttons with tooltips for repeated commands.
- Separate creation tools from object properties.
- Provide undo, redo, save state, zoom, selection, and keyboard support when expected.
- Avoid layout shifts while editing.

---

## 13. Anti-Patterns

Avoid these common AI-generated frontend failures:

- A landing page when the user asked for an app.
- Large decorative hero sections on operational tools.
- Generic gradient backgrounds that do not communicate product value.
- Nested cards and floating sections everywhere.
- Unstable layouts that resize on hover or data load.
- Text inside controls that clips on mobile.
- Icons without accessible names.
- Buttons that look equal even when one action is primary.
- Missing empty, error, loading, and disabled states.
- Tables with no responsive strategy.
- Charts without labels, legends, or interpretation.
- Accessibility left until after visual polish.
- Framework-heavy implementation that ignores HTML, CSS, and browser behavior.

---

## 14. Verification Checklist

Before finishing a frontend task, verify:

- The primary user task is visible and usable.
- The UI follows the existing project patterns.
- The page has a clear hierarchy and no incoherent overlap.
- Text fits inside buttons, cards, tabs, and sidebars.
- Mobile, tablet, and desktop layouts work.
- Keyboard navigation and focus states work.
- Forms have labels and recoverable validation.
- Loading, empty, error, success, disabled, hover, focus, and active states exist where relevant.
- Images and media render, are sized properly, and have appropriate alt text.
- Color contrast is acceptable.
- Performance-sensitive assets and JavaScript are controlled.
- Available lint, type, test, build, and browser checks pass.

---

## 15. Public-Safe Use Rules

- Do not copy protected book text, screenshots, exercises, proprietary prompts, or paid course material into this repository.
- Use source links as references, then write original project-specific guidance.
- Keep examples generic and sanitized.
- Do not include private product strategy, customer data, screenshots, credentials, or unreleased designs.
- Prefer durable frontend principles over tool hype.
- Update this protocol when repository frontend standards change.

