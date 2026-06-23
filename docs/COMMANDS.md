# Command Specification

This file specifies planned commands. The first implementation can be a simple Python CLI that renders templates and prints paths. No LLM API is required for the MVP.

## init-global

Create global learner files in a configured Obsidian location.

```bash
ai-tutor init-global --vault "<vault-path>"
```

Outputs:

- Global Learner Profile
- Global Tutor Index
- Domains folder
- Workspaces folder

## init-domain

Create a domain profile.

```bash
ai-tutor init-domain LLMs
```

Outputs:

- domain learner profile;
- domain concept index;
- domain practice queue.

## init-workspace

Create workspace files and an Obsidian bridge note.

```bash
ai-tutor init-workspace --name nanoGPT --source "C:\path\to\nanoGPT" --domain LLMs
```

Outputs:

- workspace bridge note;
- local `_learning/` control files if requested;
- source index stub;
- concept map stub;
- episode queue stub.

## show-context

Print the context packet that would be loaded for the next session.

```bash
ai-tutor show-context --workspace nanoGPT
```

## start-session

Create a session context packet.

```bash
ai-tutor start-session --workspace nanoGPT --mode tutor --goal "Understand causal self-attention"
```

## close-session

Render a session close checklist and target files to update.

```bash
ai-tutor close-session --workspace nanoGPT
```

## Future Commands

```text
ai-tutor diagnose-topic
ai-tutor examiner
ai-tutor ingest-source
ai-tutor review-notes
ai-tutor plan-next-episode
ai-tutor gemini-review
ai-tutor claude-review
```
