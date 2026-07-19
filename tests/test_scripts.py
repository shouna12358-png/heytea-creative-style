from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "heytea-style"


class ScriptTests(unittest.TestCase):
    def test_skill_frontmatter_and_assets(self) -> None:
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\nname: heytea-style\n"))
        self.assertIn("\ndescription:", text.split("\n---", 1)[0])
        self.assertTrue((SKILL / "assets" / "font-f-coarse-reference.png").is_file())
        self.assertTrue((SKILL / "assets" / "font-i-fine-reference.png").is_file())

    def test_stage_cache_and_render(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            source = temp / "source.png"
            staged = temp / "staged.png"
            manifest = temp / "manifest.json"
            base = Image.new("RGB", (540, 960), "white")
            base.save(source)

            stage = SKILL / "scripts" / "stage_input.py"
            command = [sys.executable, str(stage), "--src", str(source), "--out", str(staged), "--manifest", str(manifest)]
            subprocess.run(command, check=True, capture_output=True, text=True)
            subprocess.run(command, check=True, capture_output=True, text=True)
            data = json.loads(manifest.read_text(encoding="utf-8"))
            self.assertTrue(data["cache_reused"])
            self.assertEqual((data["width"], data["height"]), (540, 960))

            title_f = temp / "f.png"
            title_i = temp / "i.png"
            for path, width in ((title_f, 16), (title_i, 8)):
                layer = Image.new("RGB", (300, 400), "white")
                draw = ImageDraw.Draw(layer)
                draw.line((40, 40, 260, 360), fill="black", width=width)
                layer.save(path)

            out_f = temp / "out-f.jpg"
            out_i = temp / "out-i.jpg"
            render = SKILL / "scripts" / "render_variants.py"
            subprocess.run([
                sys.executable, str(render), "--base", str(staged),
                "--title-f", str(title_f), "--title-i", str(title_i),
                "--out-f", str(out_f), "--out-i", str(out_i),
            ], check=True, capture_output=True, text=True)
            with Image.open(out_f) as rendered_f, Image.open(out_i) as rendered_i:
                self.assertEqual(rendered_f.size, (540, 960))
                self.assertEqual(rendered_i.size, (540, 960))


if __name__ == "__main__":
    unittest.main()
