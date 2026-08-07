#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TGwiki 必应 IndexNow 提交脚本

用途：
  - 自动遍历 src/**/*.md 生成完整站内 URL 列表
  - 将最新全站 URL 提交至 Bing / IndexNow API，实现搜索引擎秒级收录

提交接口：
  - https://api.indexnow.org/indexnow
  - https://www.bing.com/indexnow
"""

import os
import glob
import json
import urllib.request
import urllib.error

SRC_DIR = "src"
KEY = "4A563D1939640309CA93D410CA082D71"
HOSTS = [
    "wiki.tgnav.org",
    "tg.ygjc.cc"
]

ENDPOINTS = [
    "https://api.indexnow.org/indexnow",
    "https://www.bing.com/indexnow"
]

def get_url_path(md_path):
    # 将 src/path/file.md 转为对应的网页 relative path
    rel_path = os.path.relpath(md_path, SRC_DIR)
    
    # README.md / index.md -> 目录主页 /
    dirname, basename = os.path.split(rel_path)
    filename, _ = os.path.splitext(basename)
    
    if filename.lower() in ("readme", "index"):
        if not dirname or dirname == ".":
            return "/"
        return f"/{dirname}/"
    
    if not dirname or dirname == ".":
        return f"/{filename}.html"
    return f"/{dirname}/{filename}.html"

def main():
    files = sorted(glob.glob(os.path.join(SRC_DIR, "**", "*.md"), recursive=True))
    print(f"📦 发现 {len(files)} 个 Markdown 文章文件。")

    for host in HOSTS:
        url_list = []
        for md in files:
            path = get_url_path(md)
            full_url = f"https://{host}{path}"
            url_list.append(full_url)

        key_location = f"https://{host}/{KEY}.txt"
        
        payload = {
            "host": host,
            "key": KEY,
            "keyLocation": key_location,
            "urlList": url_list
        }

        print(f"\n🚀 开始向 IndexNow 提交域名 [{host}] ({len(url_list)} 个 URL)...")
        data_bytes = json.dumps(payload, indent=2, ensure_ascii=False).encode('utf-8')

        for endpoint in ENDPOINTS:
            try:
                req = urllib.request.Request(
                    endpoint,
                    data=data_bytes,
                    headers={
                        "Content-Type": "application/json; charset=utf-8",
                        "User-Agent": "TGwiki-IndexNow-Submitter/1.0"
                    },
                    method="POST"
                )
                with urllib.request.urlopen(req, timeout=10) as response:
                    status = response.status
                    print(f"  ✅ [{endpoint}] 响应状态码: {status}")
            except urllib.error.HTTPError as e:
                print(f"  ⚠️ [{endpoint}] HTTP 异常: {e.code} - {e.reason}")
                try:
                    err_body = e.read().decode('utf-8')
                    print(f"     详请: {err_body}")
                except Exception:
                    pass
            except Exception as e:
                print(f"  ❌ [{endpoint}] 请求失败: {e}")

if __name__ == "__main__":
    main()
