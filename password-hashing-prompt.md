# Password Hashing — AI Prompt Guide

> **Purpose:** A structured reference prompt to give AI assistants when asking for help with password hashing. Copy the relevant sections into your conversation to get accurate, secure, and scalable advice.

---

## 1. Context Block — Paste This First

```
You are a security-focused backend engineer assistant.
I am building a system that stores user passwords.
All advice must be production-safe, scalable, and follow current best practices (OWASP, NIST SP 800-63B).
Never suggest MD5, SHA-1, or unsalted hashes for new password storage.
Always explain trade-offs between security and performance.
```

---

## 2. Algorithm Selection Prompt

Use this when you need help choosing the right hashing algorithm.

```
Help me choose a password hashing algorithm for my project.

Context:
- Expected concurrent users: [e.g. 10,000 / 1M+]
- Server hardware: [e.g. 2-core VPS / 32-core dedicated]
- Language/framework: [e.g. Node.js, Python Django, Java Spring]
- Are users migrating from a legacy system? [yes/no — if yes, specify current scheme]

Requirements:
- Must be resistant to GPU/ASIC brute force
- Must support a configurable work factor for future scaling
- Must include per-user salt (no global pepper unless I specify)

Compare the following and recommend one with justification:
- bcrypt
- Argon2id
- PBKDF2-HMAC-SHA256
- scrypt
```

---

## 3. Algorithm Reference Table

| Algorithm | Type | Designed To Be Slow | Salt | Work Factor | Use Case |
|---|---|---|---|---|---|
| **Argon2id** | Memory-hard | ✅ Yes | ✅ Auto | Iterations + Memory + Parallelism | ✅ Best choice for new systems |
| **bcrypt** | CPU-hard | ✅ Yes | ✅ Auto | Cost factor (2^n) | ✅ Strong default; widely supported |
| **PBKDF2-HMAC-SHA256** | CPU-iterative | ✅ Yes | ✅ Required | Iteration count | ✅ FIPS-compliant environments |
| **PBKDF2-HMAC-SHA512** | CPU-iterative | ✅ Yes | ✅ Required | Iteration count | ✅ Higher entropy variant |
| **scrypt** | Memory-hard | ✅ Yes | ✅ Required | N, r, p params | ⚠️ Good but complex to tune |
| **phpass MD5** | Fast (iterative) | ❌ No | ✅ | Factor | ⛔ Legacy only — migrate away |
| **phpass SHA-512** | Fast (iterative) | ❌ No | ✅ | Factor | ⛔ Legacy only — migrate away |
| **Salted MD5** | Fast | ❌ No | ✅ Required | Iteration count | ⛔ Migration only — do not use |
| **Salted SHA-256** | Fast | ❌ No | ✅ Required | Iteration count | ⛔ Migration only — do not use |
| **Salted HMAC-SHA256** | Fast | ❌ No | ✅ Required | None | ⛔ Migration only — do not use |

---

## 4. Recommended Work Factors (2025 Baseline)

> ⚠️ These are minimums. Set as high as your login latency budget allows (target: 200–500ms per hash).

| Algorithm | Minimum | Recommended | Notes |
|---|---|---|---|
| **bcrypt** | cost=10 | cost=12 | Each +1 doubles work. cost=13 is ~2× slower than 12. |
| **Argon2id** | m=19456, t=2, p=1 | m=64MB, t=3, p=4 | Tune memory first, then iterations |
| **PBKDF2-HMAC-SHA256** | 310,000 | 600,000 | OWASP 2023 recommendation |
| **PBKDF2-HMAC-SHA512** | 120,000 | 260,000 | Lower count needed; SHA-512 is slower |
| **scrypt** | N=32768, r=8, p=1 | N=65536, r=8, p=2 | Memory-intensive; test under load |

---

## 5. Implementation Prompt (per language)

Replace `[ALGORITHM]` and `[LANGUAGE]` with your choices.

```
Write a production-ready password hashing utility in [LANGUAGE] using [ALGORITHM].

Requirements:
1. Hash a plaintext password and return the encoded hash string.
2. Verify a plaintext password against a stored hash.
3. Detect when a stored hash uses outdated parameters and re-hash on successful login.
4. Never log plaintext passwords or raw hash bytes.
5. Use the library's built-in salt generation — do not generate salt manually.
6. Include inline comments explaining each security decision.
7. Add a helper that benchmarks hash time on the current machine and suggests a work factor.

Show example usage and explain how to store the resulting string in a database (column type, length).
```

---

## 6. Migration Prompt (Legacy → Modern)

Use this when upgrading from MD5, SHA-1, SHA-256, phpass, or similar.

```
I need to migrate users from [CURRENT_SCHEME] to [TARGET_SCHEME] without forcing a password reset.

Current storage format: [describe the field — e.g. "$P$B..." for phpass, hex string for salted SHA-256]
Current factor/iterations: [if known]
Database: [e.g. PostgreSQL, MySQL]

Provide:
1. A migration strategy using "hash-on-login" (rehash when the user successfully authenticates).
2. A schema change to store both the algorithm identifier and the hash (e.g. a separate `hash_scheme` column or a prefixed string).
3. A query or code snippet to identify users still on the old scheme so I can track migration progress.
4. How to handle users who never log in — should I force a reset after [N] months?
5. A rollback plan in case the new scheme causes performance issues.
```

---

## 7. Scalability & Performance Prompt

```
My application is expected to handle [N] logins per second at peak.
Each login requires one password hash verification using [ALGORITHM] at work factor [X].

Help me:
1. Calculate the minimum CPU cores needed to sustain this throughput without latency spikes.
2. Identify if offloading hashing to a dedicated worker/queue makes sense for my scale.
3. Recommend caching strategies that are safe (e.g. session tokens after initial auth — not the hash itself).
4. Explain how to autoscale hashing workers in [Kubernetes / AWS ECS / bare metal].
5. Warn me about anti-patterns: e.g. hashing inside a database stored procedure, or synchronous hashing in an event loop.
```

---

## 8. Audit & Security Review Prompt

```
Review the following password hashing implementation for security issues.
Check for:
- Weak or deprecated algorithm choice
- Insufficient work factor for current hardware
- Improper salt handling (reuse, global salt, too short)
- Timing side-channels in comparison logic (use constant-time compare)
- Logging of sensitive data
- Missing rehash-on-login for upgrading parameters over time
- Hard-coded secrets or credentials

[PASTE YOUR CODE HERE]

Provide a severity rating (Critical / High / Medium / Low) for each issue found, with a specific fix.
```

---

## 9. Common Anti-Patterns to Always Avoid

Paste this block into any conversation as a constraint:

```
Hard rules — never violate these:
- Never store plaintext passwords, even temporarily.
- Never use MD5 or SHA-1 for password hashing (they are fast — that's the problem).
- Never use a global salt (pepper) as the *only* salt — each password must have a unique salt.
- Never compare hashes with == or !== — always use a constant-time comparison function.
- Never log the plaintext password, the raw hash bytes, or the salt separately.
- Never invent a custom hashing scheme — use a well-audited library.
- Never cache the password hash in memory longer than the request lifecycle.
- Never skip the rehash step when work factors are upgraded.
```

---

## 10. Quick Decision Tree

```
Is this a NEW system?
├── Yes → Use Argon2id (preferred) or bcrypt (widely supported)
└── No (migration) →
    ├── Can you force a password reset? → Migrate immediately, no compatibility needed
    └── No reset possible →
        ├── Store algorithm identifier per user
        ├── Rehash on successful login to the new algorithm
        └── Report migration % until legacy scheme users drop below threshold

Is FIPS 140-2/3 compliance required?
└── Yes → Use PBKDF2-HMAC-SHA256 (≥310,000 iterations) — Argon2/bcrypt are not FIPS-approved

Is login latency under 100ms critical?
└── Yes → Lower work factor + horizontal scaling is safer than sacrificing the algorithm
```

---

## 11. Pseudocode Reference (Algorithm Internals)

These pseudocode snippets help AI tools identify whether a legacy scheme matches a known algorithm during import or migration analysis.

### bcrypt
```
hash(password, salt, factor):
  // salt encoded with bcrypt's custom base64 alphabet [./A-Za-z0-9]
  result = bcrypt(bytes(password), base64Decode(salt), factor, bcryptIV)
  return base64Encode(result[0 .. len(bcryptIV)*4 - 1])
```

### PBKDF2-HMAC-SHA256
```
hash(password, salt, factor):
  return base64Encode(pbkdf2Sha256(password, base64Decode(salt), factor, keyLength=256))
```

### PBKDF2-HMAC-SHA512
```
hash(password, salt, factor):
  return base64Encode(pbkdf2Sha512(password, base64Decode(salt), factor, keyLength=512))
```

### phpass MD5 (legacy — migration only)
```
hash(password, salt, factor):
  result = md5(concat(bytes(salt), bytes(password)))
  repeat factor times: result = md5(concat(result, bytes(password)))
  return base64Encode(result[0..15])
```

### Salted SHA-256 (legacy — migration only)
```
hash(password, salt, factor):
  result = concat(bytes(password), base64Decode(salt))
  repeat factor times: result = sha256(result)
  return result
```

---

## References

- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [NIST SP 800-63B — Digital Identity Guidelines](https://pages.nist.gov/800-63-3/sp800-63b.html)
- [FusionAuth Password Hashing Algorithm Reference](https://fusionauth.io/docs/reference/password-hashes)
- [Argon2 RFC 9106](https://www.rfc-editor.org/rfc/rfc9106)
- [HaveIBeenPwned — Pwned Passwords API](https://haveibeenpwned.com/API/v3#PwnedPasswords)
