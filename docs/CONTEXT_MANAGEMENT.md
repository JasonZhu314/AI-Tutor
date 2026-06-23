# Context Management

## Principle

Context is working memory, not storage.

Do not load the whole vault, course, repo, or paper stack by default. Load indexes first, then pull the smallest source set that supports the current episode.

## Memory Tiers

```text
Hot context
- current prompt, active source excerpts, learner attempt, immediate plan

Warm memory
- episode queue, active concept map, current misconceptions, paper packet

Cold memory
- global learner profile, domain profiles, old session logs, generated wiki

Raw archive
- textbooks, slides, PDFs, transcripts, repos, datasets, papers
```

## Context Packet Template

Use `templates/workspace/Context Packet.md` as the default packet.

A good packet contains:

- goal;
- mode;
- learner state summary;
- source references;
- active excerpts;
- task constraints;
- desired output;
- memory update target.

## Failure Modes

Avoid:

- long prompt soup;
- summary drift;
- context pollution;
- provenance loss;
- over-compression;
- duplicate memory updates;
- key information buried in the middle of long context.

## Session Rule

At the end of a session, do not rely on chat history. Update durable files.
