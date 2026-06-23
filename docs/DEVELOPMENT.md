# Development

## Current Implementation

The scaffold CLI is standard-library only. It is intentionally small so the file-based workflow can be validated before adding dependencies, retrieval, plugin logic, or model API calls.

## Run From Source

From the repository root:

```bash
PYTHONPATH=src python -m ai_tutor.cli --help
```

PowerShell:

```powershell
$env:PYTHONPATH = "src"
python -m ai_tutor.cli --help
```

## Test

```bash
PYTHONPATH=src python -m unittest discover -s tests
python -m compileall -q src tests
```

## Design Constraints

- Commands are dry-run by default.
- `--apply` is required for writes.
- Do not call LLM APIs in Phase 1.
- Do not write real private learner state into this public repo.
- Keep Codex as coordinator; Gemini and Claude are consultants.

## Next Engineering Step

Add a local configuration mechanism so users do not need to pass `--project-root` repeatedly. The config must remain private and ignored by git.
