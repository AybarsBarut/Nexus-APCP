# Nexus-APCP Release Process

Use this process when preparing a public Nexus-APCP release.

## Version Policy

Nexus-APCP uses SemVer for the public protocol kit:

- `MAJOR`: breaking changes to protocol file names, required setup flow, generated bundle format, or public safety rules.
- `MINOR`: new profiles, protocols, examples, validation checks, or backward-compatible workflow additions.
- `PATCH`: wording fixes, metadata corrections, link fixes, validation hardening, and non-breaking script fixes.

## Release Checklist

1. Update `CHANGELOG.md` under a dated version heading.
2. Update `codemeta.json`:
   - `version`
   - `dateModified`
   - keywords and description if public positioning changed
3. Update `CITATION.cff`:
   - `version`
   - `date-released`
4. Confirm `.github/repository-metadata.yml` and `docs/SEO_CHECKLIST.md` still match README positioning.
5. Run:

```bash
python scripts/apcp-gather.py --caveman
python -m py_compile scripts/apcp_core_files.py scripts/apcp-gather.py scripts/apcp-install.py scripts/validate-repo.py
python -m unittest discover -s tests
python scripts/validate-repo.py
```

6. Confirm `PROMPT_READY.txt` is not tracked and is removed after validation.
7. Create an annotated Git tag only after validation passes.
8. Publish GitHub Release notes from `CHANGELOG.md`.

## Pre-CLI Rule

Do not describe Nexus-APCP as an installable CLI until the repository includes packaging metadata, entry points, release artifacts, and CLI-specific tests.
