# AI Tutor

AI Tutor is a personal, folder-native tutoring system for learning from local resources: course folders, textbooks, papers, Obsidian vaults, and code repositories.

The system is designed around Codex as the primary coordinator, with Gemini and Claude as occasional consultants.

## Status

Phase 1 scaffold CLI. The current implementation renders Markdown templates, creates private Obsidian/workspace files, and prints context packet paths. It does not call an LLM API.

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

## Run From Source

The implementation is currently standard-library only. From the repo root:

```bash
python -m ai_tutor.cli --help
```

If running from a checkout without installing the package, set `PYTHONPATH=src` first.

PowerShell example:

```powershell
$env:PYTHONPATH = "src"
python -m ai_tutor.cli --help
```

## Scaffold Example

Commands are dry-run by default. Add `--apply` to write files.

```bash
ai-tutor init-global --vault "<vault-path>" --apply
ai-tutor init-domain LLMs --project-root "<vault-path>/Projects/AI Tutor" --apply
ai-tutor init-workspace --name nanoGPT --source "<path-to-nanogpt>" --domain LLMs --project-root "<vault-path>/Projects/AI Tutor" --apply
ai-tutor show-context --workspace nanoGPT --project-root "<vault-path>/Projects/AI Tutor"
ai-tutor start-session --workspace nanoGPT --mode tutor --goal "Understand causal self-attention" --project-root "<vault-path>/Projects/AI Tutor" --apply
ai-tutor close-session --workspace nanoGPT --project-root "<vault-path>/Projects/AI Tutor"
```

Use `--local-control` with `init-workspace` only when you want to create `_learning/` files inside the source folder.

## Repository Layout

```text
src/                   Python scaffold CLI
tests/                 Unit tests for scaffold behavior
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
