# Code Review & Static Analysis Setup

This repo is configured for two parallel review layers so you can compare
traditional static analysis against AI-powered code review:

1. **Static analysis (deterministic)** — GitHub Actions workflow
   (`.github/workflows/static-analysis.yml`) running on every PR/push to `main`:
   - **bandit** — SAST scan of `producer/` (hardcoded secrets, insecure patterns).
   - **pip-audit** — SCA scan of `producer/requirements.txt` (known CVEs in pinned deps).
   Both upload their reports as workflow artifacts and fail the build on findings.

2. **AI code review** — CodeRabbit, configured via `.coderabbit.yaml` at the repo
   root. Runs automatically on PRs once the GitHub App is installed (see below).

## Manual steps required (GitHub-side, not done by the agent)

These require your GitHub account access and were intentionally left for you:

1. **Push these files to GitHub:**
   ```bash
   git add .github/workflows/static-analysis.yml .coderabbit.yaml SETUP.md
   git commit -m "Add static analysis CI and CodeRabbit config"
   git push origin main
   ```

2. **Confirm GitHub Actions is enabled** for the repo:
   `Settings → Actions → General → Allow all actions and reusable workflows`.

3. **Install the CodeRabbit GitHub App:**
   - Go to https://github.com/apps/coderabbitai
   - Click "Install", select `EsTelite/ssh-failed-attempt` (or all repos).
   - Authorize. CodeRabbit will auto-review new PRs going forward.

4. **(Optional) Branch protection:** `Settings → Branches → Add rule` for `main`,
   require the `SAST (bandit)` and `SCA (pip-audit)` status checks to pass before
   merging, and optionally require CodeRabbit's review to resolve before merge.

## How to use this for the learning exercise

1. Open a PR with a small code change (e.g., touch `producer/dbconn.py` or
   `producer/models.py`).
2. Compare the three outputs on that same PR:
   - bandit findings (deterministic, rule-based)
   - pip-audit findings (known CVEs in dependencies)
   - CodeRabbit's review comment (contextual/intent-based reasoning)
3. Note what each layer catches that the others miss. For example, bandit/pip-audit
   won't catch the shared mutable `FailedAttempts` singleton in `models.py` (a logic/
   concurrency issue) — that's the kind of thing to watch for in CodeRabbit's output
   instead, since it reasons about intent and surrounding context rather than
   matching fixed rules.
