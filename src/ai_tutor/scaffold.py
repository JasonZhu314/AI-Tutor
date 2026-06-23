"""File-based scaffold operations for AI Tutor.

The functions in this module are deliberately small and dependency-free. They build
plans first, then the CLI decides whether to apply those plans. This keeps private
Obsidian and workspace writes explicit.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
import re
from string import Template
from typing import Mapping

PLACEHOLDER_RE = re.compile(r"{{\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*}}")
INVALID_PATH_CHARS_RE = re.compile(r'[<>:"/\\|?*]+')


@dataclass(frozen=True)
class FileAction:
    """A planned file write."""

    path: Path
    content: str
    description: str


@dataclass(frozen=True)
class WriteResult:
    """Result of applying or previewing a file action."""

    path: Path
    status: str
    description: str


def today() -> str:
    return date.today().isoformat()


def timestamp() -> str:
    return datetime.now().strftime("%Y%m%d-%H%M%S")


def slugify(value: str) -> str:
    cleaned = INVALID_PATH_CHARS_RE.sub("-", value).strip().strip(".")
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned or "workspace"


def default_template_root() -> Path:
    module_path = Path(__file__).resolve()
    candidates = [
        module_path.parents[2] / "templates",
        Path.cwd() / "templates",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return candidates[0]


def project_root_from_vault(vault: Path, project_name: str = "AI Tutor") -> Path:
    return vault / "Projects" / project_name


def render_text(text: str, values: Mapping[str, str]) -> str:
    def replace(match: re.Match[str]) -> str:
        key = match.group(1)
        return str(values.get(key, match.group(0)))

    return PLACEHOLDER_RE.sub(replace, text)


def render_template(template_root: Path, relative_path: str, values: Mapping[str, str]) -> str:
    path = template_root / relative_path
    text = path.read_text(encoding="utf-8")
    return render_text(text, values)


def base_values(**overrides: str) -> dict[str, str]:
    values = {
        "created_date": today(),
        "mode": "tutor",
        "goal": "TBD",
    }
    values.update({key: str(value) for key, value in overrides.items()})
    return values


def global_index_content(created_date: str) -> str:
    return f"""---
type: index
scope: global
created: {created_date}
last_updated: {created_date}
---

# AI Tutor Index

## Core Files

- [[Global Learner Profile]]

## Folders

- [[Domains]]
- [[Workspaces]]

## Notes

This is the private AI Tutor home inside the Obsidian vault. Do not commit real learner state to the public repository.
"""


def domain_index_content(domain: str, created_date: str) -> str:
    return f"""---
type: domain-index
domain: {domain}
created: {created_date}
last_updated: {created_date}
---

# {domain} Index

## Learner State

- [[{domain} Learner Profile]]

## Workspaces

- TBD

## Notes

Add course, repo, paper, and research-field workspaces related to {domain} here.
"""


def init_global_plan(project_root: Path, template_root: Path) -> list[FileAction]:
    values = base_values()
    return [
        FileAction(
            project_root / "Global Learner Profile.md",
            render_template(template_root, "global/Global Learner Profile.md", values),
            "global learner profile",
        ),
        FileAction(
            project_root / "AI Tutor Index.md",
            global_index_content(values["created_date"]),
            "global AI Tutor index",
        ),
        FileAction(project_root / "Domains" / ".gitkeep", "", "domains directory marker"),
        FileAction(project_root / "Workspaces" / ".gitkeep", "", "workspaces directory marker"),
    ]


def init_domain_plan(project_root: Path, domain: str, template_root: Path) -> list[FileAction]:
    domain_dir = project_root / "Domains" / slugify(domain)
    values = base_values(domain=domain)
    return [
        FileAction(
            domain_dir / f"{domain} Learner Profile.md",
            render_template(template_root, "domain/Domain Profile.md", values),
            "domain learner profile",
        ),
        FileAction(
            domain_dir / f"{domain} Index.md",
            domain_index_content(domain, values["created_date"]),
            "domain index",
        ),
    ]


def workspace_file_name(workspace_name: str, suffix: str) -> str:
    return f"{workspace_name} {suffix}.md"


def init_workspace_plan(
    project_root: Path,
    workspace_name: str,
    source_root: Path,
    domain: str,
    template_root: Path,
    *,
    local_control: bool = False,
) -> list[FileAction]:
    workspace_dir = project_root / "Workspaces" / slugify(workspace_name)
    values = base_values(
        workspace_name=workspace_name,
        source_root=str(source_root),
        domain=domain,
    )
    actions = [
        FileAction(
            workspace_dir / workspace_file_name(workspace_name, "Learning Workspace"),
            render_template(template_root, "workspace/Workspace Bridge.md", values),
            "workspace bridge note",
        ),
        FileAction(
            workspace_dir / workspace_file_name(workspace_name, "Concept Map"),
            render_template(template_root, "workspace/Concept Map.md", values),
            "workspace concept map",
        ),
        FileAction(
            workspace_dir / workspace_file_name(workspace_name, "Source Index"),
            render_template(template_root, "workspace/Source Index.md", values),
            "workspace source index",
        ),
        FileAction(
            workspace_dir / workspace_file_name(workspace_name, "Episode Queue"),
            render_template(template_root, "workspace/Episode Queue.md", values),
            "workspace episode queue",
        ),
        FileAction(
            workspace_dir / workspace_file_name(workspace_name, "Misconceptions"),
            render_template(template_root, "workspace/Misconceptions.md", values),
            "workspace misconceptions",
        ),
        FileAction(
            workspace_dir / workspace_file_name(workspace_name, "Session Log"),
            render_template(template_root, "workspace/Session Log.md", values),
            "workspace session log",
        ),
    ]
    if local_control:
        local_dir = source_root / "_learning"
        actions.extend(
            [
                FileAction(
                    local_dir / "TUTOR.md",
                    render_template(template_root, "workspace/TUTOR.md", values),
                    "local workspace tutor instructions",
                ),
                FileAction(
                    local_dir / "Source Index.md",
                    render_template(template_root, "workspace/Source Index.md", values),
                    "local source index",
                ),
            ]
        )
    return actions


def start_session_plan(
    project_root: Path,
    workspace_name: str,
    mode: str,
    goal: str,
    template_root: Path,
) -> list[FileAction]:
    workspace_dir = project_root / "Workspaces" / slugify(workspace_name)
    session_dir = workspace_dir / "Sessions"
    values = base_values(workspace_name=workspace_name, mode=mode, goal=goal)
    content = render_template(template_root, "workspace/Context Packet.md", values)
    return [
        FileAction(
            session_dir / f"{timestamp()} Context Packet.md",
            content,
            "session context packet",
        )
    ]


def workspace_context_paths(project_root: Path, workspace_name: str) -> list[tuple[str, Path]]:
    workspace_dir = project_root / "Workspaces" / slugify(workspace_name)
    return [
        ("workspace bridge", workspace_dir / workspace_file_name(workspace_name, "Learning Workspace")),
        ("concept map", workspace_dir / workspace_file_name(workspace_name, "Concept Map")),
        ("source index", workspace_dir / workspace_file_name(workspace_name, "Source Index")),
        ("episode queue", workspace_dir / workspace_file_name(workspace_name, "Episode Queue")),
        ("misconceptions", workspace_dir / workspace_file_name(workspace_name, "Misconceptions")),
        ("session log", workspace_dir / workspace_file_name(workspace_name, "Session Log")),
    ]


def apply_plan(actions: list[FileAction], *, apply: bool, force: bool = False) -> list[WriteResult]:
    results: list[WriteResult] = []
    for action in actions:
        path = action.path
        if not apply:
            status = "would create" if not path.exists() else "would skip existing"
            results.append(WriteResult(path, status, action.description))
            continue
        if path.exists() and not force:
            existing = path.read_text(encoding="utf-8") if path.is_file() else None
            if existing == action.content:
                results.append(WriteResult(path, "unchanged", action.description))
                continue
            raise FileExistsError(f"Refusing to overwrite existing file without --force: {path}")
        existed = path.exists()
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(action.content, encoding="utf-8", newline="\n")
        results.append(WriteResult(path, "written" if existed else "created", action.description))
    return results


def format_results(results: list[WriteResult]) -> str:
    lines = []
    for result in results:
        lines.append(f"{result.status}: {result.path} ({result.description})")
    return "\n".join(lines)


def format_context(project_root: Path, workspace_name: str) -> str:
    lines = [f"Context packet inputs for workspace: {workspace_name}", ""]
    for label, path in workspace_context_paths(project_root, workspace_name):
        status = "exists" if path.exists() else "missing"
        lines.append(f"- {label}: {path} [{status}]")
    return "\n".join(lines)


def close_session_checklist(project_root: Path, workspace_name: str) -> str:
    workspace_dir = project_root / "Workspaces" / slugify(workspace_name)
    template = Template(
        """Close-session checklist for $workspace

Update these files if the session produced evidence:

- $session_log
- $misconceptions
- $episode_queue
- $concept_map
- $source_index

Report back:

1. What changed.
2. What evidence was produced.
3. What the next episode should be.
4. Any uncertainty or correctness risks.
"""
    )
    return template.substitute(
        workspace=workspace_name,
        session_log=workspace_dir / workspace_file_name(workspace_name, "Session Log"),
        misconceptions=workspace_dir / workspace_file_name(workspace_name, "Misconceptions"),
        episode_queue=workspace_dir / workspace_file_name(workspace_name, "Episode Queue"),
        concept_map=workspace_dir / workspace_file_name(workspace_name, "Concept Map"),
        source_index=workspace_dir / workspace_file_name(workspace_name, "Source Index"),
    )
