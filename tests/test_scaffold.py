from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from ai_tutor.scaffold import (
    apply_plan,
    close_session_checklist,
    default_template_root,
    format_context,
    init_domain_plan,
    init_global_plan,
    init_workspace_plan,
    start_session_plan,
)


class ScaffoldTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.project_root = self.root / "vault" / "Projects" / "AI Tutor"
        self.source_root = self.root / "sources" / "nanoGPT"
        self.source_root.mkdir(parents=True)
        self.template_root = default_template_root()

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_init_global_writes_expected_files(self) -> None:
        actions = init_global_plan(self.project_root, self.template_root)
        apply_plan(actions, apply=True)
        self.assertTrue((self.project_root / "Global Learner Profile.md").exists())
        self.assertTrue((self.project_root / "AI Tutor Index.md").exists())

    def test_init_domain_writes_profile_and_index(self) -> None:
        actions = init_domain_plan(self.project_root, "LLMs", self.template_root)
        apply_plan(actions, apply=True)
        self.assertTrue((self.project_root / "Domains" / "LLMs" / "LLMs Learner Profile.md").exists())
        self.assertTrue((self.project_root / "Domains" / "LLMs" / "LLMs Index.md").exists())

    def test_init_workspace_writes_workspace_files(self) -> None:
        actions = init_workspace_plan(
            self.project_root,
            "nanoGPT",
            self.source_root,
            "LLMs",
            self.template_root,
            local_control=True,
        )
        apply_plan(actions, apply=True)
        workspace = self.project_root / "Workspaces" / "nanoGPT"
        self.assertTrue((workspace / "nanoGPT Learning Workspace.md").exists())
        self.assertTrue((workspace / "nanoGPT Concept Map.md").exists())
        self.assertTrue((self.source_root / "_learning" / "TUTOR.md").exists())

    def test_start_session_writes_context_packet_with_goal(self) -> None:
        actions = start_session_plan(
            self.project_root,
            "nanoGPT",
            "tutor",
            "Understand causal self-attention",
            self.template_root,
        )
        apply_plan(actions, apply=True)
        sessions = list((self.project_root / "Workspaces" / "nanoGPT" / "Sessions").glob("*.md"))
        self.assertEqual(len(sessions), 1)
        text = sessions[0].read_text(encoding="utf-8")
        self.assertIn("Understand causal self-attention", text)

    def test_show_and_close_session_outputs_paths(self) -> None:
        text = format_context(self.project_root, "nanoGPT")
        self.assertIn("Context packet inputs for workspace: nanoGPT", text)
        checklist = close_session_checklist(self.project_root, "nanoGPT")
        self.assertIn("Close-session checklist", checklist)
        self.assertIn("nanoGPT Session Log.md", checklist)


if __name__ == "__main__":
    unittest.main()
