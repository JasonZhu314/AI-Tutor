# Workflows

## Start A Learning Workspace

1. Choose a source folder.
2. Create or locate the Obsidian bridge note.
3. Initialize workspace control files.
4. Build a source index.
5. Create the first context packet.
6. Run a short diagnostic.
7. Start the first learning episode.

## Start Session

Session start should assemble:

- current goal;
- tutor mode;
- relevant learner profile snippets;
- domain profile snippets;
- current episode queue;
- relevant source map;
- active source files or excerpts;
- output contract.

## Close Session

Session close should update:

- session log;
- mastery map;
- misconception list;
- episode queue;
- generated concept notes or other learning artifacts.

The tutor should report all changed files in chat.

## Tutor Mode

Use when learning new material.

Pattern:

```text
diagnose -> attempt -> hint -> feedback -> correction -> transfer -> memory update
```

## Examiner Mode

Use when testing mastery.

Rules:

- no hints during the test;
- one question at a time;
- classify errors after the attempt;
- update mastery only with evidence.

## Feedback Mode

Use when reviewing learner output.

Inputs:

- code;
- proofs;
- derivations;
- essays;
- problem set attempts;
- written explanations.

Outputs:

- exact issues;
- error categories;
- smallest next repair;
- follow-up practice.

## Research Field Mode

Goal: build a field atlas before diving into individual papers.

Artifact:

```text
core problems
canonical papers
main mathematical objects
standard benchmarks
datasets and software
major schools of thought
open controversies
prerequisite map
reading ladder
implementation ladder
```

## Paper Deep Dive Mode

Goal: understand a paper deeply enough to critique or implement it.

Protocol:

```text
1. Triage: problem, claim, contribution
2. Structure: assumptions, notation, method, experiments
3. Reconstruction: derive equations or algorithm
4. Critique: reviewer-style weaknesses and missing evidence
5. Implementation: minimal reproducible version
6. Integration: update field map, learner state, and open questions
```
