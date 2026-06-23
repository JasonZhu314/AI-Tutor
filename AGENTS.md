# AGENTS.md

This repository defines a personal AI Tutor system. It is public-safe infrastructure: templates, documentation, command specifications, and eventually tooling. It must not contain the user's private learner state, course materials, transcripts, or real Obsidian notes.

## Mission

Build a folder-native, Obsidian-connected AI tutor that helps a learner study from local resources such as course folders, textbooks, papers, and code repositories.

The tutor is not an answer machine. It should support active learning, feedback, diagnosis, context management, durable notes, and learner memory.

## Supported Agents

For the personal MVP, support exactly three agents:

```text
Codex = coordinator, filesystem operator, code tutor, note maintainer
Gemini = bounded consultant for broad search, field research, source discovery, and critique
Claude = bounded consultant for deep critique, writing review, pedagogy review, and alternative reasoning
```

Do not design generic multi-provider orchestration until the Codex + Gemini + Claude workflow is stable.

## Core Principles

- Context is working memory, not storage.
- Obsidian is the long-term knowledge IDE.
- Local folders are learning workspaces.
- Raw sources are source of truth.
- Generated wiki pages are useful synthesis, not ground truth.
- Learner memory must be evidence-based and editable.
- The AI should reduce friction, not reduce thinking.
- Every serious session should produce or update a durable learning artifact.

## Privacy Rules

Never commit private learner data. Keep the public repo limited to generic assets.

Do not add:

- real learner profiles;
- real domain profiles;
- real session logs;
- real misconceptions;
- course PDFs, slides, transcripts, or problem sets;
- private Obsidian vault content;
- API keys, tokens, or local machine secrets.

Use synthetic examples only.

## Repository Editing Rules

- Keep changes small and traceable.
- Prefer Markdown templates and specs before implementing complex code.
- Do not add retrieval, databases, web services, or plugin scaffolding until the file-based workflow is validated.
- If adding code, keep the first CLI minimal: scaffold folders, render templates, and print context packets.
- Preserve public/private separation in documentation and examples.

## Documentation Style

- Write direct, practical docs.
- Prefer concrete folder layouts, command examples, and templates.
- Distinguish decisions, open questions, and future work.
- Avoid claiming the system is finished before it has been piloted.

## MVP Direction

First deliverable:

```text
A reusable scaffold that creates AI Tutor files for any learning workspace.
```

Planned commands:

```text
ai-tutor init-global
ai-tutor init-domain <domain>
ai-tutor init-workspace --name <name> --source <path> --domain <domain>
ai-tutor show-context
ai-tutor start-session
ai-tutor close-session
```

The first implementation does not need to call an LLM API.
