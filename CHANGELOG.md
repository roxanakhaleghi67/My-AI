# Changelog

All notable changes to this project are documented here.

## Unreleased

### Added
- Per-session conversation memory (`ConversationChain` + `ConversationBufferMemory`).
- `GET /health` liveness endpoint that works without an API key.
- Optional `.env` loading through `python-dotenv`.
- `.dockerignore`.

### Fixed
- Docker image now imports the application as a package (`app.main:app`); the startup no longer
  conflicts with the relative imports.
- The model client is created lazily, so importing the app no longer requires `OPENAI_API_KEY`.
- Pinned dependency versions.

### Removed
- The virtual environment, bytecode and the local SQLite database from version control.
