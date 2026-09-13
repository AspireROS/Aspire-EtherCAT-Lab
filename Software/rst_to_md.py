#!/usr/bin/env python3
"""递归将指定目录下的 .rst 文件重命名为同名 .md 文件。"""

from __future__ import annotations

import argparse
from pathlib import Path


def convert_rst_to_md(root: Path) -> int:
    """转换 root 下的所有 .rst 文件，返回转换数量。"""
    converted = 0
    # 使用后缀小写比较，确保 README.RST 等大小写变体也能被处理。
    for source in root.rglob("*"):
        if not source.is_file() or source.suffix.lower() != ".rst":
            continue
        target = source.with_suffix(".md")
        if target.exists():
            print(f"跳过（目标已存在）：{target}")
            continue
        source.rename(target)
        print(f"已转换：{source} -> {target}")
        converted += 1
    return converted


def main() -> None:
    parser = argparse.ArgumentParser(
        description="递归将目录中的 .rst 文件改名为 .md 文件（不修改文件内容）。"
    )
    parser.add_argument(
        "directory",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parent / "App",
        help="待处理目录，默认是本脚本同级的 App 目录。",
    )
    args = parser.parse_args()

    root = args.directory.resolve()
    if not root.is_dir():
        parser.error(f"目录不存在：{root}")

    count = convert_rst_to_md(root)
    print(f"完成，共转换 {count} 个文件。")


if __name__ == "__main__":
    main()
