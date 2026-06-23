# Design Overview

## Architecture

AI Tutor has four durable layers:

```text
1. Raw Sources
   Textbooks, slides, notes, transcripts, problem sets, code, repos, papers.

2. Generated Subject Wiki
   Concept pages, summaries, examples, comparisons, source maps.

3. Learner State
   Mastery map, misconceptions, cadence, practice queue, session logs.

4. Global Obsidian Memory
   Cross-subject learner profile, goals, learning principles, active projects.
```

## Learning OS and Context OS

The tutor has two operating systems:

```text
Learning OS: diagnosis, episodes, mastery, practice
Context OS: source selection, memory, compression, provenance
```

The Learning OS decides what should happen next educationally. The Context OS decides what information belongs in model context right now.

## Hybrid Placement

Use hybrid placement:

```text
Obsidian = canonical learner memory and durable knowledge
Subject folder = local source context and operational control
```

Obsidian stores global learner memory, domain profiles, durable field maps, and cross-subject indexes. Subject folders store local instructions, source indexes, and optional generated local caches.

## Context Packet

Every serious session should assemble a context packet:

```text
1. Current goal
2. Tutor mode
3. Relevant learner state
4. Current episode
5. Source map
6. Active source excerpts or files
7. Learner's current attempt
8. Output contract
```

The model context is working memory, not storage.

## Learning Artifacts

Each serious session should produce or update at least one artifact:

- concept note;
- field map;
- paper packet;
- implementation checklist;
- exercise bank;
- misconception entry;
- mastery update;
- episode queue update;
- session log.

## Agent Model

```text
Codex = coordinator
Gemini = search and field-research consultant
Claude = critique, writing, pedagogy, and reasoning consultant
```

Codex owns context packets, file edits, local code work, Obsidian note updates, and final synthesis. Gemini provides bounded broad search, source discovery, field research, and external critique. Claude provides bounded deep critique, writing review, pedagogy review, alternative explanations, and reasoning checks.
