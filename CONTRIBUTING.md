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

## Pull Request Checklist

- [ ] The change is sanitized for public release.
- [ ] File names and links are correct.
- [ ] The README remains understandable to a first-time visitor.
- [ ] Token-saving guidance still preserves technical accuracy.
- [ ] Security-sensitive guidance is not weakened.
