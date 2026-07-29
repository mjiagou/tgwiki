---
title: Telegram Bot 开发实战教程：从零构建一个功能完整的机器人
shortTitle: Bot 开发实战
description: 手把手教你用 Python 开发 Telegram 机器人。涵盖命令处理、内联键盘、会话状态、数据持久化、Webhook 部署的完整流程，附完整代码示例。
icon: code
category:
  - 开发者
tag:
  - Bot开发
  - Python
  - python-telegram-bot
  - Webhook
  - 教程
head:
  - - meta
    - name: keywords
      content: Telegram Bot开发,Telegram机器人开发,python-telegram-bot,Telegram Bot API,Telegram Bot教程,Telegram Webhook,Telegram机器人代码,TG Bot开发,电报机器人开发,Telegram Python
---

# Telegram Bot 开发实战教程：从零构建一个功能完整的机器人

已经通过 [@BotFather](https://t.me/botfather) 申请了 Bot Token，却不知道下一步怎么写代码？本文手把手教你用 Python 开发一个功能完整的 Telegram 机器人，从 Hello World 到上线部署，附全部代码。

---

## 一、准备工作

### 1.1 技术栈选择

| 语言 | 推荐库 | 优点 | 适合 |
|:---|:---|:---|:---|
| **Python** | `python-telegram-bot` | 生态最好、教程最多、异步支持 | 初学者首选 |
| **Node.js** | `telegraf` / `grammy` | 性能好、前后端统一技术栈 | JS 开发者 |
| **Go** | `telebot` | 性能极佳、部署简单 | 高性能场景 |
| **PHP** | `nutgram` | 传统部署方便 | PHP 开发者 |

本文使用 **Python + python-telegram-bot (v20+)**，它是目前最成熟的 Telegram Bot 开发库。

### 1.2 环境搭建

```bash
# 1. 确认 Python 版本（需要 3.9+）
python3 --version

# 2. 创建项目目录
mkdir my-tg-bot && cd my-tg-bot

# 3. 创建虚拟环境
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 4. 安装依赖
pip install python-telegram-bot

# 5. 创建主程序文件
touch bot.py
```

### 1.3 获取 Bot Token

如果你还没有 Bot Token，请先阅读 [机器人申请教程](../../createrobot.md) 获取。

::: danger 安全提醒
Bot Token 是机器人的"钥匙"，任何人拿到 Token 都能控制你的机器人。**绝对不要把 Token 写在代码里提交到 GitHub**，后面会教你怎么安全管理。
:::

---

## 二、Hello World：第一个机器人

### 2.1 最简代码

```python
# bot.py
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 替换为你的 Bot Token
BOT_TOKEN = "123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghi"

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"你好，{update.effective_user.first_name}！")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("hello", hello))
    app.run_polling()
```

### 2.2 运行测试

```bash
python bot.py
```

在 Telegram 中找到你的机器人，点击 **Start**，然后发送 `/hello`，机器人会回复"你好，XXX！"。

### 2.3 代码解析

| 组件 | 作用 |
|:---|:---|
| `ApplicationBuilder` | 创建 Bot 应用实例 |
| `CommandHandler` | 监听 `/命令`，如 `/hello` |
| `update` | 包含用户消息、聊天信息等数据 |
| `context` | 提供发送消息、存储数据等能力 |
| `run_polling()` | 使用 Long Polling 方式接收消息（开发阶段推荐） |

---

## 三、命令处理：让机器人听懂指令

### 3.1 常用命令处理器

```python
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

# /start 命令 —— 用户首次启动机器人时触发
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    welcome_text = (
        f"👋 你好 {update.effective_user.first_name}！\n\n"
        "我是你的专属机器人，以下是我能做的事：\n"
        "📝 /help —— 查看帮助\n"
        "🌡️ /weather <城市> —— 查询天气\n"
        "calculator /calc <表达式> —— 简易计算器\n"
        "📌 /setnote <内容> —— 保存笔记\n"
        "📋 /mynotes —— 查看我的笔记"
    )
    await update.message.reply_text(welcome_text)

# /help 命令
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = """
📖 **使用帮助**

| 命令 | 功能 |
|:---|:---|
| `/start` | 开始使用 |
| `/hello` | 打招呼 |
| `/weather 北京` | 查询天气 |
| `/calc 1+2*3` | 计算表达式 |
| `/setnote 记住买菜` | 保存笔记 |
| `/mynotes` | 查看笔记 |

有任何问题，直接发消息给我！
    """
    await update.message.reply_markdown(help_text)

# 带参数的命令：/weather 北京
async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await update.message.reply_text("用法：`/weather 城市名`\n例：`/weather 北京`", parse_mode="Markdown")
        return

    city = " ".join(context.args)
    # 这里用模拟数据演示，实际开发中接入天气 API
    await update.message.reply_text(f"🌤️ {city} 今天晴，25°C，湿度 60%")

# 简易计算器：/calc 1+2*3
async def calculator(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await update.message.reply_text("用法：`/calc 表达式`\n例：`/calc 1+2*3`", parse_mode="Markdown")
        return

    expression = " ".join(context.args)
    try:
        # 注意：生产环境中不要直接 eval 用户输入！
        # 这里仅做演示，实际应使用 ast.literal_eval 或安全的表达式解析库
        result = eval(expression, {"__builtins__": {}}, {})
        await update.message.reply_text(f"📊 计算结果：`{expression} = {result}`", parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text(f"❌ 计算出错：{e}")

# 注册所有命令处理器
app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("weather", weather))
app.add_handler(CommandHandler("calc", calculator))
app.run_polling()
```

### 3.2 设置命令菜单

在 [@BotFather](https://t.me/botfather) 中设置命令菜单，让用户点击即可使用：

```
/setcommands
选择你的机器人，发送：
start - 开始使用
help - 查看帮助
weather - 查询天气
calc - 简易计算器
setnote - 保存笔记
mynotes - 查看笔记
```

设置后，用户在聊天框点击 `/` 就能看到命令列表。

---

## 四、消息处理：回复用户的文字

除了 `/命令`，机器人还可以回复用户的普通文字消息。

```python
from telegram import Update
from telegram.ext import MessageHandler, filters, ContextTypes

# 回复纯文本消息
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_text = update.message.text
    user_name = update.effective_user.first_name

    # 关键词自动回复
    if "你好" in user_text or "hello" in user_text.lower():
        await update.message.reply_text(f"你好呀，{user_name}！😊")
    elif "天气" in user_text:
        await update.message.reply_text("请使用 `/weather 城市名` 命令查询天气，例如：`/weather 北京`", parse_mode="Markdown")
    elif "再见" in user_text:
        await update.message.reply_text(f"再见，{user_name}！期待下次见面 👋")
    else:
        # 默认回复：原样返回（Echo 机器人）
        await update.message.reply_text(f"你说了：{user_text}")

# 回复图片消息
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("📸 收到你的图片了！但我还不会处理图片，请发文字消息吧～")

# 注册消息处理器
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
```

**过滤器说明：**

| 过滤器 | 匹配内容 |
|:---|:---|
| `filters.TEXT` | 纯文本消息 |
| `filters.COMMAND` | 以 `/` 开头的命令消息 |
| `filters.PHOTO` | 图片消息 |
| `filters.Document.ALL` | 文件消息 |
| `filters.Sticker.ALL` | 贴纸消息 |
| `~filters.COMMAND` | 排除命令（取反） |
| `filters.TEXT & ~filters.COMMAND` | 纯文本且不是命令 |

---

## 五、内联键盘：让交互更丰富

内联键盘（Inline Keyboard）是 Telegram Bot 最强大的交互方式之一。它可以在消息下方显示按钮，用户点击后触发回调。

### 5.1 基础按钮

```python
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [
            InlineKeyboardButton("🔍 查询天气", callback_data="weather"),
            InlineKeyboardButton("📊 计算器", callback_data="calc"),
        ],
        [
            InlineKeyboardButton("📌 保存笔记", callback_data="note"),
            InlineKeyboardButton("📋 我的笔记", callback_data="notes"),
        ],
        [InlineKeyboardButton("🌐 访问官网", url="https://telegram.org")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("请选择功能：", reply_markup=reply_markup)

# 处理按钮回调
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()  # 必须调用，否则按钮会一直转圈

    data = query.data
    if data == "weather":
        await query.edit_message_text("请发送 `/weather 城市名` 查询天气", parse_mode="Markdown")
    elif data == "calc":
        await query.edit_message_text("请发送 `/calc 表达式` 进行计算", parse_mode="Markdown")
    elif data == "note":
        await query.edit_message_text("请发送 `/setnote 内容` 保存笔记", parse_mode="Markdown")
    elif data == "notes":
        await query.edit_message_text("请发送 `/mynotes` 查看笔记")

app.add_handler(CommandHandler("menu", menu))
app.add_handler(CallbackQueryHandler(button_callback))
```

### 5.2 分页按钮

分页是内联键盘的常见场景，比如浏览笔记列表：

```python
NOTES = ["笔记1", "笔记2", "笔记3", "笔记4", "笔记5", "笔记6", "笔记7", "笔记8"]
PAGE_SIZE = 3

async def notes_paginated(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    page = int(context.args[0]) if context.args else 0
    await show_notes_page(update, context, page)

async def show_notes_page(update: Update, context: ContextTypes.DEFAULT_TYPE, page: int) -> None:
    total = len(NOTES)
    total_pages = (total + PAGE_SIZE - 1) // PAGE_SIZE
    start = page * PAGE_SIZE
    end = min(start + PAGE_SIZE, total)
    page_notes = NOTES[start:end]

    text = f"📋 我的笔记（第 {page + 1}/{total_pages} 页）\n\n"
    for i, note in enumerate(page_notes, start=start + 1):
        text += f"{i}. {note}\n"

    # 构建分页按钮
    buttons = []
    if page > 0:
        buttons.append(InlineKeyboardButton("⬅️ 上一页", callback_data=f"page_{page - 1}"))
    if page < total_pages - 1:
        buttons.append(InlineKeyboardButton("➡️ 下一页", callback_data=f"page_{page + 1}"))

    reply_markup = InlineKeyboardMarkup([buttons]) if buttons else None

    # 如果是回调（点击按钮），编辑消息；否则发送新消息
    if update.callback_query:
        await update.callback_query.edit_message_text(text, reply_markup=reply_markup)
    else:
        await update.message.reply_text(text, reply_markup=reply_markup)

# 在 button_callback 中添加分页处理
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data.startswith("page_"):
        page = int(query.data.split("_")[1])
        await show_notes_page(update, context, page)
```

### 5.3 URL 按钮与分享按钮

```python
keyboard = [
    # URL 按钮 —— 点击后打开链接
    [InlineKeyboardButton("🔗 打开 GitHub", url="https://github.com")],
    # 分享按钮 —— 点击后转发到其他聊天
    [InlineKeyboardButton("📤 分享机器人", switch_inline_query="/start")],
    # 当前聊天内触发 inline 模式
    [InlineKeyboardButton("🔎 在此搜索", switch_inline_query_current_chat="")],
]
```

---

## 六、会话状态管理：多步对话

很多场景需要多步对话，比如"添加笔记"需要先问标题再问内容。`ConversationHandler` 就是为此而生。

### 6.1 笔记功能：多步对话

```python
from telegram.ext import ConversationHandler, MessageHandler, filters

# 定义会话状态
TITLE, CONTENT = range(2)

# 第一步：提示输入标题
async def note_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("📝 请输入笔记标题：")
    return TITLE

# 第二步：接收标题，提示输入内容
async def note_title(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["title"] = update.message.text
    await update.message.reply_text(f"好的，标题是「{update.message.text}」。\n现在请输入笔记内容：")
    return CONTENT

# 第三步：接收内容，保存笔记
async def note_content(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    title = context.user_data.get("title", "无标题")
    content = update.message.text

    # 初始化用户的笔记列表
    if "notes" not in context.user_data:
        context.user_data["notes"] = []
    context.user_data["notes"].append({"title": title, "content": content})

    await update.message.reply_text(
        f"✅ 笔记已保存！\n\n📝 标题：{title}\n📄 内容：{content}\n\n"
        f"使用 /mynotes 查看所有笔记。"
    )
    # 清除临时数据
    context.user_data.pop("title", None)
    return ConversationHandler.END

# 取消对话
async def note_cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("❌ 已取消。")
    context.user_data.clear()
    return ConversationHandler.END

# 查看所有笔记
async def my_notes(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    notes = context.user_data.get("notes", [])
    if not notes:
        await update.message.reply_text("📋 你还没有保存任何笔记。使用 /setnote 开始创建。")
        return

    text = "📋 **我的笔记列表**\n\n"
    for i, note in enumerate(notes, 1):
        text += f"**{i}. {note['title']}**\n   {note['content'][:50]}...\n\n"
    await update.message.reply_markdown(text)

# 注册会话处理器
conv_handler = ConversationHandler(
    entry_points=[CommandHandler("setnote", note_start)],
    states={
        TITLE: [MessageHandler(filters.TEXT & ~filters.COMMAND, note_title)],
        CONTENT: [MessageHandler(filters.TEXT & ~filters.COMMAND, note_content)],
    },
    fallbacks=[CommandHandler("cancel", note_cancel)],
)
app.add_handler(conv_handler)
app.add_handler(CommandHandler("mynotes", my_notes))
```

### 6.2 会话状态流转图

```
/setnote ──► [TITLE] ──输入标题──► [CONTENT] ──输入内容──► 保存并结束
    │            │                      │
    └──/cancel──┴──────/cancel─────────┘ ──► 取消并结束
```

::: tip 提示
`context.user_data` 是按用户隔离的字典，每个用户有独立的数据空间，不会互相干扰。但注意：**这些数据存在内存中，机器人重启后会丢失**。下一节会教你用数据库持久化。
:::

---

## 七、数据持久化：用 SQLite 存储数据

内存中的数据会在机器人重启后丢失。使用 SQLite 数据库可以永久保存数据。

### 7.1 数据库初始化

```python
import sqlite3
import json

DB_PATH = "bot_data.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def save_note(user_id: int, title: str, content: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO notes (user_id, title, content) VALUES (?, ?, ?)",
        (user_id, title, content)
    )
    conn.commit()
    conn.close()

def get_user_notes(user_id: int) -> list:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, title, content, created_at FROM notes WHERE user_id = ? ORDER BY created_at DESC",
        (user_id,)
    )
    notes = cursor.fetchall()
    conn.close()
    return notes

def delete_note(note_id: int, user_id: int):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE id = ? AND user_id = ?", (note_id, user_id))
    conn.commit()
    conn.close()
```

### 7.2 改造笔记功能

```python
# 在程序启动时初始化数据库
init_db()

# 修改 note_content 函数，将笔记保存到数据库
async def note_content(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    title = context.user_data.get("title", "无标题")
    content = update.message.text
    user_id = update.effective_user.id

    save_note(user_id, title, content)

    await update.message.reply_text(
        f"✅ 笔记已保存到数据库！\n\n📝 标题：{title}\n📄 内容：{content}"
    )
    context.user_data.pop("title", None)
    return ConversationHandler.END

# 修改 my_notes 函数，从数据库读取
async def my_notes(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    notes = get_user_notes(user_id)

    if not notes:
        await update.message.reply_text("📋 你还没有保存任何笔记。使用 /setnote 开始创建。")
        return

    text = "📋 **我的笔记列表**\n\n"
    for note_id, title, content, created_at in notes:
        text += f"**#{note_id} {title}**\n   {content[:50]}...\n   📅 {created_at}\n\n"
    text += "\n使用 /delnote <编号> 删除笔记"
    await update.message.reply_markdown(text)

# 删除笔记命令
async def del_note(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await update.message.reply_text("用法：`/delnote 笔记编号`\n例：`/delnote 3`", parse_mode="Markdown")
        return

    try:
        note_id = int(context.args[0])
    except ValueError:
        await update.message.reply_text("❌ 编号必须是数字")
        return

    user_id = update.effective_user.id
    delete_note(note_id, user_id)
    await update.message.reply_text(f"✅ 笔记 #{note_id} 已删除")

app.add_handler(CommandHandler("delnote", del_note))
```

---

## 八、完整代码：整合所有功能

下面是整合了所有功能的完整代码，可以直接复制使用。

::: details 📄 完整代码（bot.py）

```python
"""
Telegram Bot 完整示例
功能：命令处理、消息回复、内联键盘、多步对话、SQLite 持久化
依赖：pip install python-telegram-bot
"""

import logging
import sqlite3
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ConversationHandler,
    ContextTypes,
    filters,
)

# ========== 配置 ==========
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"  # 替换为你的 Token
DB_PATH = "bot_data.db"

# 配置日志
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ========== 数据库 ==========
def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def save_note(user_id, title, content):
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "INSERT INTO notes (user_id, title, content) VALUES (?, ?, ?)",
        (user_id, title, content)
    )
    conn.commit()
    conn.close()

def get_user_notes(user_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.execute(
        "SELECT id, title, content, created_at FROM notes WHERE user_id = ? ORDER BY created_at DESC",
        (user_id,)
    )
    notes = cursor.fetchall()
    conn.close()
    return notes

def delete_note_db(note_id, user_id):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("DELETE FROM notes WHERE id = ? AND user_id = ?", (note_id, user_id))
    conn.commit()
    conn.close()

# ========== 会话状态 ==========
TITLE, CONTENT = range(2)

# ========== 命令处理器 ==========
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        f"👋 你好 {update.effective_user.first_name}！\n\n"
        "我是你的专属机器人，输入 /help 查看我能做什么。"
    )
    await update.message.reply_text(text)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📖 **使用帮助**\n\n"
        "/start - 开始使用\n"
        "/menu - 打开功能菜单\n"
        "/setnote - 保存笔记（多步对话）\n"
        "/mynotes - 查看我的笔记\n"
        "/delnote <编号> - 删除笔记\n"
        "/calc <表达式> - 简易计算器\n\n"
        "也可以直接发文字和我聊天！"
    )
    await update.message.reply_markdown(text)

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📌 保存笔记", callback_data="setnote"),
         InlineKeyboardButton("📋 我的笔记", callback_data="mynotes")],
        [InlineKeyboardButton("📊 计算器", callback_data="calc"),
         InlineKeyboardButton("❓ 帮助", callback_data="help")],
    ]
    await update.message.reply_text("请选择功能：", reply_markup=InlineKeyboardMarkup(keyboard))

async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("用法：/calc 表达式\n例：/calc 1+2*3")
        return
    expr = " ".join(context.args)
    try:
        result = eval(expr, {"__builtins__": {}}, {})
        await update.message.reply_text(f"📊 {expr} = {result}")
    except Exception as e:
        await update.message.reply_text(f"❌ 计算出错：{e}")

# ========== 笔记会话 ==========
async def note_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📝 请输入笔记标题：")
    return TITLE

async def note_title(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["title"] = update.message.text
    await update.message.reply_text(f"标题：{update.message.text}\n现在请输入笔记内容：")
    return CONTENT

async def note_content(update: Update, context: ContextTypes.DEFAULT_TYPE):
    title = context.user_data.get("title", "无标题")
    content = update.message.text
    save_note(update.effective_user.id, title, content)
    await update.message.reply_text(f"✅ 笔记已保存！\n📝 {title}\n📄 {content}")
    context.user_data.clear()
    return ConversationHandler.END

async def note_cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❌ 已取消")
    context.user_data.clear()
    return ConversationHandler.END

async def my_notes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    notes = get_user_notes(update.effective_user.id)
    if not notes:
        await update.message.reply_text("📋 还没有笔记，使用 /setnote 创建")
        return
    text = "📋 **我的笔记**\n\n"
    for nid, title, content, created in notes:
        text += f"**#{nid} {title}**\n   {content[:60]}...\n   📅 {created}\n\n"
    await update.message.reply_markdown(text)

async def del_note(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("用法：/delnote 编号")
        return
    try:
        nid = int(context.args[0])
        delete_note_db(nid, update.effective_user.id)
        await update.message.reply_text(f"✅ 笔记 #{nid} 已删除")
    except ValueError:
        await update.message.reply_text("❌ 编号必须是数字")

# ========== 消息处理器 ==========
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if "你好" in text:
        await update.message.reply_text("你好呀！😊")
    elif "再见" in text:
        await update.message.reply_text("再见！👋")
    else:
        await update.message.reply_text(f"你说了：{text}")

# ========== 回调处理器 ==========
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data
    if data == "setnote":
        await query.message.reply_text("请发送 /setnote 开始创建笔记")
    elif data == "mynotes":
        await query.message.reply_text("请发送 /mynotes 查看笔记")
    elif data == "calc":
        await query.message.reply_text("请发送 /calc 表达式 进行计算")
    elif data == "help":
        await query.message.reply_text("输入 /help 查看完整帮助")

# ========== 错误处理 ==========
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f"异常：{context.error}", exc_info=context.error)
    if isinstance(update, Update) and update.effective_chat:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="⚠️ 处理消息时出现错误，请稍后重试。"
        )

# ========== 启动 ==========
def main():
    init_db()
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # 命令处理器
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(CommandHandler("calc", calc))
    app.add_handler(CommandHandler("mynotes", my_notes))
    app.add_handler(CommandHandler("delnote", del_note))

    # 会话处理器
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("setnote", note_start)],
        states={
            TITLE: [MessageHandler(filters.TEXT & ~filters.COMMAND, note_title)],
            CONTENT: [MessageHandler(filters.TEXT & ~filters.COMMAND, note_content)],
        },
        fallbacks=[CommandHandler("cancel", note_cancel)],
    )
    app.add_handler(conv_handler)

    # 消息处理器
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # 回调处理器
    app.add_handler(CallbackQueryHandler(button_callback))

    # 错误处理
    app.add_error_handler(error_handler)

    print("🤖 机器人已启动，按 Ctrl+C 停止")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
```

:::

---

## 九、Webhook 部署：让机器人上线

`run_polling()` 适合开发调试，但生产环境推荐使用 **Webhook** 模式，响应更快、资源消耗更低。

### 9.1 Polling vs Webhook 对比

| 维度 | Long Polling | Webhook |
|:---|:---|:---|
| **原理** | 机器人主动轮询服务器 | Telegram 服务器推送消息给机器人 |
| **延迟** | 略高 | 极低 |
| **资源** | 持续消耗 | 按需消耗 |
| **部署** | 简单，本地即可 | 需要 HTTPS 域名和服务器 |
| **适用场景** | 开发调试 | 生产环境 |

### 9.2 Webhook 代码

```python
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")
WEBHOOK_URL = "https://yourdomain.com"  # 你的 HTTPS 域名
PORT = 8443

async def post_init(application):
    """启动后设置 Webhook"""
    await application.bot.set_webhook(
        url=f"{WEBHOOK_URL}/{BOT_TOKEN}",
        max_connections=100,
        drop_pending_updates=True,
    )
    print(f"✅ Webhook 已设置：{WEBHOOK_URL}/{BOT_TOKEN}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).post_init(post_init).build()

    # 注册处理器（同前面的代码）
    # app.add_handler(...)

    # 启动 Webhook 服务器
    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=BOT_TOKEN,
        webhook_url=f"{WEBHOOK_URL}/{BOT_TOKEN}",
    )
```

### 9.3 使用 Nginx 反向代理（推荐）

```nginx
# /etc/nginx/sites-available/tgbot
server {
    listen 443 ssl;
    server_name yourdomain.com;

    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;

    location /YOUR_BOT_TOKEN/ {
        proxy_pass http://127.0.0.1:8443/;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

### 9.4 使用 Systemd 守护进程

```ini
# /etc/systemd/system/tgbot.service
[Unit]
Description=Telegram Bot Service
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/opt/tgbot
Environment=BOT_TOKEN=your_bot_token_here
ExecStart=/opt/tgbot/venv/bin/python bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

```bash
# 启动服务
sudo systemctl daemon-reload
sudo systemctl enable tgbot
sudo systemctl start tgbot

# 查看日志
sudo journalctl -u tgbot -f
```

### 9.5 免费部署方案：Vercel / Cloudflare Workers

如果不想自己维护服务器，可以使用 Serverless 平台部署：

**Cloudflare Workers 方案**（免费额度充足）：

```javascript
// 适合简单的轻量级 Bot
// 复杂 Bot 仍推荐 VPS 部署
export default {
  async fetch(request, env) {
    const update = await request.json();
    const chatId = update.message?.chat?.id;
    const text = update.message?.text;

    if (chatId && text) {
      await fetch(`https://api.telegram.org/bot${env.BOT_TOKEN}/sendMessage`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ chat_id: chatId, text: `Echo: ${text}` }),
      });
    }
    return new Response("OK");
  },
};
```

---

## 十、安全与最佳实践

### 10.1 Token 安全管理

```python
# ❌ 错误：硬编码在代码中
BOT_TOKEN = "123456:ABC-DEF"

# ✅ 正确：从环境变量读取
import os
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# ✅ 更好：使用 .env 文件（开发环境）
# pip install python-dotenv
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.environ.get("BOT_TOKEN")
```

`.env` 文件示例（加入 `.gitignore`）：
```
BOT_TOKEN=123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghi
```

### 10.2 用户鉴权

限制只有特定用户才能使用机器人：

```python
ALLOWED_USERS = {123456789, 987654321}  # 替换为你的 Telegram User ID

def restricted(func):
    """装饰器：限制只有授权用户才能使用"""
    async def wrapped(update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs):
        user_id = update.effective_user.id
        if user_id not in ALLOWED_USERS:
            await update.message.reply_text("⛔ 你没有权限使用此功能。")
            return
        return await func(update, context, *args, **kwargs)
    return wrapped

@restricted
async def admin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ 管理员命令执行成功")
```

### 10.3 速率限制

防止用户频繁发消息导致机器人过载：

```python
from collections import defaultdict
from datetime import datetime, timedelta

# 简易速率限制器
user_last_message = defaultdict(lambda: datetime.min)
RATE_LIMIT_SECONDS = 2  # 每个用户 2 秒只能发一条消息

def rate_limit(func):
    async def wrapped(update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs):
        user_id = update.effective_user.id
        now = datetime.now()
        if (now - user_last_message[user_id]).total_seconds() < RATE_LIMIT_SECONDS:
            await update.message.reply_text("⏳ 操作太频繁，请稍后再试")
            return
        user_last_message[user_id] = now
        return await func(update, context, *args, **kwargs)
    return wrapped
```

### 10.4 输入验证

```python
# 安全计算器：使用 ast 替代 eval
import ast
import operator

SAFE_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}

def safe_eval(expression: str) -> float:
    """安全解析数学表达式"""
    node = ast.parse(expression, mode="eval").body
    return _eval_node(node)

def _eval_node(node):
    if isinstance(node, ast.Constant):
        return node.value
    elif isinstance(node, ast.BinOp):
        left = _eval_node(node.left)
        right = _eval_node(node.right)
        op = SAFE_OPERATORS.get(type(node.op))
        if op is None:
            raise ValueError(f"不支持的运算符：{type(node.op)}")
        return op(left, right)
    elif isinstance(node, ast.UnaryOp):
        operand = _eval_node(node.operand)
        op = SAFE_OPERATORS.get(type(node.op))
        if op is None:
            raise ValueError(f"不支持的运算符：{type(node.op)}")
        return op(operand)
    else:
        raise ValueError(f"不支持的表达式：{type(node)}")
```

### 10.5 最佳实践清单

| 项目 | 说明 |
|:---|:---|
| ✅ Token 安全 | 使用环境变量，不硬编码 |
| ✅ 错误处理 | 全局 error_handler，避免崩溃 |
| ✅ 日志记录 | 记录关键操作和错误 |
| ✅ 速率限制 | 防止滥用和 DDoS |
| ✅ 输入验证 | 永不信任用户输入 |
| ✅ 用户鉴权 | 管理命令加权限检查 |
| ✅ 数据持久化 | 重要数据存数据库 |
| ✅ 优雅关闭 | 处理 SIGTERM 信号 |
| ✅ 监控告警 | 机器人挂了能及时知道 |
| ✅ 定期备份 | 数据库定期备份 |

---

## 十一、调试技巧

### 11.1 本地开发调试

```python
# 开启详细日志
import logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG  # DEBUG 级别会输出所有请求和响应
)
```

### 11.2 使用 Telegram 的测试环境

Telegram 提供了测试服务器，可以在不影响正式环境的情况下调试：

```
测试环境 API: https://api.telegram.org/bot<token>/getMe
（需要在 @BotFather 中将 bot 迁移到测试环境）
```

### 11.3 常见错误排查

| 错误 | 原因 | 解决方案 |
|:---|:---|:---|
| `Conflict: terminated by other getUpdates` | 多个实例同时在运行 | 确保只有一个实例运行 polling |
| `Unauthorized` | Token 错误或被吊销 | 检查 Token，必要时重新申请 |
| `Chat not found` | chat_id 错误 | 确认用户已先给机器人发过消息 |
| `Message is not modified` | 编辑消息但内容没变 | 编辑前检查内容是否相同 |
| `Query is too old` | 回调按钮超时 | 按钮回调有时间限制，需要尽快响应 |
| `Forbidden: bot was blocked by the user` | 用户拉黑了机器人 | 捕获异常，标记用户状态 |

### 11.4 BotFather 常用设置命令

| 命令 | 功能 |
|:---|:---|
| `/setname` | 设置机器人显示名 |
| `/setdescription` | 设置机器人简介（打开前看到的） |
| `/setabouttext` | 设置关于文本（profile 页面） |
| `/setuserpic` | 设置机器人头像 |
| `/setcommands` | 设置命令菜单 |
| `/setinline` | 开启 Inline 模式 |
| `/menubutton` | 设置 Mini App 菜单按钮 |
| `/setdomain` | 设置 Mini App 域名 |

---

## 十二、进阶方向

掌握了基础开发后，可以探索以下方向：

### 12.1 Inline Mode

允许用户在任意聊天中通过 `@你的机器人名` 触发搜索：

```python
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler

async def inline_search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query
    if not query:
        return

    results = [
        InlineQueryResultArticle(
            id="1",
            title=f"搜索：{query}",
            description="点击发送",
            input_message_content=InputTextMessageContent(
                f"🔍 搜索结果：{query}"
            ),
        )
    ]
    await update.inline_query.answer(results)

app.add_handler(InlineQueryHandler(inline_search))
```

### 12.2 接入 AI 模型

参考 [AI 机器人完全指南](../ai/ai-bots.md)，将 OpenAI / DeepSeek 等 AI 模型接入机器人。

### 12.3 开发 Mini App

参考 [Mini App 开发入门](../game/miniapp-dev.md)，用 Bot 菜单按钮打开你的 Web 应用。

### 12.4 群管功能开发

开发自动踢人、关键词过滤、欢迎消息等群管功能。参考 [群管机器人对比](./bot-comparison.md) 了解现有方案。

---

## 十三、学习资源

### 官方资源

- [Telegram Bot API 官方文档](https://core.telegram.org/bots/api) —— 最权威的 API 参考
- [python-telegram-bot 官方文档](https://docs.python-telegram-bot.org/) —— 库的完整 API
- [python-telegram-bot 示例库](https://github.com/python-telegram-bot/python-telegram-bot/tree/master/examples) —— 官方代码示例

### 推荐学习路径

```
入门 ──► 本文（基础 Bot 开发）
  │
  ├── 进阶 ──► Inline Mode（内联搜索）
  │
  ├── 进阶 ──► 接入 AI 模型（智能 Bot）
  │
  ├── 进阶 ──► Mini App 开发（Web 应用）
  │
  └── 高阶 ──► MTProto/TDLib（用户客户端）
```

---

## 总结

本文从零开始，带你完成了一个功能完整的 Telegram Bot 开发：

1. **环境搭建** —— Python + python-telegram-bot
2. **命令处理** —— /start、/help、带参数命令
3. **消息处理** —— 关键词回复、图片处理
4. **内联键盘** —— 按钮交互、分页
5. **多步对话** —— ConversationHandler
6. **数据持久化** —— SQLite 数据库
7. **Webhook 部署** —— 生产环境上线
8. **安全实践** —— Token 管理、鉴权、限流

**下一步建议：**
- 把完整代码跑起来，修改成自己的功能
- 逐步添加新功能（天气 API、翻译、提醒等）
- 部署到服务器，让朋友也能使用
- 探索 [Mini App 开发](../game/miniapp-dev.md) 和 [AI 机器人](../ai/ai-bots.md) 等进阶方向

Telegram Bot 的可能性几乎是无限的，从简单的工具机器人到复杂的商业系统，都可以在 Telegram 上实现。开始动手吧！🚀

---

**相关阅读：**

- [机器人申请教程](../../createrobot.md) — 通过 BotFather 创建 Bot
- [API 入门指南](../../api-intro.md) — Bot API 与 MTProto API 对比
- [AI 机器人完全指南](../ai/ai-bots.md) — 接入 AI 大模型
- [Mini App 开发入门](../game/miniapp-dev.md) — 开发 Telegram 小程序
- [群管机器人对比](./bot-comparison.md) — 现有群管方案对比