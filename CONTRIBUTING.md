# Contributing to Nexus-APCP

Thanks for improving Nexus-APCP. This repository is a protocol kit, so contributions should make AI-assisted development safer, clearer, or easier to repeat.

## Good Contributions

- Clearer setup instructions.
- Better prompt templates for real developer workflows.
- Safer `.gitignore` patterns for specific domains.
- More precise delivery gates for web, backend, AI/LLM, game, mobile, DevOps, or security projects.
- Improvements to token efficiency that do not remove technical meaning.
- Fixes for outdated file names, broken links, or confusing terminology.

## Contribution Guidelines

1. Keep public templates sanitized. Do not commit filled private project context, internal architecture maps, secrets, credentials, customer data, private prompts, or security runbooks.
2. Keep terminology consistent: use `Nexus-APCP` and `AI Project Context Protocol`.
3. Prefer specific examples over vague process language.
4. Update README links or metadata when adding new public-facing files.
5. Run the context gatherer before submitting major protocol changes:

```bash
python scripts/apcp-gather.py --caveman
```

6. Run repository validation before opening a pull request:

```bash
python scripts/validate-repo.py
```

7. Follow the pull request title rules in [`.github/pull_request_title_conventions.md`](./.github/pull_request_title_conventions.md).

## Pull Request Checklist

- [ ] The change is sanitized for public release.
- [ ] File names and links are correct.
- [ ] The README remains understandable to a first-time visitor.
- [ ] Token-saving guidance still preserves technical accuracy.
- [ ] Security-sensitive guidance is not weakened.
- [ ] `python scripts/validate-repo.py` passes.

---

## Emoji Usage Policy

Nexus-APCP forbids emoji usage across repository content and AI-generated output. The rule keeps documentation, prompts, code, logs, examples, metadata, and generated context bundles consistent, professional, accessible, and easy to search.

### Scope
Applies to all repo-facing artifacts: READMEs, code, scripts, YAML/JSON, PR titles, and AI assistant responses.

### Rule
Do not use emoji. Use plain words, ASCII labels, or existing icon components instead (e.g. `COMPLETED`, `WARNING`).

### Temporary UI Exception
Emoji may be proposed only as a temporary button icon placeholder when all conditions are true:
- No suitable project-approved icon is available.
- The emoji is only a short-lived replacement marker.
- The AI assistant asks the user first and receives explicit approval.
- The follow-up task records that the placeholder must be replaced.

---

## CAVEMAN PROTOCOL: Advanced Token Compression

**"Maximum Signal. Minimum Noise."**
Caveman Mode bypasses LLM verbosity, reducing API latency and token costs by up to 80% without sacrificing technical precision.

### Activation and Deactivation
- Activate: Run `python scripts/apcp-gather.py --caveman`, add `PROTOCOL: CAVEMAN` to session, or user says "use Caveman Mode".
- Deactivate: User asks for normal detail/teaching mode, or the answer needs legal/security nuance that would be unsafe if over-compressed.

### Standard Operating Procedures (SOP)
1. **Grammatical Stripping**: Drop articles (a, an, the), auxiliary verbs (is, are), pronouns (I, you, we), and politeness.
2. **Structural Compression**: Fragments only. Use `-` or `*` instead of paragraphs. Newlines = logic breaks.
3. **Technical Anchoring**: Use standard industry shorthand (MVP, CI/CD). Use `File.ext` directly. Use plain ASCII status labels (e.g., `DONE`, `FAIL`, `WARN`). Follow the Emoji Policy.
4. **Code vs. Prose**: NEVER compress code blocks. Only describe the change in prose.
