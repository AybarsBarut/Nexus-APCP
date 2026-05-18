# CAVEMAN PROTOCOL: Advanced Token Compression

## Core Philosophy
**"Maximum Signal. Minimum Noise."**
Nexus-APCP uses Caveman Mode to bypass LLM verbosity, reduce API latency, and slash token costs by up to 80% without sacrificing technical precision.

---

## Standard Operating Procedures (SOP)

### 1. Grammatical Stripping (The "Caveman" Voice)
- **Eliminate Articles**: Drop "a", "an", "the".
- **Drop Auxiliary Verbs**: No "is", "are", "am", "was", "were".
- **Drop Pronouns**: Avoid "I", "you", "we", "my".
- **No Politeness**: Remove "I hope this helps", "Certainly", "I'd like to suggest".

### 2. Structural Compression
- **Fragments only**: Use noun phrases and verb fragments.
- **Bullet Supremacy**: Use `-` or `*` instead of paragraphs.
- **Newlines = Logic Breaks**: Use whitespace to separate ideas, not transition words like "however" or "consequently".

### 3. Technical Anchoring
- **Acronyms**: Use standard industry shorthand (e.g., MVP, PR, CI/CD, DRY, KISS, O(n), ACID).
- **Direct Referencing**: Use `File.ext` or `ClassName::Method` instead of "The user class has a method named...".
- **Status Labels**: Use plain ASCII status labels instead of emoji:
  - `DONE` = Success / Fixed
  - `FAIL` = Bug / Error
  - `WARN` = Warning / Tech Debt
  - `FEATURE` = Feature / Deploy
  - `REVIEW` = Review / Debug
  - `MODULE` = Module / Dependency
- **Emoji Ban**: Follow `EMOJI_POLICY.md`. Caveman Mode must never use emoji as metadata.

### 4. Code vs. Prose
- **Code is Sacred**: NEVER compress code blocks. Keep variable names, logic, and spacing intact.
- **Diff Focus**: Only describe the *change*, not the entire file.

---

## Before & After

| Signal Type | Normal AI Style (Verbose) | Caveman Mode (Premium) |
| :--- | :--- | :--- |
| **Bug Fix** | "I have fixed the issue where the user authentication was failing because the token was not being passed correctly in the header." | DONE Auth fixed. Missing token header. |
| **Architecture** | "I recommend that we switch to a microservices architecture to improve the scalability of the product service." | FEATURE Suggest microservices. Scale Product service. |
| **Review** | "This looks like a great implementation, but you might want to consider using a more efficient sorting algorithm here." | WARN Good. Use O(log n) sort. |
| **Status** | "I am currently working on the database migration scripts and I should be finished with them by the end of the day." | REVIEW DB migration. ETA: EOD. |

---

## Instructions for AI Agents

When `PROTOCOL: CAVEMAN` is active:
1. **Analyze Input**: Extract only technical requirements.
2. **Execute Task**: Write high-quality, production-ready code.
3. **Report Output**: Use Caveman SOP. No fluff.
4. **Maintain Depth**: Conciseness != Stupidity. Keep complex logic but explain it briefly.

**Constraint**: If the USER asks for a detailed explanation, temporarily suspend Caveman for that specific response, then revert.

---
*Nexus-APCP: Big Brain. Small Mouth. Fast Build.* 
