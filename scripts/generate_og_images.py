#!/usr/bin/env python3
"""
Generate high-resolution Open Graph (OG) & Twitter Card images for TGWIKI.
Uses headless Google Chrome to render HTML/CSS designs into 1200x630 and 800x800 PNG images.
"""

import base64
import os
import subprocess
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
ASSETS_DIR = os.path.join(PROJECT_ROOT, "src", ".vuepress", "public", "assets")
TEMP_DIR = "/tmp/tgwiki_og"

os.makedirs(TEMP_DIR, exist_ok=True)
os.makedirs(ASSETS_DIR, exist_ok=True)

def to_base64(filepath):
    if not os.path.exists(filepath):
        print(f"Error: file {filepath} not found.")
        sys.exit(1)
    with open(filepath, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

banner_bg_b64 = to_base64(os.path.join(ASSETS_DIR, "og-hero-banner.jpg"))
square_bg_b64 = to_base64(os.path.join(ASSETS_DIR, "og-hero-square.jpg"))

# 1. 1200x630 Landscape Card (Open Graph & Twitter summary_large_image)
html_1200 = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<style>
* {{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}}
body {{
  width: 1200px;
  height: 630px;
  overflow: hidden;
  background-color: #060b17;
  font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Segoe UI", Roboto, sans-serif;
  color: #ffffff;
  position: relative;
}}

/* Background layers */
.bg-image {{
  position: absolute;
  top: 0;
  right: -40px;
  width: 780px;
  height: 630px;
  background-image: url('data:image/jpeg;base64,{banner_bg_b64}');
  background-size: cover;
  background-position: center right;
  -webkit-mask-image: linear-gradient(to left, rgba(0,0,0,0.95) 45%, rgba(0,0,0,0) 95%);
  mask-image: linear-gradient(to left, rgba(0,0,0,0.95) 45%, rgba(0,0,0,0) 95%);
  z-index: 1;
}}

.ambient-glow-1 {{
  position: absolute;
  top: -120px;
  left: -80px;
  width: 550px;
  height: 550px;
  background: radial-gradient(circle, rgba(34, 158, 217, 0.22) 0%, rgba(14, 165, 233, 0.08) 50%, transparent 75%);
  z-index: 2;
  pointer-events: none;
}}

.ambient-glow-2 {{
  position: absolute;
  bottom: -150px;
  left: 300px;
  width: 500px;
  height: 450px;
  background: radial-gradient(circle, rgba(56, 189, 248, 0.15) 0%, rgba(99, 102, 241, 0.08) 45%, transparent 70%);
  z-index: 2;
  pointer-events: none;
}}

.grid-overlay {{
  position: absolute;
  inset: 0;
  background-image: 
    linear-gradient(to right, rgba(255, 255, 255, 0.025) 1px, transparent 1px),
    linear-gradient(to bottom, rgba(255, 255, 255, 0.025) 1px, transparent 1px);
  background-size: 48px 48px;
  z-index: 2;
  pointer-events: none;
}}

/* Main layout */
.container {{
  position: relative;
  z-index: 10;
  width: 1200px;
  height: 630px;
  padding: 56px 64px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}}

/* Top Brand Tag */
.brand-pill {{
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: rgba(14, 165, 233, 0.12);
  border: 1px solid rgba(56, 189, 248, 0.35);
  padding: 8px 18px;
  border-radius: 9999px;
  backdrop-filter: blur(12px);
  width: fit-content;
  box-shadow: 0 4px 20px rgba(0, 186, 255, 0.15);
}}

.pulse-dot {{
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #38bdf8;
  box-shadow: 0 0 10px #38bdf8;
}}

.brand-pill-text {{
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 1.5px;
  color: #7dd3fc;
  text-transform: uppercase;
}}

.brand-pill-divider {{
  color: rgba(255, 255, 255, 0.25);
}}

.brand-pill-sub {{
  font-size: 13px;
  color: #e2e8f0;
  font-weight: 500;
  letter-spacing: 0.5px;
}}

/* Content area */
.main-content {{
  max-width: 660px;
  margin-top: 18px;
}}

.hero-title-row {{
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 12px;
}}

.hero-title {{
  font-size: 64px;
  font-weight: 900;
  letter-spacing: -0.5px;
  line-height: 1.1;
  background: linear-gradient(135deg, #ffffff 20%, #e0f2fe 55%, #38bdf8 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  filter: drop-shadow(0 4px 24px rgba(56, 189, 248, 0.35));
}}

.verified-badge {{
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 38px;
  height: 38px;
  background: linear-gradient(135deg, #0284c7, #0ea5e9);
  border-radius: 50%;
  box-shadow: 0 0 16px rgba(14, 165, 233, 0.6);
}}

.verified-badge svg {{
  width: 22px;
  height: 22px;
  fill: #ffffff;
}}

.hero-subtitle {{
  font-size: 24px;
  font-weight: 600;
  color: #94a3b8;
  letter-spacing: 0.5px;
  margin-bottom: 28px;
  display: flex;
  align-items: center;
  gap: 10px;
}}

.hero-subtitle span {{
  color: #38bdf8;
}}

/* Features 2x2 grid */
.features-grid {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
  max-width: 650px;
}}

.feature-card {{
  background: rgba(15, 23, 42, 0.65);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 14px;
  padding: 12px 16px;
  display: flex;
  align-items: center;
  gap: 12px;
  backdrop-filter: blur(16px);
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.3);
  position: relative;
  overflow: hidden;
}}

.feature-card::before {{
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 3px;
  height: 100%;
  background: linear-gradient(to bottom, #38bdf8, transparent);
}}

.feature-icon {{
  font-size: 22px;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  border-radius: 10px;
  background: rgba(56, 189, 248, 0.12);
  border: 1px solid rgba(56, 189, 248, 0.2);
  flex-shrink: 0;
}}

.feature-text {{
  display: flex;
  flex-direction: column;
}}

.feature-title {{
  font-size: 15px;
  font-weight: 700;
  color: #f1f5f9;
  letter-spacing: 0.2px;
}}

.feature-desc {{
  font-size: 12px;
  color: #94a3b8;
  margin-top: 2px;
  white-space: nowrap;
}}

/* Footer */
.footer-row {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 20px;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
}}

.domain-badge {{
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 9999px;
  padding: 8px 20px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.2);
}}

.domain-icon {{
  color: #38bdf8;
  display: flex;
}}

.domain-name {{
  font-size: 16px;
  font-weight: 800;
  letter-spacing: 1px;
  color: #ffffff;
}}

.domain-highlight {{
  color: #38bdf8;
}}

.meta-tags {{
  display: flex;
  align-items: center;
  gap: 18px;
}}

.meta-item {{
  font-size: 13px;
  color: #64748b;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 6px;
}}

.meta-item strong {{
  color: #cbd5e1;
  font-weight: 600;
}}
</style>
</head>
<body>
  <div class="bg-image"></div>
  <div class="ambient-glow-1"></div>
  <div class="ambient-glow-2"></div>
  <div class="grid-overlay"></div>

  <div class="container">
    <div>
      <div class="brand-pill">
        <div class="pulse-dot"></div>
        <span class="brand-pill-text">TGWIKI</span>
        <span class="brand-pill-divider">/</span>
        <span class="brand-pill-sub">高质量 Telegram 中文知识库</span>
      </div>
    </div>

    <div class="main-content">
      <div class="hero-title-row">
        <h1 class="hero-title">电报宝典</h1>
        <div class="verified-badge">
          <svg viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>
        </div>
      </div>
      <div class="hero-subtitle">
        Telegram 全方位使用指南 <span>·</span> 零基础轻松入门
      </div>

      <div class="features-grid">
        <div class="feature-card">
          <div class="feature-icon">🚀</div>
          <div class="feature-text">
            <span class="feature-title">新手入门与汉化</span>
            <span class="feature-desc">官方下载 / 一键中文语言包</span>
          </div>
        </div>

        <div class="feature-card">
          <div class="feature-icon">🔓</div>
          <div class="feature-text">
            <span class="feature-title">限制与封号解除</span>
            <span class="feature-desc">+86私聊限制 / 快速申诉解封</span>
          </div>
        </div>

        <div class="feature-card">
          <div class="feature-icon">🛡️</div>
          <div class="feature-text">
            <span class="feature-title">账号与隐私安全</span>
            <span class="feature-desc">双重验证 / 防盗号与防被封</span>
          </div>
        </div>

        <div class="feature-card">
          <div class="feature-icon">💎</div>
          <div class="feature-text">
            <span class="feature-title">进阶玩转与生态</span>
            <span class="feature-desc">Premium会员 / 机器人 / 频道推荐</span>
          </div>
        </div>
      </div>
    </div>

    <div class="footer-row">
      <div class="domain-badge">
        <span class="domain-icon">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10"></circle>
            <line x1="2" y1="12" x2="22" y2="12"></line>
            <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
          </svg>
        </span>
        <span class="domain-name">tg.<span class="domain-highlight">ygjc.cc</span></span>
      </div>

      <div class="meta-tags">
        <div class="meta-item">
          <span>开源地址:</span>
          <strong>github.com/mjiagou/tgwiki</strong>
        </div>
        <div class="meta-item">
          <span>推特:</span>
          <strong>@hasenbalg673018</strong>
        </div>
      </div>
    </div>
  </div>
</body>
</html>
"""

# 2. 800x800 Square Card
html_800 = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<style>
* {{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}}
body {{
  width: 800px;
  height: 800px;
  overflow: hidden;
  background-color: #060b17;
  font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Segoe UI", Roboto, sans-serif;
  color: #ffffff;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  padding: 48px 40px 42px;
}}

/* Background layers */
.bg-square {{
  position: absolute;
  top: 10px;
  left: 50%;
  transform: translateX(-50%);
  width: 580px;
  height: 520px;
  background-image: url('data:image/jpeg;base64,{square_bg_b64}');
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
  mix-blend-mode: screen;
  mask-image: radial-gradient(ellipse 65% 65% at 50% 48%, #000 30%, rgba(0,0,0,0.7) 50%, transparent 68%);
  -webkit-mask-image: radial-gradient(ellipse 65% 65% at 50% 48%, #000 30%, rgba(0,0,0,0.7) 50%, transparent 68%);
  z-index: 1;
}}

.ambient-glow {{
  position: absolute;
  top: 100px;
  left: 50%;
  transform: translateX(-50%);
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, rgba(34, 158, 217, 0.22) 0%, rgba(14, 165, 233, 0.08) 50%, transparent 75%);
  z-index: 2;
  pointer-events: none;
}}

.grid-overlay {{
  position: absolute;
  inset: 0;
  background-image: 
    linear-gradient(to right, rgba(255, 255, 255, 0.025) 1px, transparent 1px),
    linear-gradient(to bottom, rgba(255, 255, 255, 0.025) 1px, transparent 1px);
  background-size: 40px 40px;
  z-index: 2;
  pointer-events: none;
}}

.top-header {{
  position: relative;
  z-index: 10;
}}

.brand-pill {{
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: rgba(14, 165, 233, 0.12);
  border: 1px solid rgba(56, 189, 248, 0.35);
  padding: 7px 16px;
  border-radius: 9999px;
  backdrop-filter: blur(12px);
  box-shadow: 0 4px 16px rgba(0, 186, 255, 0.15);
}}

.pulse-dot {{
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #38bdf8;
  box-shadow: 0 0 8px #38bdf8;
}}

.brand-pill-text {{
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 1.5px;
  color: #7dd3fc;
}}

.brand-pill-sub {{
  font-size: 12px;
  color: #e2e8f0;
  font-weight: 500;
}}

.hero-spacer {{
  width: 100%;
  height: 250px;
  position: relative;
  z-index: 5;
}}

.bottom-content {{
  position: relative;
  z-index: 10;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  background: linear-gradient(to top, rgba(6, 11, 23, 0.98) 60%, rgba(6, 11, 23, 0.8) 85%, transparent 100%);
  padding: 16px 20px 0;
  border-radius: 24px;
}}

.hero-title {{
  font-size: 58px;
  font-weight: 900;
  letter-spacing: -0.5px;
  line-height: 1.15;
  background: linear-gradient(135deg, #ffffff 20%, #e0f2fe 55%, #38bdf8 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  filter: drop-shadow(0 4px 20px rgba(56, 189, 248, 0.4));
  margin-bottom: 6px;
}}

.hero-subtitle {{
  font-size: 19px;
  font-weight: 600;
  color: #94a3b8;
  letter-spacing: 0.5px;
  margin-bottom: 20px;
}}

.hero-subtitle span {{
  color: #38bdf8;
}}

.tags-row {{
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px;
  max-width: 680px;
  margin-bottom: 22px;
}}

.tag-item {{
  background: rgba(15, 23, 42, 0.8);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 9999px;
  padding: 6px 14px;
  font-size: 13px;
  font-weight: 600;
  color: #e2e8f0;
  display: flex;
  align-items: center;
  gap: 6px;
  backdrop-filter: blur(8px);
}}

.tag-item span {{
  color: #38bdf8;
}}

.domain-badge {{
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 9999px;
  padding: 8px 22px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.3);
}}

.domain-icon {{
  color: #38bdf8;
  display: flex;
}}

.domain-name {{
  font-size: 15px;
  font-weight: 800;
  letter-spacing: 1px;
  color: #ffffff;
}}

.domain-highlight {{
  color: #38bdf8;
}}
</style>
</head>
<body>
  <div class="bg-square"></div>
  <div class="ambient-glow"></div>
  <div class="grid-overlay"></div>

  <div class="top-header">
    <div class="brand-pill">
      <div class="pulse-dot"></div>
      <span class="brand-pill-text">TGWIKI</span>
      <span style="color: rgba(255,255,255,0.25)">|</span>
      <span class="brand-pill-sub">Telegram 电报知识库</span>
    </div>
  </div>

  <div class="hero-spacer"></div>

  <div class="bottom-content">
    <h1 class="hero-title">电报宝典</h1>
    <div class="hero-subtitle">
      Telegram 中文全方位指南 <span>·</span> 进阶与避坑宝典
    </div>

    <div class="tags-row">
      <div class="tag-item"><span>✦</span> 客户端下载与汉化</div>
      <div class="tag-item"><span>✦</span> +86私聊限制解除</div>
      <div class="tag-item"><span>✦</span> 账号安全与防封号</div>
      <div class="tag-item"><span>✦</span> Premium与机器人</div>
    </div>

    <div class="domain-badge">
      <span class="domain-icon">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="10"></circle>
          <line x1="2" y1="12" x2="22" y2="12"></line>
          <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
        </svg>
      </span>
      <span class="domain-name">tg.<span class="domain-highlight">ygjc.cc</span></span>
    </div>
  </div>
</body>
</html>
"""

def main():
    path_1200 = os.path.join(TEMP_DIR, "og_1200.html")
    path_800 = os.path.join(TEMP_DIR, "og_800.html")

    with open(path_1200, "w", encoding="utf-8") as f:
        f.write(html_1200)

    with open(path_800, "w", encoding="utf-8") as f:
        f.write(html_800)

    chrome_candidates = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "google-chrome",
        "chromium"
    ]
    chrome_cmd = None
    for c in chrome_candidates:
        if os.path.exists(c) or subprocess.run(["which", c], capture_output=True).returncode == 0:
            chrome_cmd = c
            break

    if not chrome_cmd:
        print("Error: Google Chrome not found!")
        sys.exit(1)

    print(f"Using Chrome: {chrome_cmd}")

    og_image_path = os.path.join(ASSETS_DIR, "og-image.png")
    twitter_card_path = os.path.join(ASSETS_DIR, "twitter-card.png")
    square_image_path = os.path.join(ASSETS_DIR, "og-image-square.png")

    # Render 1200x630
    cmd_1200 = [
        chrome_cmd,
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        "--window-size=1200,630",
        f"--screenshot={og_image_path}",
        f"file://{path_1200}"
    ]
    subprocess.run(cmd_1200, check=True)
    subprocess.run(["cp", og_image_path, twitter_card_path], check=True)
    print(f"Rendered: {og_image_path} and {twitter_card_path}")

    # Render 800x800
    cmd_800 = [
        chrome_cmd,
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        "--window-size=800,800",
        f"--screenshot={square_image_path}",
        f"file://{path_800}"
    ]
    subprocess.run(cmd_800, check=True)
    print(f"Rendered: {square_image_path}")

if __name__ == "__main__":
    main()
