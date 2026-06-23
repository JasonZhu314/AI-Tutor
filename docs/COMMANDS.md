# Command Specification

The current CLI is a standard-library Python scaffold. It renders templates, creates private AI Tutor files, and prints context packet paths. It does not call an LLM API.

Commands are dry-run by default. Use `--apply` to write files and `--force` to overwrite existing files.

## init-global

Create global learner files in a configured Obsidian location.

```bash
ai-tutor init-global --vault "<vault-path>"
ai-tutor init-global --vault "<vault-path>" --apply
```

Default target:

```text
<vault-path>/Projects/AI Tutor
```

Outputs:

- `Global Learner Profile.md`
- `AI Tutor Index.md`
- `Domains/`
- `Workspaces/`

## init-domain

Create a domain profile under a private AI Tutor project root.

```bash
ai-tutor init-domain LLMs --project-root "<vault-path>/Projects/AI Tutor"
ai-tutor init-domain LLMs --project-root "<vault-path>/Projects/AI Tutor" --apply
```

Outputs:

- `Domains/LLMs/LLMs Learner Profile.md`
- `Domains/LLMs/LLMs Index.md`

## init-workspace

Create workspace files and an Obsidian bridge note.

```bash
ai-tutor init-workspace --name nanoGPT --source "<path-to-nanogpt>" --domain LLMs --project-root "<vault-path>/Projects/AI Tutor"
ai-tutor init-workspace --name nanoGPT --source "<path-to-nanogpt>" --domain LLMs --project-root "<vault-path>/Projects/AI Tutor" --apply
```

Outputs under `Workspaces/<workspace>/`:

- workspace bridge note;
- concept map;
- source index;
- episode queue;
- misconceptions;
- session log.

Optional source-local control files:

```bash
ai-tutor init-workspace --name nanoGPT --source "<path-to-nanogpt>" --domain LLMs --project-root "<vault-path>/Projects/AI Tutor" --local-control --apply
```

`--local-control` creates `_learning/TUTOR.md` and `_learning/Source Index.md` inside the source folder.

## show-context

Print the context packet input paths for the next session.

```bash
ai-tutor show-context --workspace nanoGPT --project-root "<vault-path>/Projects/AI Tutor"
```

## start-session

Create a session context packet.

```bash
ai-tutor start-session --workspace nanoGPT --mode tutor --goal "Understand causal self-attention" --project-root "<vault-path>/Projects/AI Tutor"
ai-tutor start-session --workspace nanoGPT --mode tutor --goal "Understand causal self-attention" --project-root "<vault-path>/Projects/AI Tutor" --apply
```

Output:

- `Workspaces/<workspace>/Sessions/<timestamp> Context Packet.md`

## close-session

Render a session close checklist and target files to update.

```bash
ai-tutor close-session --workspace nanoGPT --project-root "<vault-path>/Projects/AI Tutor"
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
