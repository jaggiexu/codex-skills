---
name: test-case-generate
description: Generate one Chinese APP XMind test-case file from all requirement materials supplied in a single invocation, including screenshots, images, Markdown, Word, PDF, Excel, folders, and accessible authenticated web pages. Use when the user explicitly invokes $test-case-generate or Test_CaseGenerate and supplies requirement materials; treat every supplied item as one requirement, start immediately without asking for an extra generation command, separate core, derived, and pending-confirmation cases, and keep memory isolated per project.
---

# Test_CaseGenerate

Generate exactly one XMind test-case artifact per invocation from all materials in the invoking user message. Start immediately. Do not ask the user to repeat “generate test cases”, identify that files belong together, choose APP, or choose XMind.

## Fixed defaults

- Treat all attachments, referenced files, folders, screenshots, and links in the invocation as one requirement.
- Generate Chinese APP cases. Use `APP` unless the requirement explicitly distinguishes Android or iOS.
- Produce one `.xmind` file under `<project>/test-docs/`.
- Name it `<requirement-id>_testcases_<YYYYmmddHHMMSS>.xmind`; use `Test_CaseGenerate_testcases_<timestamp>.xmind` when no ID is available.
- Store project memory under `<project>/.test-case-memory/`; never store inputs, outputs, or memory inside this installed skill.
- Do not pause for ordinary ambiguity. Generate the affected case with a pending-confirmation expected result and an `rc:` note.

## Required workflow

1. Locate the current project root. Inventory every supplied source and record its path or URL.
2. Read [INPUT-RULES.md](references/INPUT-RULES.md), then extract text, tables, images, diagrams, visible UI elements, and accessible linked-page content. Use the appropriate installed document, PDF, spreadsheet, image, or browser capability when required.
3. Load or initialize `.test-case-memory/` with `scripts/memory_manager.py`. Apply terminology and preferences only from this project.
4. Parse modules, explicit rules, acceptance criteria, flows, boundaries, platform statements, and requirement IDs. Read [PARSING-RULES.md](references/PARSING-RULES.md) as needed.
5. Design cases with EP, BVA, ST, and EG according to [TEST-DESIGN-METHODS.md](references/TEST-DESIGN-METHODS.md). Read [APP-TESTING-RULES.md](references/APP-TESTING-RULES.md) for APP-specific derivations and [BUSINESS-RULES.md](references/BUSINESS-RULES.md) for applicable derived checks.
6. Classify every case:
   - `核心用例`: directly supported by requirement text, acceptance criteria, visible screenshot content, or explicit flow/rule.
   - `衍生用例`: logically derived boundaries, negative classes, error guesses, APP risks, or applicable business rules. Never present an unstated behavior as confirmed.
   - `待确认`: an operation can be tested but its expected behavior, value, wording, or condition is absent or ambiguous.
7. Deduplicate by verification objective, while never merging distinct requirement IDs or platform-specific behavior.
8. Build a JSON array matching `assets/case-schema.json`. Prefix every module path with its class, for example `["核心用例", "登录", "手机号"]`.
9. For pending cases, set the expected result to `待确认：需求未说明……` and add `备注` beginning with `待确认：`.
10. Run `scripts/validate_cases.py` before generation. Fix every error; report warnings without blocking.
11. Run `scripts/generate_xmind.py` to create the single XMind file. Verify that it is a readable ZIP containing `content.xml` and that at least one test-case node exists.
12. Add a generation record to project memory. Return the output link plus counts for core, derived, and pending cases and a compact pending-confirmation list.

## Case requirements

- Use fields: `模块`, `用例标题`, `优先级`, `需求ID`, `设计方法`, optional `前置条件`, `步骤`, `标签`, optional `备注`.
- Write titles as action + object + condition/scenario; avoid “正常” and “正确”.
- Give each step one action. Number operations and matching expected results from 1 with equal array length.
- Mark at least one design method: `EP`, `BVA`, `ST`, or `EG`.
- Keep core cases strictly traceable. Derived cases may extend coverage but must stay under `衍生用例` and avoid invented exact behavior.
- Treat visible screenshot elements and text as explicit evidence; do not infer hidden backend rules from appearance.
- Do not duplicate identical APP cases for Android and iOS. Split only when the requirement states or evidence shows platform differences.
- Use priority rules as guidance, not quotas. Do not manufacture cases to reach a percentage.

## Stop conditions

Pause only when no material was supplied, all material is unreadable, authenticated content cannot be accessed, no valid requirement can be identified, or the output location is not writable. Otherwise continue and mark uncertainty as pending confirmation.
