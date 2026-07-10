---
title: Telegram API 开发者入门指南：Bot API 与 MTProto API 对比与实战
shortTitle: API入门
description: 想开发 Telegram 机器人或客户端？本文详解 Bot API 与 MTProto API 的区别、开发环境搭建、第一个机器人代码实战，以及开发者学习资源推荐。
icon: code
category:
  - 进阶教程
tag:
  - API
  - 开发者
  - 机器人
  - Bot API
  - MTProto
head:
  - - meta
    - name: keywords
      content: Telegram API,Telegram Bot API,Telegram MTProto API,Telegram开发,Telegram机器人开发,TG API,TG开发,电报API,电报开发,Telegram TDLib,Telegram开发者入门
---

# Telegram API 开发者入门指南：Bot API 与 MTProto API 对比与实战

Telegram 提供了两套 API，分别面向不同的开发场景。无论你是想写一个群管机器人，还是开发一个完整的第三方客户端，本文都能帮你快速找到正确的入口。

---

## 一、两套 API 概览

### 1.1 Bot API vs MTProto API

| 维度 | Bot API | MTProto API (TDLib) |
|------|---------|-------------------|
| **面向对象** | 机器人开发者 | 客户端/高级应用开发者 |
| **协议** | HTTPS | MTProto（自定义加密协议） |
| **开发难度** | ⭐ 低 | ⭐⭐⭐⭐ 高 |
| **语言支持** | 任何能发 HTTP 请求的语言 | C/C++/Rust 为主，其他语言通过绑定 |
| **功能范围** | 机器人相关功能 | 几乎全部 Telegram 功能 |
| **身份** | 以机器人身份运行 | 以用户身份或机器人身份运行 |
| **消息接收** | Webhook 或 Long Polling | 推送（实时） |
| **文件上传** | 有大小限制（50MB 发送 / 20MB 接收） | 无限制 |
| **维护成本** | 低 | 高 |

### 1.2 我该选哪个？

```
你的需求是什么？
    │
    ├── 写一个机器人（群管、通知、查询等）
    │   └── ✅ 选 Bot API
    │
    ├── 写一个第三方客户端 / 用户工具
    │   └── ✅ 选 MTProto API (TDLib)
    │
    └── 需要以用户身份批量操作
        └── ✅ 选 MTProto API (User API)
```

::: tip 💡 大多数开发者的选择
90% 的开发者只需要 **Bot API**。它简单、文档完善、社区资源丰富。除非你有明确的客户端开发需求，否则从 Bot API 开始。
:::

---

## 二、Bot API 详解

### 2.1 核心概念

Bot API 是一套基于 HTTPS 的 RESTful 接口，你通过向 `https://api.telegram.org/bot<TOKEN>/<METHOD>` 发送请求来控制机器人。

**工作流程：**
```
用户在 Telegram 中发送消息
        ↓
Telegram 服务器收到消息
        ↓
通过 Webhook 或 getUpdates 推送给你的服务
        ↓
你的程序处理消息并调用 Bot API 回复
        ↓
Telegram 服务器将回复发送给用户
```

### 2.2 获取 API Token

1. 在 Telegram 中搜索 [@BotFather](https://t.me/BotFather)
2. 发送 `/newbot` 创建机器人
3. 按提示输入名称和用户名
4. 获得 API Token，格式为 `123456789:ABCdefGHIjklMNOpqrSTUvwxYZ`

::: danger 🚨 安全警告
API Token 等于机器人的控制权！
- **绝对不要**将 Token 提交到公开的 Git 仓库
- **绝对不要**在聊天中分享 Token
- 如果 Token 泄露，立即在 BotFather 中 `/revoke` 重新生成
:::

详细的 Token 获取和机器人管理流程，请参阅 [机器人创建教程](./createrobot.html)。

### 2.3 两种接收消息的方式

#### 方式一：Long Polling（轮询）

你的程序主动向 Telegram 服务器询问"有没有新消息"：

```
你的程序 → getUpdates → Telegram 服务器
                                ↓
                        返回新消息（或超时空列表）
```

**优点：** 简单，无需公网 IP，本地开发友好
**缺点：** 实时性略差（通常 1-2 秒延迟），不适合高并发

#### 方式二：Webhook（推送）

你提供一个 HTTPS URL，Telegram 服务器有新消息时主动推送给你：

```
Telegram 服务器 → POST /your-webhook-url → 你的服务器
```

**优点：** 实时性好，性能高
**缺点：** 需要公网 HTTPS 服务器，配置稍复杂

::: tip 💡 开发阶段建议
开发阶段用 Long Polling（简单快速），生产环境切换到 Webhook（性能更好）。
:::

---

## 三、第一个 Bot：Hello World

### 3.1 Python 实战（推荐新手）

#### 环境准备

```bash
# 需要 Python 3.8+
python3 -m venv venv
source venv/bin/activate
pip install python-telegram-bot
```

#### 最简代码

```python
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# 替换为你的 Bot Token
TOKEN = "YOUR_BOT_TOKEN_HERE"

async def start(update: Update, context):
    await update.message.reply_text("你好！我是你的第一个机器人 🤖")

async def echo(update: Update, context):
    text = update.message.text
    await update.message.reply_text(f"你说了：{text}")

def main():
    app = Application.builder().token(TOKEN).build()
    
    # 注册命令处理器
    app.add_handler(CommandHandler("start", start))
    
    # 注册消息处理器（回复所有文本消息）
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    # 启动机器人
    print("机器人已启动，按 Ctrl+C 停止")
    app.run_polling()

if __name__ == "__main__":
    main()
```

#### 运行

```bash
python bot.py
```

在 Telegram 中找到你的机器人，点击 **Start**，发送任意消息，机器人会回复你说的内容。

### 3.2 Node.js 实战

#### 环境准备

```bash
mkdir my-bot && cd my-bot
npm init -y
npm install node-telegram-bot-api
```

#### 最简代码

```javascript
const TelegramBot = require('node-telegram-bot-api');

// 替换为你的 Bot Token
const token = 'YOUR_BOT_TOKEN_HERE';

const bot = new TelegramBot(token, { polling: true });

// /start 命令
bot.onText(/\/start/, (msg) => {
    bot.sendMessage(msg.chat.id, '你好！我是你的第一个机器人 🤖');
});

// 回复所有文本消息
bot.on('message', (msg) => {
    if (!msg.text || msg.text.startsWith('/')) return;
    bot.sendMessage(msg.chat.id, `你说了：${msg.text}`);
});

console.log('机器人已启动，按 Ctrl+C 停止');
```

#### 运行

```bash
node bot.js
```

### 3.3 直接调用 Bot API（无框架）

不使用任何框架，直接发送 HTTP 请求：

```bash
# 发送消息
curl -s "https://api.telegram.org/bot<TOKEN>/sendMessage" \
  -d "chat_id=123456789" \
  -d "text=Hello from curl!"
```

```python
# Python requests
import requests

TOKEN = "YOUR_BOT_TOKEN"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
requests.post(url, json={
    "chat_id": 123456789,
    "text": "Hello from Python!"
})
```

::: details 📋 常用 Bot API 方法

| 方法 | 功能 |
|------|------|
| `getMe` | 获取机器人信息 |
| `sendMessage` | 发送文本消息 |
| `sendPhoto` | 发送图片 |
| `sendDocument` | 发送文件 |
| `sendLocation` | 发送位置 |
| `sendPoll` | 发送投票 |
| `answerCallbackQuery` | 响应内联键盘按钮点击 |
| `setWebhook` | 设置 Webhook |
| `getUpdates` | 获取新消息（Long Polling） |
| `editMessageText` | 编辑已发送的消息 |
| `deleteMessage` | 删除消息 |
| `forwardMessage` | 转发消息 |

完整方法列表参见 [Bot API 官方文档](https://core.telegram.org/bots/api)。
:::

---

## 四、Bot API 进阶功能

### 4.1 内联键盘（Inline Keyboard）

在消息下方添加可点击的按钮：

```python
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def button_demo(update, context):
    keyboard = [
        [InlineKeyboardButton("选项 A", callback_data='a'),
         InlineKeyboardButton("选项 B", callback_data='b')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("请选择：", reply_markup=reply_markup)
```

### 4.2 自定义命令菜单

通过 BotFather 或 API 设置命令列表，用户在输入框点击 `/` 时会看到：

```bash
# 通过 BotFather
/setcommands
# 然后发送：
start - 开始使用
help - 获取帮助
settings - 设置
```

### 4.3 Mini App（小程序）

Bot API 支持在聊天中嵌入 Web 应用：

1. 通过 BotFather → `/newapp` 创建 Mini App
2. 提供 HTTPS 页面 URL
3. 用户点击按钮即可在 Telegram 内打开网页应用

详见 [Mini App 开发文档](https://core.telegram.org/bots/webapps)。

### 4.4 支付功能

Bot API 集成了支付系统，支持 Telegram Stars 和第三方支付：

```python
await context.bot.send_invoice(
    chat_id=chat_id,
    title="VIP会员",
    description="解锁全部功能",
    payload="vip_subscription",
    provider_token="YOUR_PROVIDER_TOKEN",  # 使用 Stars 时留空
    currency="XTR",  # Telegram Stars
    prices=[{"label": "VIP", "amount": 100}]  # 100 Stars
)
```

---

## 五、MTProto API 详解

### 5.1 什么是 MTProto？

MTProto 是 Telegram 自研的加密通信协议，用于客户端与服务器之间的所有通信。它比 Bot API 更底层、更强大，但也更复杂。

### 5.2 TDLib（Telegram Database Library）

TDLib 是 Telegram 官方维护的跨平台库，封装了 MTProto 协议：

- **语言**：C++ 编写，提供多种语言绑定
- **功能**：完整的 Telegram 客户端功能
- **身份**：可以以**用户身份**或**机器人身份**运行
- **存储**：本地数据库缓存，离线可用

### 5.3 API ID 和 API Hash

使用 MTProto API 需要获取 `api_id` 和 `api_hash`：

1. 访问 [my.telegram.org](https://my.telegram.org)
2. 登录你的 Telegram 账号
3. 点击 **API development tools**
4. 填写应用名称和平台
5. 获得 `api_id`（数字）和 `api_hash`（字符串）

::: warning ⚠️ 安全提醒
- `api_id` 和 `api_hash` 用于标识你的应用，不是秘密凭证
- 但仍建议不要公开提交到代码仓库
- 真正需要保密的是用户的**手机号**和**验证码**
:::

### 5.4 TDLib 语言绑定

| 语言 | 推荐库 | 说明 |
|------|--------|------|
| **Python** | `python-telegram` | TDLib 的 Python 绑定 |
| **JavaScript/TypeScript** | `telegram-mtproto` | MTProto 协议实现 |
| **Go** | `gotd/td` | 纯 Go 实现 |
| **Rust** | `grammers` | 纯 Rust 实现 |
| **Java/Kotlin** | TDLib 官方 JNI | 官方 Java 绑定 |
| **C#** | `WTelegramClient` | .NET 实现 |

### 5.5 TDLib 基本使用（Python 示例）

```python
from telegram import Telegram

# 初始化
tg = Telegram(
    api_id=12345,          # 你的 api_id
    api_hash="abc123...",  # 你的 api_hash
    phone="+8613800138000" # 你的手机号
)

await tg.connect()

# 首次登录需要验证码
result = await tg.login()
if isinstance(result, LoginCodeRequired):
    code = input("输入验证码: ")
    await tg.login(code=code)

# 发送消息
await tg.send_message(chat_id=123456789, text="Hello from TDLib!")

# 接收消息
async def handle_message(update):
    if hasattr(update, 'message'):
        print(f"收到: {update.message.text}")

tg.add_handler(handle_message)
await tg.idle()  # 保持运行
```

::: warning ⚠️ User API 限制
以用户身份使用 MTProto API 时，请注意：
- 不要发送垃圾消息，否则账号会被封禁
- 遵守 [Telegram API 使用条款](https://core.telegram.org/api/terms)
- 建议使用小号进行开发和测试
:::

---

## 六、开发环境搭建

### 6.1 开发语言选择

| 语言 | Bot API 推荐 | MTProto 推荐 | 适合人群 |
|------|-------------|-------------|---------|
| **Python** | `python-telegram-bot` | `python-telegram` | 新手、快速原型 |
| **Node.js** | `node-telegram-bot-api` / `telegraf` | `telegram-mtproto` | Web 开发者 |
| **Go** | `telebot` | `gotd/td` | 追求性能 |
| **Rust** | `tbot` | `grammers` | 追求极致性能和安全 |
| **PHP** | `nutgram` | — | 传统 Web 主机 |

### 6.2 Webhook 部署方案

生产环境推荐使用 Webhook，常见部署方案：

**方案一：VPS + Nginx + 反向代理**
```
Telegram → Nginx (443) → 你的应用 (8080)
```

**方案二：Serverless（无服务器）**
```
Telegram → Cloudflare Workers / Vercel / AWS Lambda
```

**方案三：云函数**
```
Telegram → 腾讯云函数 / 阿里云函数计算
```

::: tip 💡 Webhook 要求
- 必须 HTTPS（TLS 加密）
- 端口仅支持：443、80、88、8443
- 响应时间需在 60 秒内
- 如长时间无响应，Telegram 会重试
:::

### 6.3 本地开发 Webhook 测试

开发阶段无需公网服务器，使用隧道工具即可：

```bash
# 方案1：ngrok
ngrok http 8080
# 获得 https://xxx.ngrok.io → localhost:8080

# 方案2：cloudflared（免费）
cloudflared tunnel --url http://localhost:8080

# 然后设置 Webhook
curl "https://api.telegram.org/bot<TOKEN>/setWebhook?url=https://xxx.ngrok.io/webhook"
```

---

## 七、实用开发技巧

### 7.1 消息格式

Bot API 支持 Markdown 和 HTML 两种格式：

```python
# Markdown 格式
await bot.send_message(
    chat_id,
    "*粗体* _斜体_ `代码` [链接](https://example.com)",
    parse_mode="MarkdownV2"
)

# HTML 格式
await bot.send_message(
    chat_id,
    "<b>粗体</b> <i>斜体</i> <code>代码</code> <a href='https://example.com'>链接</a>",
    parse_mode="HTML"
)
```

::: tip 💡 HTML 比 Markdown 更推荐
MarkdownV2 需要转义大量特殊字符（`. - ( ) !` 等），容易出错。HTML 格式更直观，转义规则更简单。
:::

### 7.2 速率限制

Bot API 有速率限制，需注意：

| 操作类型 | 限制 |
|---------|------|
| 单个聊天 | 每秒 1 条消息 |
| 群组 | 每秒 20 条消息 |
| 全局 | 每秒 30 条消息 |
| 相同内容群发 | 每分钟 30 条（不同聊天） |

超出限制会收到 `429 Too Many Requests` 错误，响应中包含 `retry_after` 字段告诉你等待多少秒。

### 7.3 错误处理

```python
from telegram.error import TelegramError, RetryAfter, Forbidden

async def safe_send(bot, chat_id, text):
    try:
        await bot.send_message(chat_id, text)
    except RetryAfter as e:
        print(f"速率限制，等待 {e.retry_after} 秒")
        await asyncio.sleep(e.retry_after)
        await bot.send_message(chat_id, text)  # 重试
    except Forbidden:
        print(f"用户 {chat_id} 已屏蔽机器人")
    except TelegramError as e:
        print(f"Telegram 错误: {e}")
```

### 7.4 数据持久化

Bot API 本身不存储状态，你需要自行管理：

- **SQLite**：轻量级，适合小型 Bot
- **PostgreSQL**：功能完整，适合中大型项目
- **Redis**：高速缓存，适合临时数据和速率限制
- **MongoDB**：灵活模式，适合非结构化数据

---

## 八、学习资源推荐

### 8.1 官方资源

| 资源 | 链接 | 说明 |
|------|------|------|
| Bot API 文档 | [core.telegram.org/bots/api](https://core.telegram.org/bots/api) | 最权威的 API 参考 |
| MTProto 文档 | [core.telegram.org/mtproto](https://core.telegram.org/mtproto) | 协议白皮书 |
| TDLib 文档 | [core.telegram.org/tdlib](https://core.telegram.org/tdlib) | TDLib 使用指南 |
| Telegram API 入门 | [core.telegram.org/api](https://core.telegram.org/api) | API 概览 |
| Bot 介绍 | [core.telegram.org/bots](https://core.telegram.org/bots) | Bot 功能介绍 |

### 8.2 开源项目参考

| 项目 | 语言 | 说明 |
|------|------|------|
| [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) | Python | 最流行的 Python Bot 框架 |
| [Telegraf](https://github.com/telegraf/telegraf) | Node.js | 最流行的 Node.js Bot 框架 |
| [grammY](https://github.com/grammyjs/grammY) | TypeScript | 新一代 TS Bot 框架 |
| [aiogram](https://github.com/aiogram/aiogram) | Python | 异步 Bot 框架 |
| [gotd](https://github.com/gotd/td) | Go | 纯 Go MTProto 实现 |
| [TDLight](https://github.com/tdlight-team) | Java/C++ | TDLib 增强版 |

### 8.3 学习路径建议

```
第1步：通过 BotFather 创建机器人，获得 Token
    ↓
第2步：用 curl 调用 getMe 和 sendMessage，理解 API 机制
    ↓
第3步：选择语言和框架，写一个 echo 机器人
    ↓
第4步：添加命令处理、内联键盘、消息格式
    ↓
第5步：接入数据库，实现状态管理
    ↓
第6步：部署到服务器，配置 Webhook
    ↓
第7步（可选）：学习 MTProto API / TDLib，开发高级功能
```

---

## 九、常见问题

### Q1：Bot API 免费吗？

完全免费。Telegram 不对 API 调用收费。但你需要自己承担服务器费用。

### Q2：一个 Token 可以在多个服务器上使用吗？

技术上可以，但不建议。多个实例同时 `getUpdates` 会互相抢消息。如果需要多实例，使用 Webhook 或消息队列。

### Q3：Bot 能主动给用户发消息吗？

可以，但用户必须先主动给 Bot 发过消息（或通过 `/start` 启动过）。Bot 不能主动给从未交互过的用户发消息。

### Q4：Bot 能读取群组里的所有消息吗？

默认不能。Bot 在群组中只能收到以下消息：
- 以 `/` 开头的命令
- @提到该 Bot 的消息
- 回复 Bot 消息的消息

如需接收所有消息，在 BotFather 中关闭 **Group Privacy**。

### Q5：MTProto API 会被封号吗？

以用户身份使用 MTProto API 时，如果发送大量消息或行为异常，可能会被封号。建议：
- 使用小号测试
- 遵守 Telegram 服务条款
- 控制消息频率
- 不要批量加好友/群组

### Q6：Bot 能发送文件吗？大小限制是多少？

Bot API 限制：发送 50MB，接收 20MB。如需更大文件，使用 MTProto API（无限制）。

---

## 十、总结

| 维度 | Bot API | MTProto API |
|------|---------|-------------|
| **适合** | 机器人开发 | 客户端/高级应用 |
| **难度** | 低 | 高 |
| **功能** | 机器人功能 | 全部功能 |
| **推荐人群** | 所有开发者 | 高级开发者 |
| **入门时间** | 1-2 小时 | 1-2 天 |

**核心建议：**

1. **从 Bot API 开始**：90% 的需求都能满足
2. **选好框架**：不要裸写 HTTP 请求，用成熟框架
3. **注意安全**：保护 Token，做好错误处理
4. **关注官方文档**：Bot API 频繁更新，新功能优先出现在文档中
5. **参考开源项目**：阅读优秀 Bot 的源码是最佳学习方式

::: tip 💡 下一步
创建好机器人后，可以参考 [私聊机器人搭建教程](./livegram.html) 实现一个实用的客服 Bot，或阅读 [礼物系统指南](./topics/gift/gifts.html) 了解 Bot 与支付功能的结合。
:::

---

## 相关文章

- [机器人创建教程](./createrobot.html)
- [私聊机器人搭建](./livegram.html)
- [Premium 会员](./premium.html)
- [礼物系统](./topics/gift/gifts.html)
- [频道助推](./boost.html)
