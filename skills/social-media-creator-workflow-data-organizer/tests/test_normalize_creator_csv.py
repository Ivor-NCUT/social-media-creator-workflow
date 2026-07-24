from __future__ import annotations

import csv
import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "normalize_creator_csv.py"
SPEC = importlib.util.spec_from_file_location("normalize_creator_csv", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


class NormalizeCreatorCsvTest(unittest.TestCase):
    def test_normalizes_and_computes_safe_rates(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            source = Path(temp_dir) / "source.csv"
            destination = Path(temp_dir) / "normalized.csv"
            source.write_text(
                "作品标题,曝光量,播放量,点赞量,评论量,收藏量,转发量,新增关注,备注\n"
                "测试内容,1000,500,50,10,20,5,15,保留\n",
                encoding="utf-8",
            )
            MODULE.normalize_csv(source, destination)
            with destination.open(encoding="utf-8") as handle:
                row = next(csv.DictReader(handle))
            self.assertEqual(row["title"], "测试内容")
            self.assertEqual(row["view_rate"], "0.5")
            self.assertEqual(row["engagement_rate"], "0.17")
            self.assertEqual(row["follow_rate"], "0.03")
            self.assertEqual(row["source__备注"], "保留")

    def test_rejects_duplicate_aliases(self) -> None:
        with self.assertRaises(ValueError):
            MODULE.build_mapping(["播放量", "观看量"])


if __name__ == "__main__":
    unittest.main()
