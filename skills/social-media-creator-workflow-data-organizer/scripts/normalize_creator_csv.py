#!/usr/bin/env python3
"""
[INPUT]: A creator-platform CSV export with known or unknown column names.
[OUTPUT]: A UTF-8 CSV with canonical fields, preserved source fields, and safe derived ratios.
[POS]: Deterministic helper for the data-organizer skill; strategy interpretation stays outside.
[PROTOCOL]: Update aliases and tests together, then check the data-organizer knowledge pack.
"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


CANONICAL_FIELDS = (
    "content_id",
    "title",
    "publish_time",
    "impressions",
    "views",
    "likes",
    "comments",
    "saves",
    "shares",
    "follows",
    "search_views",
    "completion_rate",
)

ALIASES = {
    "content_id": {"content_id", "作品id", "内容id", "视频id", "笔记id"},
    "title": {"title", "标题", "作品标题", "内容标题", "笔记标题"},
    "publish_time": {"publish_time", "发布时间", "发布于", "创建时间"},
    "impressions": {"impressions", "曝光", "曝光量", "展现量"},
    "views": {"views", "播放", "播放量", "阅读量", "观看量"},
    "likes": {"likes", "点赞", "点赞量"},
    "comments": {"comments", "评论", "评论量"},
    "saves": {"saves", "收藏", "收藏量"},
    "shares": {"shares", "分享", "分享量", "转发", "转发量"},
    "follows": {"follows", "涨粉", "新增关注", "关注转化"},
    "search_views": {"search_views", "搜索流量", "搜索播放", "搜索阅读"},
    "completion_rate": {"completion_rate", "完播率", "阅读完成率"},
}

DERIVED_FIELDS = (
    "view_rate",
    "engagement_rate",
    "save_rate",
    "follow_rate",
    "search_share",
)


def normalize_header(value: str) -> str:
    return re.sub(r"[\s_\-/（）()]+", "", value.strip().lower())


def alias_index() -> dict[str, str]:
    return {
        normalize_header(alias): canonical
        for canonical, aliases in ALIASES.items()
        for alias in aliases
    }


def parse_number(value: str) -> float | None:
    text = value.strip().replace(",", "")
    if not text:
        return None
    if text.endswith("%"):
        try:
            return float(text[:-1]) / 100
        except ValueError:
            return None
    try:
        return float(text)
    except ValueError:
        return None


def safe_ratio(numerator: float | None, denominator: float | None) -> str:
    if numerator is None or denominator is None or denominator <= 0:
        return ""
    return f"{numerator / denominator:.6f}".rstrip("0").rstrip(".")


def build_mapping(headers: list[str]) -> tuple[dict[str, str], list[str]]:
    index = alias_index()
    mapping: dict[str, str] = {}
    unknown: list[str] = []
    claimed: dict[str, str] = {}
    for header in headers:
        canonical = index.get(normalize_header(header))
        if canonical:
            if canonical in claimed:
                raise ValueError(
                    f"multiple source columns map to {canonical}: "
                    f"{claimed[canonical]!r}, {header!r}"
                )
            claimed[canonical] = header
            mapping[header] = canonical
        else:
            unknown.append(header)
    return mapping, unknown


def normalize_csv(source: Path, destination: Path) -> None:
    with source.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise ValueError("CSV has no header row")
        mapping, unknown = build_mapping(list(reader.fieldnames))
        rows = list(reader)

    source_fields = [f"source__{normalize_header(name) or 'unnamed'}" for name in unknown]
    output_fields = list(CANONICAL_FIELDS) + list(DERIVED_FIELDS) + source_fields
    destination.parent.mkdir(parents=True, exist_ok=True)

    with destination.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=output_fields)
        writer.writeheader()
        for row in rows:
            item = {field: "" for field in output_fields}
            for source_name, canonical in mapping.items():
                item[canonical] = (row.get(source_name) or "").strip()
            for source_name, output_name in zip(unknown, source_fields):
                item[output_name] = (row.get(source_name) or "").strip()

            numbers = {field: parse_number(item[field]) for field in CANONICAL_FIELDS}
            engagement = sum(
                numbers[field] or 0 for field in ("likes", "comments", "saves", "shares")
            )
            item["view_rate"] = safe_ratio(numbers["views"], numbers["impressions"])
            item["engagement_rate"] = safe_ratio(engagement, numbers["views"])
            item["save_rate"] = safe_ratio(numbers["saves"], numbers["views"])
            item["follow_rate"] = safe_ratio(numbers["follows"], numbers["views"])
            item["search_share"] = safe_ratio(numbers["search_views"], numbers["views"])
            writer.writerow(item)


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize creator analytics CSV exports.")
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    normalize_csv(args.source, args.destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
