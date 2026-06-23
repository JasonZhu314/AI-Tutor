# AI Tutor

AI Tutor is a personal, folder-native tutoring system for learning from local resources: course folders, textbooks, papers, Obsidian vaults, and code repositories.

The system is designed around Codex as the primary coordinator, with Gemini and Claude as occasional consultants.

## Status

Design and scaffold phase. The first implementation target is a file-based workflow that creates templates and context packets. It does not need to call an LLM API yet.

## Why This Exists

Static tutorials have one path. A human tutor adapts by diagnosing the learner, adjusting pace, choosing the next challenge, and remembering what happened.

AI Tutor aims to approximate that loop with explicit files:

```text
observe learner -> infer learner state -> choose next episode -> watch attempt -> give feedback -> update memory
```

## Core Ideas

- Any folder can become a learning workspace.
- Obsidian stores long-term learner memory and durable knowledge.
- Local folders store source-proximal control files and indexes.
- Context packets keep model context focused.
- Learning artifacts keep sessions from disappearing into chat history.
- Codex coordinates; Gemini and Claude consult.

## Public vs Private

This repository should contain public-safe infrastructure:

- docs;
- templates;
- synthetic examples;
- command specifications;
- scaffold code.

Your private Obsidian vault should contain real learner state:

- global learner profile;
- domain profiles;
- misconceptions;
- session logs;
- course notes;
- real workspace bridge notes.

Do not commit private learner state or course materials.

## Planned CLI

```bash
ai-tutor init-global
ai-tutor init-domain LLMs
ai-tutor init-workspace --name nanoGPT --source "C:\path\to\nanoGPT" --domain LLMs
ai-tutor show-context
ai-tutor start-session
ai-tutor close-session
```

## Repository Layout

```text
docs/                  Design, workflows, privacy, command specs
templates/             Public-safe Markdown templates
examples/              Synthetic example workspaces
AGENTS.md              Codex/project instructions
GEMINI.md              Gemini consultant instructions
CLAUDE.md              Claude consultant instructions
```

## First Pilot Subjects

- nanoGPT
- Scientific Machine Learning
- Inverse Problems and Data Assimilation

The latter two are more important long term, but nanoGPT is the first code-heavy pilot because it is already available locally.
