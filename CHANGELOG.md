# Changelog

All notable changes to the Vibe Coding Playbook are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [Unreleased]

## [0.3.0] - 2026-03-27

### Added

- Origin story section in README explaining the 10-LLM survey methodology
- `CONTRIBUTING.md` standalone contribution guide
- `CHANGELOG.md` for this playbook (this file)
- `CHANGELOG.md` stub added to `starter-template/`
- Prev/next navigation footers on all 11 guide sections
- `opencode-ignore` plugin setup instructions in section 03
- `docs/SESSION.md` pattern added to section 04 per-session checklist

### Fixed

- Broken code fence in section 02 (`AGENTS.md` example)
- `YOUR_USERNAME` placeholder URLs replaced with real repo URL (`plamen5rov`)
- Incorrect "Terminal-only" IDE claim for Claude Code in section 05
- Removed incorrect "ChatGPT Plus subscription" billing claim for Claude Code
- Broken cross-links in sections 08 and 09 (`../` prefix removed)
- Stale model names and speculative pricing in section 10

### Changed

- Section 00 duplicate quick-start block replaced with link to README
- Section 01 "10 AI models surveyed" line now links to origin story
- Section 06 community templates table now includes Notes column
- Section 10 pricing replaced with disclaimer + general guidance
- README starter-template file tree updated to include `CHANGELOG.md`
- README project structure updated to include `ai_answers/`, `FAQ.md`, `CHANGELOG.md`
- README "How to Contribute" section condensed to point to `CONTRIBUTING.md`

## [0.2.0] - 2026-03-26

### Added

- Sections 00, 07, 08, 09, 10 (what is vibe coding, prompt engineering,
  debugging, project types, cost and models)
- Header images for sections 01–06
- Custom `/push` OpenCode command
- "Common mistakes" section in section 03
- Local models guide expanded in section 04
- Icons added to README guide section

### Fixed

- Image paths corrected to use `../pictures/` for sections

## [0.1.0] - 2026-03-20

### Added

- Initial 6 guide sections (01–06) synthesized from 10-LLM survey
- `starter-template/` with 5 template files
- `FAQ.md` — original questions submitted to 10 LLMs
- `ai_answers/` — raw responses from all 10 models
- `.markdownlint.json` configuration
- `.opencode/` config directory
