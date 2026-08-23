---
name: generate-daily-plan-html
description: Generate or update a standalone Chinese daily execution-plan HTML with a fixed visual format, Gantt chart, milestones, daily acceptance criteria, phase filters, local progress tracking, and JSON import/export. Use when the user asks to turn current conversation conclusions, project materials, goals, deadlines, or an existing overall plan into a 每日计划、执行计划、排期、甘特图 or HTML tracker matching the bundled format. Keep format and interactions stable while regenerating all project-specific content from the latest evidence. Do not use for ordinary prose schedules, calendars, or unrelated websites.
---

# Generate Daily Plan HTML

Create one self-contained HTML file from the latest conversation and supplied materials.

## Required workflow

1. Read all user-designated source materials in the stated order.
2. Inspect any existing overall plan or specialist plan that constrains dates, workload, milestones, or priorities.
3. Summarize the real current state before scheduling:
   - completed and reusable work;
   - work that must be redone;
   - missing deliverables;
   - deadlines, time budget, hardware, dependencies, and risks.
4. Resolve material contradictions with the user before authoring. Make reasonable assumptions only when they do not change the project outcome.
5. Read [references/content-contract.md](references/content-contract.md).
6. Copy [assets/daily-plan-template.html](assets/daily-plan-template.html) to the requested output location.
7. Preserve the template's layout, styling, responsive behavior, filters, checkboxes, progress summary, Gantt chart, local storage, and JSON import/export.
8. Replace every project-specific fact with content grounded in the current task. Never carry thesis-specific facts, dates, hardware, model names, outcomes, or risks into an unrelated plan.
9. Update the local-storage key and export format so separate plans never overwrite one another.
10. Validate the completed file before delivery.

## Fixed format

Keep these sections, in this order:

1. Hero title, subtitle, date filter, reset, export, and import controls.
2. Dark final-deliverables panel with exactly three outcome cards and one execution pledge.
3. Four-card plan baseline/evidence panel.
4. Phase milestones.
5. Completion summary and progress bars.
6. Full-period Gantt chart.
7. Filterable daily main-task list.
8. Three fixed execution-rule cards.

Keep one main task per calendar day unless the user explicitly requests another rhythm. Each daily task must contain date, phase, title, concrete action, acceptance/output, slot, and estimated hours.

## Dynamic content rules

- Treat the latest user-approved conclusions as authoritative.
- Derive tasks from actual gaps and dependencies, not generic learning lists.
- Put prerequisite and uncertainty-reduction work before implementation or writing.
- Give every milestone a tangible artifact.
- Make daily work small enough for the stated time budget.
- Reserve time for integration, reruns, review, and final packaging.
- Include explicit fallback rules for material risks such as compute, missing data, external review, or long-running experiments.
- Do not mark tasks completed automatically.
- Do not claim unverified results in plan copy.

## Validation

Before delivery, verify:

- start and end dates match the request;
- every calendar date in the range appears exactly once;
- phases are continuous, non-overlapping, and cover the full range;
- task dates and phase ranges agree;
- milestone dates fall within the plan;
- JavaScript passes a syntax check;
- HTML is self-contained and opens without external dependencies;
- local-storage and export identifiers are unique to the plan;
- the output filename is descriptive and ends in `.html`.

Deliver a clickable absolute file link and briefly state the date range, task count, and phase count.
