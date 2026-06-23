"""Command-line interface for the AI Tutor scaffold."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

from .scaffold import (
    apply_plan,
    close_session_checklist,
    default_template_root,
    format_context,
    format_results,
    init_domain_plan,
    init_global_plan,
    init_workspace_plan,
    project_root_from_vault,
    start_session_plan,
)


def existing_path(value: str) -> Path:
    return Path(value).expanduser().resolve()


def template_root_from_args(args: argparse.Namespace) -> Path:
    return existing_path(args.template_root) if args.template_root else default_template_root()


def require_project_root(args: argparse.Namespace) -> Path:
    if not args.project_root:
        raise SystemExit("--project-root is required for this command")
    return existing_path(args.project_root)


def add_write_options(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--apply", action="store_true", help="write files; default is dry-run")
    parser.add_argument("--force", action="store_true", help="overwrite existing files")
    parser.add_argument("--template-root", help="template directory; defaults to repo templates/")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ai-tutor",
        description="File-based scaffold for a folder-native, Obsidian-connected AI tutor.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    init_global = sub.add_parser("init-global", help="initialize global AI Tutor files")
    init_global.add_argument("--vault", help="Obsidian vault path")
    init_global.add_argument("--project-root", help="explicit AI Tutor project root")
    init_global.add_argument("--project-name", default="AI Tutor", help="project folder under <vault>/Projects")
    add_write_options(init_global)

    init_domain = sub.add_parser("init-domain", help="initialize a domain profile")
    init_domain.add_argument("domain")
    init_domain.add_argument("--project-root", required=True, help="AI Tutor project root")
    add_write_options(init_domain)

    init_workspace = sub.add_parser("init-workspace", help="initialize a learning workspace")
    init_workspace.add_argument("--name", required=True, help="workspace name")
    init_workspace.add_argument("--source", required=True, help="source folder path")
    init_workspace.add_argument("--domain", required=True, help="domain name")
    init_workspace.add_argument("--project-root", required=True, help="AI Tutor project root")
    init_workspace.add_argument(
        "--local-control",
        action="store_true",
        help="also create _learning/ files inside the source folder",
    )
    add_write_options(init_workspace)

    show_context = sub.add_parser("show-context", help="print context packet input paths")
    show_context.add_argument("--workspace", required=True, help="workspace name")
    show_context.add_argument("--project-root", required=True, help="AI Tutor project root")

    start_session = sub.add_parser("start-session", help="create a session context packet")
    start_session.add_argument("--workspace", required=True, help="workspace name")
    start_session.add_argument("--mode", default="tutor", help="session mode")
    start_session.add_argument("--goal", required=True, help="session goal")
    start_session.add_argument("--project-root", required=True, help="AI Tutor project root")
    add_write_options(start_session)

    close_session = sub.add_parser("close-session", help="print close-session checklist")
    close_session.add_argument("--workspace", required=True, help="workspace name")
    close_session.add_argument("--project-root", required=True, help="AI Tutor project root")

    return parser


def run(args: argparse.Namespace) -> str:
    if args.command == "init-global":
        if args.project_root:
            project_root = existing_path(args.project_root)
        elif args.vault:
            project_root = project_root_from_vault(existing_path(args.vault), args.project_name)
        else:
            raise SystemExit("init-global requires --vault or --project-root")
        actions = init_global_plan(project_root, template_root_from_args(args))
        return format_results(apply_plan(actions, apply=args.apply, force=args.force))

    if args.command == "init-domain":
        actions = init_domain_plan(require_project_root(args), args.domain, template_root_from_args(args))
        return format_results(apply_plan(actions, apply=args.apply, force=args.force))

    if args.command == "init-workspace":
        actions = init_workspace_plan(
            require_project_root(args),
            args.name,
            existing_path(args.source),
            args.domain,
            template_root_from_args(args),
            local_control=args.local_control,
        )
        return format_results(apply_plan(actions, apply=args.apply, force=args.force))

    if args.command == "show-context":
        return format_context(require_project_root(args), args.workspace)

    if args.command == "start-session":
        actions = start_session_plan(
            require_project_root(args),
            args.workspace,
            args.mode,
            args.goal,
            template_root_from_args(args),
        )
        return format_results(apply_plan(actions, apply=args.apply, force=args.force))

    if args.command == "close-session":
        return close_session_checklist(require_project_root(args), args.workspace)

    raise SystemExit(f"Unknown command: {args.command}")


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        output = run(args)
    except Exception as exc:  # keep CLI errors readable for now
        print(f"error: {exc}", file=sys.stderr)
        return 1
    if output:
        print(output)
    if hasattr(args, "apply") and not args.apply:
        print("\nDry-run only. Re-run with --apply to write files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
