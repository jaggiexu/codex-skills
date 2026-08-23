# Content contract

Use this contract when adapting the bundled HTML template.

## Required plan fields

- `START`, `END`: inclusive ISO dates.
- `KEY`: unique local-storage key containing the project slug and date range.
- Page title, eyebrow, subtitle.
- Three final outcome cards.
- One execution pledge.
- Four plan-baseline cards: existing evidence, required rework, resource strategy, time budget. Adapt labels when the project requires different evidence categories.
- Phases: display name, CSS class, inclusive start and end.
- Milestones: date, short title, inspectable deliverable.
- Daily tasks: date, phase, short title, concrete action, acceptance/output.
- Three execution rules: asset/evidence discipline, risk/fallback discipline, delivery/quality discipline.

## Scheduling rules

1. Calculate the number of inclusive calendar days.
2. Create exactly one dated task per day by default.
3. Allocate hours from user constraints; do not invent unsustainable workload.
4. Order work by dependency:
   - baseline and scope;
   - uncertainty reduction;
   - foundation or data;
   - core implementation;
   - validation and comparison;
   - writing, review, and delivery.
5. Use milestone dates as gates, not decorative labels.
6. If work may run unattended, schedule the launch and the later result review separately.
7. Preserve a final review/packaging window unless the user explicitly rejects it.

## Template adaptation boundaries

Preserve:

- CSS visual system and responsive breakpoints;
- DOM section ordering;
- progress calculation;
- completion checkboxes;
- phase filters;
- Gantt rendering;
- date filtering;
- JSON progress import/export.

Replace:

- all titles and descriptive copy;
- dates and unique keys;
- phase names, ranges, and colors when needed;
- milestones;
- outcomes, facts, rules, and daily tasks;
- export filename and format identifier.

Never leave stale facts from the example template. Search the finished file for old project-specific terms before delivery.

## Acceptance wording

Prefer observable outputs:

- `产出：配置文件 + 运行日志`
- `验收：随机抽查 20 条，均满足时间约束`
- `产出：可交付初稿 + 待确认问题清单`

Avoid vague acceptance language such as `了解`, `学习一下`, `尽量完成`, or `效果不错`.
