# Engineering Guidelines

These are team coding standards applied during code review, independent of
any specific linter or formatter configuration.

## Function design

- Each function must focus on a single capability (single responsibility).
  A function that validates input, performs a database write, and formats
  a response is doing three things — split it into three functions.
- If a function's name needs "and" to describe what it does (e.g.
  `validate_and_save`), it is very likely doing too much and should be split.
- Prefer functions under ~20-30 lines. Longer functions are acceptable only
  when the extra length comes from necessary branching for a single concern,
  not from mixing unrelated responsibilities.
- Side effects (I/O, database writes, network calls) should be isolated from
  pure logic (calculations, transformations, validation) wherever practical,
  so the pure logic can be tested without mocking I/O.

## Review expectations

When reviewing a pull request, flag functions that:
- Mix data access with business logic with response formatting.
- Could be described with multiple distinct verbs (e.g. "parses, validates,
  and persists").
- Duplicate logic that already exists elsewhere in the codebase instead of
  extracting a shared helper.
