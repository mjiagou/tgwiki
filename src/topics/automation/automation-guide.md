---
title: Telegram 自动化工作流：RSS、通知、跨平台集成与无人值守运营
shortTitle: 自动化工作流
description: 手把手教你构建 Telegram 自动化工作流。涵盖 RSS 自动推送、GitHub/监控通知、Make/n8n 集成、跨平台同步发帖、定时发送等实用场景，附完整代码和配置。
icon: gear
category:
  - 进阶教程
tag:
  - 自动化
  - RSS
  - Webhook
  - n8n
  - 工作流
head:
  - - meta
    - name: keywords
      content: Telegram自动化,Telegram RSS,Telegram自动推送,Telegram Webhook,Telegram n8n,Telegram Make,Telegram定时发送,Telegram机器人通知,Telegram跨平台,Telegram集成,TG自动化,TG RSS,TG自动推送,电报自动化,电报RSS,电报自动推送
---

# Telegram 自动化工作流：RSS、通知、跨平台集成与无人值守运营

每天手动转发内容到频道太累？GitHub 提交、服务器报警、网站更新都要手动通知？本文教你用自动化工具打通 Telegram 与外部世界，实现内容自动推送、告警通知、跨平台同步，让频道和群组实现无人值守运营。

---

## 一、自动化场景概览

### 1.1 为什么要自动化

| 痛点 | 手动操作 | 自动化后 |
|:---|:---|:---|
| 频道每日更新 | 手动找内容、编辑、发送 | RSS 自动抓取并推送 |
| 代码提交通知 | 手动截图发群 | GitHub Webhook 自动通知 |
| 服务器告警 | 登录服务器查看 | 异常自动推送到群 |
| 多平台分发 | 每个平台手动发 | 一次发布，多平台同步 |
| 定时公告 | 设闹钟提醒自己发 | 定时自动发送 |
| 新成员欢迎 | 手动逐个回复 | Bot 自动欢迎并验证 |

### 1.2 自动化工具选型

| 工具 | 类型 | 难度 | 费用 | 适合 |
|:---|:---|:---:|:---|:---|
| **Bot API** | 自开发 | ⭐⭐⭐ | 免费 | 完全定制的场景 |
| **RSS Bot** | 现成 Bot | ⭐ | 免费 | RSS 订阅推送 |
| **Make (Integromat)** | 可视化平台 | ⭐⭐ | 免费额度 | 零代码集成 |
| **n8n** | 自部署工作流 | ⭐⭐⭐ | 开源免费 | 隐私敏感场景 |
| **Zapier** | 可视化平台 | ⭐⭐ | 付费为主 | 企业用户 |
| **GitHub Actions** | CI/CD | ⭐⭐⭐ | 免费 | 开发者场景 |
| **crontab + 脚本** | 系统级 | ⭐⭐⭐ | 免费 | 服务器定时任务 |

---

## 二、RSS 自动推送：让频道自动更新

### 2.1 使用现成 RSS Bot（零代码）

最简单的方式：直接使用现成的 RSS 订阅 Bot。

**推荐 Bot：** [@TheFeederBot](https://t.me/TheFeederBot) / [@rss2tg_bot](https://t.me/rss2tg_bot)

**操作步骤：**

1. 在频道中添加 Bot 为管理员，给予发送消息权限
2. 私聊 Bot，发送 `/subscribe <RSS链接>`
3. Bot 会自动监控 RSS 更新并推送到频道

::: tip 选择 RSS 源
常用的 RSS 源包括：
- 新闻网站 RSS（如 BBC、Reuters）
- 博客 RSS（如 Medium、个人博客）
- GitHub Release RSS（`https://github.com/用户/仓库/releases.atom`）
- YouTube 频道 RSS（`https://www.youtube.com/feeds/videos.xml?channel_id=频道ID`）
- Reddit 子版 RSS（`https://www.reddit.com/r/子版名/.rss`）
:::

### 2.2 自建 RSS 推送 Bot（Python）

如果需要更多控制权，可以自建 RSS Bot。

```python
"""
RSS to Telegram Bot
功能：监控 RSS 源，有新文章时自动推送到 Telegram 频道
依赖：pip install feedparser python-telegram-bot
"""

import asyncio
import feedparser
import os
import logging
from datetime import datetime, timedelta
from telegram import Bot

# ========== 配置 ==========
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = os.environ.get("CHANNEL_ID", "@your_channel")  # 频道用户名或 -100 开头的 ID
RSS_FEEDS = [
    "https://example.com/feed.xml",
    "https://github.com/python-telegram-bot/python-telegram-bot/releases.atom",
]
CHECK_INTERVAL = 300  # 每 5 分钟检查一次

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
logger = logging.getLogger(__name__)

bot = Bot(token=BOT_TOKEN)
posted_links = set()  # 已推送的链接（生产环境建议用数据库）

def format_entry(entry) -> str:
    """格式化 RSS 条目为 Telegram 消息"""
    title = entry.get("title", "无标题")
    link = entry.get("link", "")
    summary = entry.get("summary", "")

    # 清理 HTML 标签（简单版）
    import re
    summary = re.sub(r'<[^>]+>', '', summary)[:200]

    source = entry.get("source", {}).get("title", "RSS更新")

    return (
        f"📢 *{title}*\n\n"
        f"{summary}...\n\n"
        f"🔗 [阅读原文]({link})\n"
        f"📰 来源：{source}"
    )

async def check_feeds():
    """检查所有 RSS 源，推送新内容"""
    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries[:5]:  # 每次最多检查 5 条
            link = entry.get("link", "")
            if link and link not in posted_links:
                try:
                    message = format_entry(entry)
                    await bot.send_message(
                        chat_id=CHANNEL_ID,
                        text=message,
                        parse_mode="Markdown",
                        disable_web_page_preview=False,
                    )
                    posted_links.add(link)
                    logger.info(f"已推送：{entry.get('title', '未知标题')}")
                    await asyncio.sleep(2)  # 避免发送过快
                except Exception as e:
                    logger.error(f"推送失败：{e}")

async def main():
    logger.info("🤖 RSS Bot 已启动")
    while True:
        try:
            await check_feeds()
        except Exception as e:
            logger.error(f"检查异常：{e}")
        await asyncio.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    asyncio.run(main())
```

### 2.3 使用 Node-RED 可视化搭建

[Node-RED](https://nodered.org/) 是一个可视化流程编辑器，适合不写代码也能搭建自动化：

```
[RSS 输入节点] ──► [过滤/格式化节点] ──► [Telegram 输出节点]
     ↑                                        ↓
  定时触发                               推送到频道
```

**配置步骤：**

1. 部署 Node-RED（Docker 一行命令）
2. 安装 `node-red-node-telegrambot` 插件
3. 拖入 `inject` 节点设置定时触发
4. 拖入 `rss` 节点配置 RSS 源
5. 拖入 `function` 节点格式化消息
6. 拖入 `telegram sender` 节点配置 Bot Token 和频道 ID
7. 连接节点并部署

---

## 三、通知集成：把外部事件推到 Telegram

### 3.1 GitHub/GitLab 提交通知

**方法一：GitHub Webhook + Cloudflare Worker（免费）**

```javascript
// GitHub Webhook → Cloudflare Worker → Telegram
export default {
  async fetch(request, env) {
    const payload = await request.json();
    const event = request.headers.get("X-GitHub-Event");

    let message = "";

    if (event === "push") {
      const repo = payload.repository.full_name;
      const branch = payload.ref.replace("refs/heads/", "");
      const commits = payload.commits.map(c => `  • ${c.message.split('\n')[0]}`).join('\n');
      message = `🔧 *新提交*\n📦 ${repo} (${branch})\n👤 ${payload.pusher.name}\n\n${commits}`;
    } else if (event === "pull_request") {
      const pr = payload.pull_request;
      message = `🔀 *PR ${payload.action}*\n📦 ${payload.repository.full_name}\n*${pr.title}*\n👤 ${pr.user.login}\n🔗 ${pr.html_url}`;
    } else if (event === "release") {
      const release = payload.release;
      message = `🚀 *新版本发布*\n📦 ${payload.repository.full_name}\n*${release.name || release.tag_name}*\n${release.body?.slice(0, 500) || ""}`;
    }

    if (message) {
      await fetch(`https://api.telegram.org/bot${env.BOT_TOKEN}/sendMessage`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          chat_id: env.CHAT_ID,
          text: message,
          parse_mode: "Markdown",
        }),
      });
    }
    return new Response("OK");
  },
};
```

**方法二：GitHub Actions（无需服务器）**

```yaml
# .github/workflows/notify-telegram.yml
name: Notify Telegram
on:
  push:
    branches: [main]
  pull_request:
    types: [opened, closed]

jobs:
  notify:
    runs-on: ubuntu-latest
    steps:
      - name: Send Telegram notification
        uses: appleboy/telegram-action@master
        with:
          to: ${{ secrets.TELEGRAM_CHAT_ID }}
          token: ${{ secrets.TELEGRAM_BOT_TOKEN }}
          format: markdown
          message: |
            🔧 *${{ github.event_name }}* on ${{ github.repository }}
            👤 ${{ github.actor }}
            📝 ${{ github.event.head_commit.message || github.event.pull_request.title }}
            🔗 ${{ github.event.head_commit.url || github.event.pull_request.html_url }}
```

### 3.2 服务器监控告警

用 Shell 脚本监控服务器状态，异常时推送到 Telegram：

```bash
#!/bin/bash
# server-monitor.sh —— 服务器监控脚本

BOT_TOKEN="YOUR_BOT_TOKEN"
CHAT_ID="YOUR_CHAT_ID"
ALERT_URL="https://api.telegram.org/bot${BOT_TOKEN}/sendMessage"

# 发送告警函数
send_alert() {
    curl -s -X POST "$ALERT_URL" \
        -d chat_id="$CHAT_ID" \
        -d text="$1" \
        -d parse_mode="Markdown"
}

# 检查 CPU 使用率
CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'.' -f1)
if [ "$CPU_USAGE" -gt 80 ]; then
    send_alert "⚠️ *CPU 告警*
🖥️ 服务器：$(hostname)
📊 CPU 使用率：${CPU_USAGE}%
⏰ 时间：$(date '+%Y-%m-%d %H:%M:%S')"
fi

# 检查磁盘使用率
DISK_USAGE=$(df / | tail -1 | awk '{print $5}' | tr -d '%')
if [ "$DISK_USAGE" -gt 90 ]; then
    send_alert "🚨 *磁盘告警*
🖥️ 服务器：$(hostname)
📊 根分区使用率：${DISK_USAGE}%
⏰ 时间：$(date '+%Y-%m-%d %H:%M:%S')"
fi

# 检查内存使用率
MEM_USAGE=$(free | grep Mem | awk '{printf("%.0f", $3/$2 * 100)}')
if [ "$MEM_USAGE" -gt 85 ]; then
    send_alert "⚠️ *内存告警*
🖥️ 服务器：$(hostname)
📊 内存使用率：${MEM_USAGE}%
⏰ 时间：$(date '+%Y-%m-%d %H:%M:%S')"
fi

# 检查关键服务是否运行
for service in nginx postgresql; do
    if ! systemctl is-active --quiet "$service"; then
        send_alert "🚨 *服务异常*
🖥️ 服务器：$(hostname)
❌ 服务 $service 已停止
⏰ 时间：$(date '+%Y-%m-%d %H:%M:%S')"
    fi
done
```

配合 crontab 定时执行：

```bash
# 每 5 分钟检查一次
*/5 * * * * /opt/scripts/server-monitor.sh

# 每天早上 8 点发送日报
0 8 * * * /opt/scripts/server-daily-report.sh
```

### 3.3 网站更新监控

监控网站内容变化并通知：

```python
"""
网站内容监控 —— 检测页面变化并通知
依赖：pip install requests beautifulsoup4
"""
import requests
from bs4 import BeautifulSoup
import hashlib
import os
import json
import asyncio
from telegram import Bot

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

# 监控配置
MONITOR_CONFIG = [
    {
        "name": "产品更新页",
        "url": "https://example.com/changelog",
        "selector": ".changelog-content",  # CSS 选择器
        "last_hash": None,  # 上次内容哈希
    }
]

async def check_and_notify():
    bot = Bot(token=BOT_TOKEN)
    config_path = "monitor_state.json"

    # 加载上次状态
    try:
        with open(config_path) as f:
            saved_state = json.load(f)
    except FileNotFoundError:
        saved_state = {}

    for item in MONITOR_CONFIG:
        try:
            resp = requests.get(item["url"], timeout=10)
            soup = BeautifulSoup(resp.text, "html.parser")
            content = soup.select_one(item["selector"])
            if not content:
                continue

            text = content.get_text(strip=True)
            current_hash = hashlib.md5(text.encode()).hexdigest()
            saved_hash = saved_state.get(item["name"], {}).get("hash")

            if saved_hash and current_hash != saved_hash:
                # 内容有变化，发送通知
                message = (
                    f"🔔 *{item['name']} 有更新！*\n\n"
                    f"🔗 [查看页面]({item['url']})\n"
                    f"⏰ {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M')}"
                )
                await bot.send_message(
                    chat_id=CHAT_ID,
                    text=message,
                    parse_mode="Markdown"
                )

            saved_state[item["name"]] = {"hash": current_hash}
        except Exception as e:
            print(f"监控 {item['name']} 出错：{e}")

    # 保存状态
    with open(config_path, "w") as f:
        json.dump(saved_state, f, indent=2)

if __name__ == "__main__":
    asyncio.run(check_and_notify())
```

---

## 四、Make (Integromat) 可视化集成

[Make](https://www.make.com/)（原 Integromat）是一个强大的可视化自动化平台，无需写代码就能创建复杂的工作流。

### 4.1 创建 Telegram Bot 模块

1. 在 Make 中创建新场景
2. 添加 **Telegram Bot** 模块
3. 选择 **Create a webhook** 连接 Bot
4. 输入 Bot Token 完成连接

### 4.2 实战：RSS → 翻译 → 推送到频道

```
[定时触发器] ──► [RSS 检查] ──► [DeepL 翻译] ──► [Telegram 发送消息]
                      └──► [过滤：只推送含关键词的]
```

**配置步骤：**

1. **定时触发器**：设置每小时执行一次
2. **RSS 模块**：输入 RSS 源地址
3. **过滤器**：设置条件，如标题包含 "Telegram"
4. **DeepL 模块**：将英文标题翻译成中文
5. **Telegram 模块**：选择 "Send a Message"，填入频道 ID 和消息内容

### 4.3 实战：Google Sheets → Telegram 通知

适合团队协作场景：表格中新增行时自动通知群组。

```
[Google Sheets 新行] ──► [格式化消息] ──► [Telegram 群通知]
```

**消息模板：**
```
📋 新任务分配
👤 负责人：{{1.负责人}}
📝 任务：{{1.任务描述}}
📅 截止日期：{{1.截止日期}}
```

### 4.4 实战：Telegram 消息 → 存入 Notion

反向集成：在 Telegram 中发消息，自动存入 Notion 数据库。

```
[Telegram 监听消息] ──► [解析内容] ──► [Notion 创建页面]
```

---

## 五、n8n 自部署工作流

[n8n](https://n8n.io/) 是开源的自动化工具，可以自己部署，数据完全掌控。

### 5.1 Docker 部署 n8n

```bash
# 创建 n8n 数据目录
mkdir -p ~/n8n/data

# 启动 n8n 容器
docker run -d \
  --name n8n \
  -p 5678:5678 \
  -v ~/n8n/data:/home/node/.n8n \
  -e N8N_BASIC_AUTH_ACTIVE=true \
  -e N8N_BASIC_AUTH_USER=admin \
  -e N8N_BASIC_AUTH_PASSWORD=your_password \
  -e GENERIC_TIMEZONE=Asia/Shanghai \
  --restart always \
  n8nio/n8n
```

访问 `http://服务器IP:5678` 即可使用。

### 5.2 实战：多频道同步发布

在 n8n 中创建工作流，一次发送同时推送到多个频道：

```json
{
  "nodes": [
    {
      "parameters": {
        "chatId": "@channel_1",
        "text": "={{ $json.message }}",
        "additionalFields": {}
      },
      "name": "发送到频道1",
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1
    },
    {
      "parameters": {
        "chatId": "@channel_2",
        "text": "={{ $json.message }}",
        "additionalFields": {}
      },
      "name": "发送到频道2",
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1
    }
  ]
}
```

### 5.3 实战：Telegram → AI 处理 → 回复

将用户消息交给 AI 处理后自动回复：

```
[Telegram Webhook 接收消息]
        │
        ▼
[HTTP Request → AI API（OpenAI/DeepSeek）]
        │
        ▼
[Telegram 回复消息]
```

---

## 六、定时发送与内容排期

### 6.1 Python 定时发送器

```python
"""
Telegram 定时消息发送器
功能：按预定时间自动发送消息到频道/群组
依赖：pip install python-telegram-bot APScheduler
"""

import os
import asyncio
from datetime import datetime
from telegram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = os.environ.get("CHANNEL_ID", "@your_channel")
bot = Bot(token=BOT_TOKEN)

# 定时任务列表
SCHEDULED_MESSAGES = [
    {
        "time": "09:00",  # 每天 9:00 发送
        "text": "🌅 早安！今天是 {date}，祝大家一切顺利！",
    },
    {
        "time": "12:00",
        "text": "🍽️ 午休时间到啦，记得吃饭休息~",
    },
    {
        "time": "18:00",
        "text": "🌆 今天的工作快结束了，加油收尾！",
    },
    {
        "time": "22:00",
        "text": "🌙 晚安时间，明天见！",
    },
]

async def send_scheduled_message(text: str):
    """发送定时消息"""
    now = datetime.now()
    formatted_text = text.format(date=now.strftime("%Y年%m月%d日"))
    await bot.send_message(
        chat_id=CHANNEL_ID,
        text=formatted_text,
    )
    print(f"✅ 已发送：{formatted_text}")

async def main():
    scheduler = AsyncIOScheduler()

    for msg in SCHEDULED_MESSAGES:
        hour, minute = msg["time"].split(":")
        scheduler.add_job(
            send_scheduled_message,
            "cron",
            hour=int(hour),
            minute=int(minute),
            args=[msg["text"]],
            id=f"msg_{msg['time']}",
        )

    scheduler.start()
    print("⏰ 定时发送器已启动，按 Ctrl+C 停止")

    # 保持运行
    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
```

### 6.2 一次性定时发送（Bash 版）

适合简单的定时提醒场景：

```bash
#!/bin/bash
# delayed-send.sh —— 延迟发送消息
# 用法：./delayed-send.sh "消息内容" "2026-01-15 10:00"

MESSAGE="$1"
SEND_TIME="$2"
BOT_TOKEN="YOUR_BOT_TOKEN"
CHAT_ID="YOUR_CHAT_ID"

# 转换为时间戳
TARGET_TS=$(date -d "$SEND_TIME" +%s 2>/dev/null || date -j -f "%Y-%m-%d %H:%M" "$SEND_TIME" +%s)
NOW_TS=$(date +%s)
WAIT_SECONDS=$((TARGET_TS - NOW_TS))

if [ "$WAIT_SECONDS" -le 0 ]; then
    echo "指定时间已过"
    exit 1
fi

echo "将在 ${WAIT_SECONDS} 秒后发送消息..."
sleep "$WAIT_SECONDS"

curl -s -X POST "https://api.telegram.org/bot${BOT_TOKEN}/sendMessage" \
    -d chat_id="$CHAT_ID" \
    -d text="$MESSAGE" \
    -d parse_mode="Markdown"

echo "✅ 消息已发送"
```

### 6.3 内容排期表（Python + SQLite）

对于需要管理大量排期内容的频道，可以用数据库管理：

```python
import sqlite3
from datetime import datetime

def init_schedule_db():
    conn = sqlite3.connect("schedule.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS scheduled_posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            channel_id TEXT NOT NULL,
            content TEXT NOT NULL,
            scheduled_time TIMESTAMP NOT NULL,
            sent INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def add_scheduled_post(channel_id, content, scheduled_time):
    conn = sqlite3.connect("schedule.db")
    conn.execute(
        "INSERT INTO scheduled_posts (channel_id, content, scheduled_time) VALUES (?, ?, ?)",
        (channel_id, content, scheduled_time)
    )
    conn.commit()
    conn.close()
    print(f"✅ 已添加排期：{scheduled_time}")

def get_pending_posts():
    conn = sqlite3.connect("schedule.db")
    cursor = conn.execute(
        "SELECT id, channel_id, content FROM scheduled_posts "
        "WHERE sent = 0 AND scheduled_time <= ? ORDER BY scheduled_time",
        (datetime.now().strftime("%Y-%m-%d %H:%M:%S"),)
    )
    posts = cursor.fetchall()
    conn.close()
    return posts

def mark_as_sent(post_id):
    conn = sqlite3.connect("schedule.db")
    conn.execute("UPDATE scheduled_posts SET sent = 1 WHERE id = ?", (post_id,))
    conn.commit()
    conn.close()

# 使用示例
init_schedule_db()
add_scheduled_post("@my_channel", "📢 今日推荐：...", "2026-01-15 10:00:00")
add_scheduled_post("@my_channel", "🔧 工具分享：...", "2026-01-15 14:00:00")
```

---

## 七、跨平台同步：一次发布多平台推送

### 7.1 Telegram + 微信公众号 + Twitter 同步

```python
"""
跨平台内容同步发布器
支持：Telegram、Twitter、Discord
"""

import os
import requests
from telegram import Bot

class CrossPlatformPublisher:
    def __init__(self):
        self.tg_bot = Bot(token=os.environ.get("BOT_TOKEN"))
        self.tg_channel = os.environ.get("CHANNEL_ID")
        self.discord_webhook = os.environ.get("DISCORD_WEBHOOK_URL")
        self.twitter_bearer = os.environ.get("TWITTER_BEARER_TOKEN")

    async def publish(self, content: str, image_path: str = None):
        """同时发布到多个平台"""
        results = {}

        # Telegram
        try:
            if image_path:
                with open(image_path, "rb") as f:
                    await self.tg_bot.send_photo(
                        chat_id=self.tg_channel,
                        photo=f,
                        caption=content,
                    )
            else:
                await self.tg_bot.send_message(
                    chat_id=self.tg_channel,
                    text=content,
                )
            results["telegram"] = "✅"
        except Exception as e:
            results["telegram"] = f"❌ {e}"

        # Discord
        if self.discord_webhook:
            try:
                requests.post(self.discord_webhook, json={"content": content})
                results["discord"] = "✅"
            except Exception as e:
                results["discord"] = f"❌ {e}"

        return results

# 使用
# publisher = CrossPlatformPublisher()
# results = await publisher.publish("🎉 新文章发布啦！[链接](https://...)")
# print(results)
```

### 7.2 使用 IFTTT 跨平台

[IFTTT](https://ifttt.com/) 提供简单的小程序式自动化：

**典型配方：**

| 触发条件 | 执行动作 |
|:---|:---|
| YouTube 新视频 | 发送到 Telegram 频道 |
| RSS 有更新 | 发送到 Telegram |
| Telegram 频道新消息 | 同步到 Twitter |
| GitHub 新 Release | 通知 Telegram 群 |

---

## 八、群组自动化：欢迎与审核

### 8.1 自动欢迎新成员

```python
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ChatMemberHandler, ContextTypes

WELCOME_TEXT = """
👋 欢迎 {name} 加入我们的群组！

📖 请先阅读群规：
1. 友好交流，禁止人身攻击
2. 禁止发布广告和垃圾信息
3. 技术问题请详细描述并附上代码/截图
4. 使用话题功能发帖

点击下方按钮确认你已阅读群规：
"""

async def welcome_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = update.chat_member
    if result.new_chat_member.status in ["member", "restricted"]:
        user = result.new_chat_member.user
        chat_id = result.chat.id

        # 限制新成员发言（需要先设为受限状态，通过验证后解除）
        keyboard = [[InlineKeyboardButton("✅ 我已阅读群规", callback_data=f"verify_{user.id}")]]

        await context.bot.send_message(
            chat_id=chat_id,
            text=WELCOME_TEXT.format(name=user.first_name),
            reply_markup=InlineKeyboardMarkup(keyboard),
            reply_to_message_id=None,
        )

async def verify_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = int(query.data.split("_")[1])
    chat_id = query.message.chat_id

    # 解除新成员限制
    await context.bot.restrict_chat_member(
        chat_id=chat_id,
        user_id=user_id,
        permissions={
            "can_send_messages": True,
            "can_send_media_messages": True,
            "can_send_other_messages": True,
        },
    )
    await query.edit_message_text(f"✅ 验证成功，欢迎入群！")

app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()
app.add_handler(ChatMemberHandler(welcome_new_member, ChatMemberHandler.CHAT_MEMBER))
app.add_handler(CallbackQueryHandler(verify_member))
app.run_polling(allowed_updates=["chat_member", "message", "callback_query"])
```

### 8.2 关键词自动回复

```python
from telegram.ext import MessageHandler, filters

# 关键词回复规则
AUTO_REPLIES = {
    "帮助": "📖 查看完整使用帮助：/help",
    "教程": "📚 教程汇总：https://your-wiki.com",
    "bot": "🤖 Bot 开发教程：/guide",
    "ton": "💰 TON 生态指南：https://your-wiki.com/topics/ton/",
}

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    for keyword, reply in AUTO_REPLIES.items():
        if keyword in text:
            await update.message.reply_text(reply)
            return

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))
```

---

## 九、Webhook 服务器搭建

如果需要接收来自外部服务的 Webhook 并转发到 Telegram，可以搭建一个轻量级 Webhook 服务器。

### 9.1 Python Flask Webhook 服务器

```python
"""
Telegram Webhook 中转服务器
功能：接收外部 Webhook，格式化后转发到 Telegram
依赖：pip install flask requests
"""

from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
TG_API = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

def send_telegram(text, parse_mode="Markdown"):
    """发送消息到 Telegram"""
    requests.post(TG_API, json={
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": parse_mode,
    })

# ========== Webhook 路由 ==========

@app.route("/webhook/github", methods=["POST"])
def github_webhook():
    """GitHub Webhook"""
    data = request.json
    event = request.headers.get("X-GitHub-Event", "")

    if event == "push":
        repo = data["repository"]["full_name"]
        sender = data["pusher"]["name"]
        commits = len(data.get("commits", []))
        send_telegram(f"🔧 {repo} 新提交\n👤 {sender}\n📝 {commits} 个提交")

    elif event == "release":
        release = data["release"]
        send_telegram(f"🚀 {data['repository']['full_name']} 发布新版本\n*{release['tag_name']}*\n{release.get('body', '')[:300]}")

    return jsonify({"status": "ok"})

@app.route("/webhook/uptime", methods=["POST"])
def uptime_alert():
    """网站监控告警"""
    data = request.json
    alert_type = data.get("alertType", "unknown")
    site = data.get("site", "unknown")
    state = data.get("alertState", "unknown")

    if state == "down":
        emoji = "🚨"
    else:
        emoji = "✅"

    send_telegram(f"{emoji} 网站监控告警\n🌐 {site}\n状态：{state}\n类型：{alert_type}")
    return jsonify({"status": "ok"})

@app.route("/webhook/custom", methods=["POST"])
def custom_webhook():
    """通用 Webhook —— 自定义消息"""
    data = request.json
    title = data.get("title", "通知")
    body = data.get("body", "")
    send_telegram(f"📢 *{title}*\n\n{body}")
    return jsonify({"status": "ok"})

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

### 9.2 使用 Caddy 反向代理（自动 HTTPS）

```Caddyfile
# Caddyfile —— 自动获取 HTTPS 证书
webhook.yourdomain.com {
    reverse_proxy localhost:5000
}
```

```bash
# 启动 Caddy
caddy start
# Caddy 会自动申请 Let's Encrypt 证书
```

---

## 十、安全注意事项

### 10.1 Webhook 安全

```python
import hmac
import hashlib

# 验证 GitHub Webhook 签名
def verify_github_signature(payload_body: bytes, signature_header: str, secret: str) -> bool:
    """验证 GitHub Webhook 签名，防止伪造请求"""
    expected = "sha256=" + hmac.new(
        secret.encode(), payload_body, hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(expected, signature_header)

# 在 Flask 中使用
@app.route("/webhook/github", methods=["POST"])
def github_webhook():
    signature = request.headers.get("X-Hub-Signature-256", "")
    if not verify_github_signature(request.data, signature, WEBHOOK_SECRET):
        return jsonify({"error": "Invalid signature"}), 403
    # ... 处理逻辑
```

### 10.2 敏感信息管理

| 信息 | 存储方式 | 示例 |
|:---|:---|:---|
| Bot Token | 环境变量 | `export BOT_TOKEN=xxx` |
| 频道 ID | 环境变量 | `export CHAT_ID=@channel` |
| API Key | 密钥管理服务 | AWS Secrets Manager |
| Webhook Secret | 环境变量 | `export WEBHOOK_SECRET=xxx` |
| 数据库密码 | 环境变量 | `export DB_PASSWORD=xxx` |

### 10.3 防滥用措施

```python
from collections import defaultdict
from datetime import datetime

# 速率限制：每个来源每分钟最多 10 条
rate_limit = defaultdict(list)
RATE_LIMIT_PER_MINUTE = 10

def check_rate_limit(source: str) -> bool:
    now = datetime.now()
    timestamps = rate_limit[source]
    # 清理一分钟前的记录
    rate_limit[source] = [t for t in timestamps if (now - t).seconds < 60]
    if len(rate_limit[source]) >= RATE_LIMIT_PER_MINUTE:
        return False
    rate_limit[source].append(now)
    return True
```

---

## 十一、自动化方案对比与推荐

### 11.1 方案选型矩阵

```
你的需求是什么？
    │
    ├── 只需要 RSS 推送
    │   └── ✅ 用现成 RSS Bot（@TheFeederBot）
    │
    ├── 需要简单通知（GitHub/监控）
    │   └── ✅ GitHub Actions / Shell 脚本
    │
    ├── 需要多服务集成，不想写代码
    │   └── ✅ Make (免费额度够用)
    │
    ├── 需要完全掌控数据
    │   └── ✅ 自部署 n8n
    │
    ├── 需要高度定制
    │   └── ✅ 自己写 Python 脚本
    │
    └── 需要定时/排期发送
        └── ✅ APScheduler + SQLite
```

### 11.2 成本对比

| 方案 | 月成本 | 优点 | 缺点 |
|:---|:---|:---|---|
| RSS Bot | 免费 | 零配置 | 功能有限 |
| Make 免费版 | 免费（1000次/月） | 功能强大 | 额度有限 |
| n8n 自部署 | VPS 费用 ($5) | 无限制 | 需维护 |
| Python 脚本 | VPS 费用 ($5) | 完全可控 | 需开发 |
| GitHub Actions | 免费 | 无需服务器 | 仅限 GitHub |
| Caddy + Flask | VPS 费用 ($5) | 灵活 | 需开发 |

---

## 十二、实战案例：全自动频道运营方案

把前面的模块组合起来，打造一个全自动运营的技术资讯频道：

### 12.1 架构设计

```
┌─────────────┐     ┌──────────────┐     ┌───────────────┐
│  RSS 源      │────►│  Python 脚本  │────►│  Telegram 频道 │
│  GitHub     │     │  (过滤+翻译)  │     │               │
│  Hacker News│     │              │     │  + 定时早安    │
│  V2EX       │     │  + 排期发送   │     │  + RSS 推送    │
└─────────────┘     │  + 去重       │     │  + 周报汇总    │
                    └──────────────┘     └───────────────┘
                           │
                    ┌──────┴──────┐
                    │  SQLite DB  │
                    │  (排期+去重) │
                    └─────────────┘
```

### 12.2 核心代码

```python
"""
全自动频道运营机器人
功能：RSS 聚合 + 翻译 + 去重 + 排期 + 定时发送
"""

import asyncio
import feedparser
import sqlite3
import hashlib
import logging
from datetime import datetime
from telegram import Bot

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

class AutoChannelBot:
    def __init__(self, bot_token, channel_id, db_path="auto_channel.db"):
        self.bot = Bot(token=bot_token)
        self.channel_id = channel_id
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS posted (
                hash TEXT PRIMARY KEY,
                title TEXT,
                url TEXT,
                posted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS scheduled (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL,
                scheduled_time TIMESTAMP NOT NULL,
                sent INTEGER DEFAULT 0
            )
        """)
        conn.commit()
        conn.close()

    def is_posted(self, url: str) -> bool:
        h = hashlib.md5(url.encode()).hexdigest()
        conn = sqlite3.connect(self.db_path)
        cursor = conn.execute("SELECT 1 FROM posted WHERE hash = ?", (h,))
        result = cursor.fetchone() is not None
        conn.close()
        return result

    def mark_posted(self, title: str, url: str):
        h = hashlib.md5(url.encode()).hexdigest()
        conn = sqlite3.connect(self.db_path)
        conn.execute("INSERT OR IGNORE INTO posted (hash, title, url) VALUES (?, ?, ?)",
                      (h, title, url))
        conn.commit()
        conn.close()

    async def check_rss_and_post(self, feeds: list):
        """检查 RSS 并推送新文章"""
        for feed_url in feeds:
            feed = feedparser.parse(feed_url)
            for entry in feed.entries[:3]:
                url = entry.get("link", "")
                if not url or self.is_posted(url):
                    continue

                title = entry.get("title", "未知")
                summary = entry.get("summary", "")[:200]
                import re
                summary = re.sub(r'<[^>]+>', '', summary)

                message = f"📰 *{title}*\n\n{summary}...\n\n🔗 [阅读原文]({url})"

                try:
                    await self.bot.send_message(
                        chat_id=self.channel_id,
                        text=message,
                        parse_mode="Markdown",
                    )
                    self.mark_posted(title, url)
                    logging.info(f"推送：{title}")
                    await asyncio.sleep(5)  # 间隔 5 秒
                except Exception as e:
                    logging.error(f"推送失败：{e}")

    async def send_scheduled(self):
        """发送排期消息"""
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        conn = sqlite3.connect(self.db_path)
        cursor = conn.execute(
            "SELECT id, content FROM scheduled WHERE sent = 0 AND scheduled_time <= ?",
            (now,)
        )
        for post_id, content in cursor.fetchall():
            try:
                await self.bot.send_message(
                    chat_id=self.channel_id,
                    text=content,
                    parse_mode="Markdown",
                )
                conn.execute("UPDATE scheduled SET sent = 1 WHERE id = ?", (post_id,))
                logging.info(f"排期消息已发送：#{post_id}")
            except Exception as e:
                logging.error(f"排期发送失败：{e}")
        conn.commit()
        conn.close()

    async def run(self, feeds: list, interval: int = 600):
        """主循环"""
        logging.info("🤖 全自动频道机器人已启动")
        while True:
            try:
                await self.check_rss_and_post(feeds)
                await self.send_scheduled()
            except Exception as e:
                logging.error(f"主循环异常：{e}")
            await asyncio.sleep(interval)

# 使用
if __name__ == "__main__":
    import os
    bot = AutoChannelBot(
        bot_token=os.environ["BOT_TOKEN"],
        channel_id=os.environ["CHANNEL_ID"],
    )
    feeds = [
        "https://hnrss.org/frontpage",
        "https://www.theverge.com/rss/index.xml",
        "https://github.com/python-telegram-bot/python-telegram-bot/releases.atom",
    ]
    asyncio.run(bot.run(feeds))
```

---

## 总结

本文覆盖了 Telegram 自动化的核心场景：

| 场景 | 推荐方案 | 难度 |
|:---|:---|:---:|
| RSS 自动推送 | RSS Bot / Python 脚本 | ⭐ |
| 代码提交通知 | GitHub Actions / Webhook | ⭐⭐ |
| 服务器监控告警 | Shell + crontab | ⭐⭐ |
| 可视化工作流 | Make / n8n | ⭐⭐ |
| 定时/排期发送 | APScheduler + SQLite | ⭐⭐ |
| 跨平台同步 | Python 多平台发布器 | ⭐⭐⭐ |
| 群组自动化 | Bot API + ChatMemberHandler | ⭐⭐⭐ |
| Webhook 中转 | Flask + Caddy | ⭐⭐⭐ |

**上手建议：**
1. **新手**：先用现成 RSS Bot 感受自动化
2. **进阶**：用 Make 搭建无代码工作流
3. **高级**：自建 Python 脚本 + n8n 实现完全掌控

自动化是 Telegram 运营的"降本增效"利器——把重复劳动交给机器，把创造力留给内容本身。

---

**相关阅读：**

- [Bot 开发实战教程](../bot/bot-dev-guide.md) — 从零开发 Telegram 机器人
- [API 入门指南](../../api-intro.md) — Bot API 与 MTProto API
- [AI 机器人完全指南](../ai/ai-bots.md) — 接入 AI 实现智能自动化
- [频道运营全攻略](../../createchannel.md) — 频道从零到一
- [变现实战指南](../../monetization.md) — 频道赚钱方法
- [Mini App 开发入门](../game/miniapp-dev.md) — 开发小程序