#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TGwiki 内部文章链接审计脚本（确定性 / 离线）

用途：
  - 本地校验（python scripts/check-links.py）
  - CI 防回归（GitHub Actions 在 PR/push 改动 src/**/*.md 时自动跑）

审计范围：
  扫描 src/**/*.md 中的所有 Markdown 内部链接 `](path)`，
  仅校验「文章链接」(.md / .html)，输出断链并以非零退出码报错。

不校验（避免误报）：
  - http(s):// 外链（含 cdn.jsdelivr.net 图片）
  - mailto: / tel:
  - 图片等资源链接（非 .md/.html 后缀，如 /assets/images/*.jpg）
  - 纯锚点链接 (#anchor)

路径解析规则（与 VuePress base 配置一致）：
  - 以 "/" 开头的根路径链接：按站点根目录 src/ 解析
    （base 只影响 URL 前缀，不改变源文件布局，故恒从 src/ 解析）
  - 相对路径：从当前 .md 文件所在目录归一化解析
  - 链接写 .html 后缀，但源码是 .md，统一还原为 .md 判存在
"""
import os
import re
import sys
import glob

SRC = "src"


def main():
    broken = []
    total = 0
    files = sorted(glob.glob(os.path.join(SRC, "**", "*.md"), recursive=True))

    for md in files:
        d = os.path.dirname(md)
        rel = os.path.relpath(md, SRC)
        with open(md, encoding="utf-8") as f:
            for i, line in enumerate(f, 1):
                for m in re.finditer(r"\]\(([^)\s]+)\)", line):
                    link = m.group(1)
                    # 跳过外链 / 特殊协议
                    if link.startswith(("http://", "https://", "mailto:", "tel:")):
                        continue
                    path = link.split("#")[0]  # 去掉锚点
                    if not path:
                        continue
                    # 只审计文章链接（.md 或 .html）
                    if not (path.endswith(".md") or path.endswith(".html")):
                        continue
                    # 根路径从 src/ 解析；相对路径从当前文件目录解析
                    if path.startswith("/"):
                        cand = os.path.normpath(os.path.join(SRC, path.lstrip("/")))
                    else:
                        cand = os.path.normpath(os.path.join(d, path))
                    cand_md = os.path.splitext(cand)[0] + ".md"
                    total += 1
                    if not os.path.isfile(cand_md):
                        broken.append((rel, i, link, cand_md))

    print(f"扫描文章文件: {len(files)} | 检测文章链接: {total} | 断链: {len(broken)}")
    if broken:
        print("\n发现以下断链：")
        for rel, i, link, cand in broken:
            print(f"  ❌ {rel}:{i}  {link}  ->  解析为 {cand} 不存在")
        print("\n⚠️ 链接审计未通过，请修复上述断链后再提交。")
        sys.exit(1)
    print("✅ 全站文章链接零断链")
    sys.exit(0)


if __name__ == "__main__":
    main()
