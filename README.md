# Codex Skills

Personal reusable skills for ChatGPT and Codex.

## Skills

- `generate-daily-plan-html`: Generates a standalone Chinese daily execution-plan HTML with a fixed visual format, Gantt chart, milestones, acceptance criteria, filters, and local progress import/export.
- `test-case-generate`: Generates one Chinese APP XMind test-case file from requirement documents, screenshots, folders, and accessible authenticated web pages.

## Structure

Each skill is stored in its own folder under `skills/` and contains an independent `SKILL.md` plus any required assets, references, scripts, or UI metadata.

## Install a skill locally

Copy the required skill folder into a Codex user skill location. For example:

```text
$HOME/.agents/skills/generate-daily-plan-html/
```

Restart Codex if a newly installed skill does not appear.
