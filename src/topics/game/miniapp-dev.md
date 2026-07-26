---
title: Telegram Mini App 开发入门：快速构建你的第一个 Telegram 小程序
shortTitle: Mini App开发
description: 想开发 Telegram 小程序？本文从零开始，详解 Mini App 开发环境搭建、核心 API 调用、TON 钱包集成、支付功能实现，附带完整示例项目——简易积分商城。
icon: code
order: 4
category:
  - 开发者教程
tag:
  - Mini App
  - 小程序
  - 开发
  - 前端
  - TON
  - 教程

head:
  - - meta
    - name: keywords
      content: Telegram Mini App 开发,Telegram小程序开发,Telegram Web App,Mini App教程,TON钱包集成,Telegram支付开发,Telegram Bot开发,电报小程序开发
---

# Telegram Mini App 开发入门：快速构建你的第一个 Telegram 小程序

想在 Telegram 上做一个自己的小程序（Mini App）？本文将带你从零开始，一步步完成开发环境搭建、核心功能实现和发布上线。

无论你是想做一个小游戏、实用工具、还是电商应用，这篇指南都能帮你快速上手。

---

## 一、Mini App 开发入门概览

### 1.1 什么是 Mini App？

Telegram Mini App（曾称 Web App）是嵌入在 Telegram 内部的**网页应用**，本质上就是一个运行在 Telegram WebView 中的 H5 页面，但可以通过 Telegram 提供的 JS SDK 调用原生能力。

**核心特点：**
- 基于 Web 技术（HTML/CSS/JavaScript）
- 无需下载安装，点开即用
- 可以调用 Telegram 原生能力（用户信息、支付、分享等）
- 支持 TON 区块链集成
- 跨平台（iOS/Android/Desktop 都能用）

### 1.2 你需要什么基础？

**必备技能：**
- HTML、CSS、JavaScript 基础
- 前端框架（React/Vue/原生 JS 都可以）
- 基本的后端知识（可选，看项目复杂度）

**推荐技术栈：**

| 层 | 推荐方案 | 说明 |
|:---|:---|:---|
| **前端框架** | React / Vue / 原生 JS | 选你最熟悉的 |
| **UI 框架** | Tailwind CSS / Vant / Ant Design Mobile | 移动端优先 |
| **后端** | Node.js / Python / PHP | 任意后端语言 |
| **部署** | Vercel / Netlify / Cloudflare Pages | 静态托管即可 |
| **域名** | 任意 HTTPS 域名 | 必须支持 HTTPS |

### 1.3 Mini App 的典型应用场景

| 类型 | 例子 | 难度 |
|:---|:---|:---:|
| **工具类** | 计算器、转换器、待办清单 | ⭐ |
| **内容类** | 阅读器、图集、课程 | ⭐⭐ |
| **游戏类** | 休闲小游戏、益智游戏 | ⭐⭐⭐ |
| **电商类** | 商城、外卖、票务 | ⭐⭐⭐⭐ |
| **Web3 类** | 钱包应用、NFT 市场、DeFi | ⭐⭐⭐⭐⭐ |

---

## 二、准备工作

### 2.1 你需要的东西

开始之前，请确保你有：

1. ✅ 一个 Telegram 账号
2. ✅ 一个机器人（Bot）—— Mini App 需要通过 Bot 调用
3. ✅ 一个支持 HTTPS 的域名（可以用免费的）
4. ✅ 基础的前端开发环境（Node.js 等）

### 2.2 第一步：创建 Bot

Mini App 必须通过 Bot 来调用，所以你首先需要一个 Bot：

1. 打开 Telegram，搜索 [@BotFather](https://t.me/BotFather)
2. 发送 `/newbot`
3. 按提示设置 Bot 名称和用户名
4. 保存好 **Bot Token**（后面会用到）

### 2.3 第二步：准备域名和服务器

Mini App 需要通过 HTTPS 访问，所以你需要：

**域名：**
- 可以购买一个域名（推荐 Namecheap、Cloudflare）
- 或者使用免费域名（如 GitHub Pages、Vercel 提供的子域名）

**托管服务（免费方案）：**

| 服务 | 免费额度 | 特点 |
|:---|:---|:---|
| **Vercel** | 无限流量，免费 | 部署简单，支持前端框架 |
| **Netlify** | 100GB/月流量 | 拖拽部署，易用 |
| **Cloudflare Pages** | 无限流量 | 速度快，全球 CDN |
| **GitHub Pages** | 免费 | 适合静态站点 |

---

## 三、Hello World：第一个 Mini App

### 3.1 创建项目

让我们从最简单的 HTML 页面开始：

```bash
# 创建项目目录
mkdir my-first-miniapp
cd my-first-miniapp

# 创建入口文件
touch index.html
```

### 3.2 编写代码

创建一个最简单的 Mini App：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>我的第一个 Mini App</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: var(--tg-theme-bg-color, #ffffff);
            color: var(--tg-theme-text-color, #000000);
            padding: 20px;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 20px;
        }

        .greeting {
            font-size: 24px;
            font-weight: bold;
            text-align: center;
        }

        .user-info {
            background: var(--tg-theme-secondary-bg-color, #f0f0f0);
            padding: 20px;
            border-radius: 12px;
            width: 100%;
            max-width: 400px;
        }

        .user-info p {
            margin: 8px 0;
            font-size: 14px;
        }

        .btn {
            background: var(--tg-theme-button-color, #2481cc);
            color: var(--tg-theme-button-text-color, #ffffff);
            border: none;
            padding: 12px 24px;
            border-radius: 10px;
            font-size: 16px;
            cursor: pointer;
            width: 100%;
            max-width: 400px;
        }

        .btn:active {
            opacity: 0.8;
        }
    </style>
</head>
<body>
    <div class="greeting">👋 欢迎来到 Mini App</div>
    
    <div class="user-info">
        <p><strong>用户 ID：</strong><span id="userId">加载中...</span></p>
        <p><strong>用户名：</strong><span id="userName">加载中...</span></p>
        <p><strong>语言：</strong><span id="userLang">加载中...</span></p>
    </div>

    <button class="btn" id="showAlertBtn">显示原生弹窗</button>
    <button class="btn" id="closeBtn">关闭 Mini App</button>

    <!-- 引入 Telegram Web App SDK -->
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    
    <script>
        // 初始化 Telegram Web App
        const tg = window.Telegram.WebApp;
        
        // 告诉 Telegram 应用已准备好
        tg.ready();
        
        // 展开应用（可选，默认是半屏）
        tg.expand();
        
        // 获取用户信息
        const user = tg.initDataUnsafe.user;
        
        if (user) {
            document.getElementById('userId').textContent = user.id;
            document.getElementById('userName').textContent = user.first_name + (user.last_name ? ' ' + user.last_name : '');
            document.getElementById('userLang').textContent = user.language_code;
        }
        
        // 显示原生弹窗
        document.getElementById('showAlertBtn').addEventListener('click', () => {
            tg.showAlert('这是 Telegram 原生弹窗！', () => {
                console.log('用户点击了确认');
            });
        });
        
        // 关闭 Mini App
        document.getElementById('closeBtn').addEventListener('click', () => {
            tg.close();
        });
    </script>
</body>
</html>
```

### 3.3 部署到线上

将这个 `index.html` 部署到支持 HTTPS 的服务器上。

**使用 Vercel 快速部署示例：**

```bash
# 1. 安装 Vercel CLI
npm install -g vercel

# 2. 在项目目录运行
vercel

# 3. 按提示操作，部署成功后会得到一个 HTTPS 链接
```

记下你的部署 URL，例如：`https://my-first-miniapp.vercel.app`

### 3.4 配置 Bot Web App

告诉 BotFather 你的 Mini App 地址：

1. 打开 [@BotFather](https://t.me/BotFather)
2. 发送 `/newapp`
3. 选择你刚才创建的 Bot
4. 按提示输入：
   - 名称（显示在菜单里的名字）
   - 简短描述
   - 头像图片
   - Web App 的 URL（刚才部署的 HTTPS 链接）
5. 完成！你会得到一个类似 `t.me/your_bot/yourapp` 的链接

### 3.5 测试打开

在 Telegram 中，通过以下方式打开你的 Mini App：

1. **通过菜单按钮**：和你的 Bot 聊天，点击键盘菜单按钮
2. **通过链接**：访问 `t.me/your_bot/yourapp`
3. **通过内联按钮**：在消息中点击按钮打开

如果一切顺利，你会看到刚才写的页面，并且能正确显示用户信息！🎉

---

## 四、核心 API 详解

### 4.1 Telegram Web App SDK 引入

在 HTML 中引入官方 SDK：

```html
<script src="https://telegram.org/js/telegram-web-app.js"></script>
```

初始化：

```javascript
const tg = window.Telegram.WebApp;

// 必做：告诉 Telegram 应用已加载完成
tg.ready();
```

### 4.2 用户信息

```javascript
const user = tg.initDataUnsafe.user;

if (user) {
    console.log('用户ID:', user.id);
    console.log('名字:', user.first_name);
    console.log('姓氏:', user.last_name);
    console.log('用户名:', user.username);
    console.log('语言:', user.language_code);
    console.log('是否Premium:', user.is_premium);
    console.log('头像:', user.photo_url);
}
```

::: warning ⚠️ 安全提示
`initDataUnsafe` 中的数据**不可信**，不能用于后端安全验证。如果后端需要验证用户身份，必须使用 `initData` 进行签名验证。详见本章第 4.12 节。
:::

### 4.3 主题颜色（适配深色/浅色模式）

Telegram 会将当前主题色传递给 Mini App，你可以用 CSS 变量实现自动适配：

```css
:root {
    --bg-color: var(--tg-theme-bg-color, #ffffff);
    --text-color: var(--tg-theme-text-color, #000000);
    --hint-color: var(--tg-theme-hint-color, #999999);
    --link-color: var(--tg-theme-link-color, #2481cc);
    --button-color: var(--tg-theme-button-color, #2481cc);
    --button-text-color: var(--tg-theme-button-text-color, #ffffff);
    --secondary-bg: var(--tg-theme-secondary-bg-color, #f0f0f0);
}

body {
    background: var(--bg-color);
    color: var(--text-color);
}
```

监听主题变化：

```javascript
tg.onEvent('themeChanged', () => {
    console.log('主题改变了');
    // 可以在这里做额外的样式调整
});
```

### 4.4 原生弹窗

```javascript
// 确认弹窗
tg.showAlert('消息内容', () => {
    console.log('用户点击了确定');
});

// 确认/取消弹窗
tg.showConfirm('确定要删除吗？', (confirmed) => {
    if (confirmed) {
        console.log('用户确认');
    } else {
        console.log('用户取消');
    }
});

// 输入弹窗
tg.showPopup({
    title: '输入你的名字',
    message: '请输入姓名',
    buttons: [
        { id: 'ok', type: 'default', text: '确定' },
        { id: 'cancel', type: 'cancel', text: '取消' }
    ]
}, (buttonId) => {
    console.log('用户点击了:', buttonId);
});
```

### 4.5 主按钮（Main Button）

底部的主操作按钮：

```javascript
// 设置主按钮
tg.MainButton.setText('提交');
tg.MainButton.show();

// 点击事件
tg.MainButton.onClick(() => {
    console.log('用户点击了主按钮');
    
    // 显示加载状态
    tg.MainButton.showProgress();
    
    // 模拟请求
    setTimeout(() => {
        tg.MainButton.hideProgress();
        tg.showAlert('提交成功！');
    }, 2000);
});

// 隐藏主按钮
// tg.MainButton.hide();
```

### 4.6 返回按钮（Back Button）

```javascript
// 显示返回按钮（仅在 Android 上有效）
tg.BackButton.show();

// 点击事件
tg.BackButton.onClick(() => {
    // 返回上一页或关闭应用
    tg.close();
});

// 隐藏返回按钮
// tg.BackButton.hide();
```

### 4.7 分享功能

```javascript
// 分享消息到聊天
const shareUrl = 'https://t.me/share/url?url=https://example.com&text=看看这个好东西！';
window.open(shareUrl, '_blank');
```

### 4.8 发送数据到 Bot

当用户操作完成后，可以向 Bot 发送数据：

```javascript
// 发送数据给 Bot
tg.sendData(JSON.stringify({
    action: 'buy_item',
    item_id: 123,
    quantity: 2
}));
```

Bot 端会收到 `web_app_data` 类型的消息。

### 4.9 打开外部链接

```javascript
// 在外部浏览器打开链接
tg.openLink('https://example.com');

// 在 Telegram 内打开链接（instant view）
tg.openTelegramLink('https://t.me/channel');
```

### 4.10 二维码扫描

```javascript
// 调用扫码
tg.scanQrText((text) => {
    console.log('扫描结果:', text);
    tg.showAlert('扫描到：' + text);
});
```

### 4.11 设备震动

```javascript
// 短震动
tg.HapticFeedback.selectionChanged();

// 成功震动
tg.HapticFeedback.notificationOccurred('success');

// 失败震动
tg.HapticFeedback.notificationOccurred('error');

// 警告震动
tg.HapticFeedback.notificationOccurred('warning');
```

### 4.12 用户身份验证（重要）

::: danger 🔐 后端验证必须做
如果你有后端服务，必须验证用户身份的真实性，防止伪造请求。
:::

**前端获取验证数据：**

```javascript
// 将 initData 发送给后端验证
const initData = tg.initData;
// 发送到后端：GET /api/validate?initData=...
```

**后端验证（Node.js 示例）：**

```javascript
const crypto = require('crypto');

function validateTelegramInitData(initData, botToken) {
    const params = new URLSearchParams(initData);
    const hash = params.get('hash');
    params.delete('hash');
    
    // 按字母顺序排列参数
    const dataCheckArr = [];
    params.forEach((value, key) => {
        dataCheckArr.push(`${key}=${value}`);
    });
    dataCheckArr.sort();
    
    const dataCheckString = dataCheckArr.join('\n');
    
    // 使用 Bot Token 生成 HMAC-SHA256
    const secretKey = crypto.createHmac('sha256', 'WebAppData')
        .update(botToken)
        .digest();
    
    const calculatedHash = crypto.createHmac('sha256', secretKey)
        .update(dataCheckString)
        .digest('hex');
    
    // 对比 hash
    return calculatedHash === hash;
}

// 使用示例
const isValid = validateTelegramInitData(
    req.query.initData,
    'YOUR_BOT_TOKEN'
);

if (!isValid) {
    return res.status(401).json({ error: '无效的用户身份' });
}
```

---

## 五、TON 钱包集成

### 5.1 为什么要集成 TON 钱包？

TON 是 Telegram 原生支持的区块链，集成后可以实现：

- 数字货币支付
- 钱包连接
- 智能合约交互
- NFT 铸造和交易

### 5.2 连接 Tonkeeper 钱包

最常用的 TON 钱包是 [Tonkeeper](https://tonkeeper.com/)，通过官方 SDK 可以在 Mini App 中连接：

```html
<!-- 引入 TonConnect SDK -->
<script src="https://unpkg.com/@tonconnect/ui@latest/dist/tonconnect-ui.min.js"></script>
```

```javascript
// 初始化 TonConnect UI
const tonConnectUI = new TON_CONNECT_UI.TonConnectUI({
    manifestUrl: 'https://your-app.com/tonconnect-manifest.json',
    buttonRootId: 'ton-connect-btn'
});

// 监听连接状态
tonConnectUI.onStatusChange((wallet) => {
    if (wallet) {
        console.log('钱包已连接:', wallet.account.address);
        document.getElementById('wallet-status').textContent = 
            '已连接: ' + wallet.account.address.slice(0, 8) + '...';
    } else {
        console.log('钱包未连接');
        document.getElementById('wallet-status').textContent = '未连接';
    }
});
```

**创建 manifest 文件 (`tonconnect-manifest.json`)：**

```json
{
  "url": "https://your-app.com",
  "name": "Your App Name",
  "iconUrl": "https://your-app.com/icon.png"
}
```

### 5.3 发起一笔 TON 转账

```javascript
async function sendTransaction() {
    if (!tonConnectUI.connected) {
        alert('请先连接钱包');
        return;
    }
    
    const transaction = {
        validUntil: Math.floor(Date.now() / 1000) + 60 * 5, // 5分钟有效
        messages: [
            {
                address: 'EQD...收款地址...', // 收款钱包地址
                amount: '10000000', // 金额，单位是 nanoTON（1 TON = 10^9 nanoTON）
                payload: '' // 可选：消息附加数据
            }
        ]
    };
    
    try {
        const result = await tonConnectUI.sendTransaction(transaction);
        console.log('交易成功:', result);
        alert('转账成功！');
    } catch (e) {
        console.error('交易失败:', e);
        alert('转账失败：' + e.message);
    }
}
```

::: tip 💡 单位换算
TON 的最小单位是 nanoTON：
- 1 TON = 1,000,000,000 nanoTON（10^9）
- 0.01 TON = 10,000,000 nanoTON
- 代码中使用的金额都要转成 nanoTON
:::

---

## 六、实战项目：简易积分商城

让我们用所学知识，做一个完整的 Mini App —— 积分商城。

### 6.1 项目结构

```
points-shop/
├── index.html          # 主页面
├── styles.css          # 样式
└── app.js              # 逻辑
```

### 6.2 HTML 结构

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>积分商城</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <header class="header">
            <div class="user-info">
                <div class="avatar" id="avatar">👤</div>
                <div>
                    <div class="username" id="username">加载中...</div>
                    <div class="points">积分：<span id="points">0</span></div>
                </div>
            </div>
        </header>

        <section class="goods-list">
            <h2>商品列表</h2>
            <div class="goods-grid" id="goodsGrid">
                <!-- 商品会通过 JS 动态生成 -->
            </div>
        </section>
    </div>

    <div id="connectWalletBtn" class="wallet-btn-container">
        <!-- TonConnect 按钮挂载点 -->
        <div id="ton-connect-btn"></div>
    </div>

    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <script src="https://unpkg.com/@tonconnect/ui@latest/dist/tonconnect-ui.min.js"></script>
    <script src="app.js"></script>
</body>
</html>
```

### 6.3 CSS 样式

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    background: var(--tg-theme-bg-color, #f5f5f5);
    color: var(--tg-theme-text-color, #333);
    padding-bottom: 80px;
}

.container {
    padding: 16px;
    max-width: 600px;
    margin: 0 auto;
}

.header {
    background: var(--tg-theme-secondary-bg-color, #fff);
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 20px;
}

.user-info {
    display: flex;
    align-items: center;
    gap: 12px;
}

.avatar {
    width: 50px;
    height: 50px;
    background: var(--tg-theme-button-color, #2481cc);
    color: var(--tg-theme-button-text-color, #fff);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
}

.username {
    font-size: 16px;
    font-weight: 600;
}

.points {
    font-size: 14px;
    color: var(--tg-theme-hint-color, #666);
    margin-top: 4px;
}

.goods-list h2 {
    font-size: 18px;
    margin-bottom: 16px;
}

.goods-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
}

.goods-item {
    background: var(--tg-theme-secondary-bg-color, #fff);
    border-radius: 12px;
    padding: 16px;
    text-align: center;
}

.goods-icon {
    font-size: 48px;
    margin-bottom: 8px;
}

.goods-name {
    font-size: 14px;
    font-weight: 600;
    margin-bottom: 4px;
}

.goods-price {
    font-size: 12px;
    color: var(--tg-theme-hint-color, #666);
    margin-bottom: 12px;
}

.buy-btn {
    background: var(--tg-theme-button-color, #2481cc);
    color: var(--tg-theme-button-text-color, #fff);
    border: none;
    padding: 8px 16px;
    border-radius: 8px;
    font-size: 12px;
    cursor: pointer;
    width: 100%;
}

.wallet-btn-container {
    position: fixed;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
}
```

### 6.4 JavaScript 逻辑

```javascript
const tg = window.Telegram.WebApp;
tg.ready();
tg.expand();

// 商品数据（实际项目中应从后端获取）
const goods = [
    { id: 1, name: 'VIP 会员', icon: '👑', price: 100, priceTON: 0.5 },
    { id: 2, name: '头像框', icon: '💎', price: 50, priceTON: 0.2 },
    { id: 3, name: '专属贴纸', icon: '🎨', price: 30, priceTON: 0.1 },
    { id: 4, name: '神秘盲盒', icon: '🎁', price: 80, priceTON: 0.3 }
];

// 当前用户积分（实际应从后端获取）
let userPoints = 150;

// 初始化
function init() {
    const user = tg.initDataUnsafe.user;
    if (user) {
        document.getElementById('username').textContent = 
            user.first_name + (user.last_name ? ' ' + user.last_name : '');
        if (user.photo_url) {
            document.getElementById('avatar').innerHTML = 
                `<img src="${user.photo_url}" style="width:100%;height:100%;border-radius:50%;">`;
        }
    }
    
    updatePoints();
    renderGoods();
    initTonConnect();
}

// 更新积分显示
function updatePoints() {
    document.getElementById('points').textContent = userPoints;
}

// 渲染商品列表
function renderGoods() {
    const grid = document.getElementById('goodsGrid');
    grid.innerHTML = goods.map(item => `
        <div class="goods-item">
            <div class="goods-icon">${item.icon}</div>
            <div class="goods-name">${item.name}</div>
            <div class="goods-price">${item.price} 积分 / ${item.priceTON} TON</div>
            <button class="buy-btn" onclick="buyWithPoints(${item.id})">积分兑换</button>
            <button class="buy-btn" style="margin-top:6px;background:#0088cc;" onclick="buyWithTON(${item.id})">TON 购买</button>
        </div>
    `).join('');
}

// 积分购买
function buyWithPoints(goodsId) {
    const item = goods.find(g => g.id === goodsId);
    
    if (userPoints < item.price) {
        tg.showAlert('积分不足！');
        return;
    }
    
    tg.showConfirm(`确定用 ${item.price} 积分兑换「${item.name}」吗？`, (confirmed) => {
        if (confirmed) {
            userPoints -= item.price;
            updatePoints();
            tg.showAlert(`兑换成功！获得「${item.name}」`);
            
            // 通知 Bot
            tg.sendData(JSON.stringify({
                action: 'buy_points',
                goods_id: goodsId
            }));
        }
    });
}

// 初始化 TonConnect
let tonConnectUI;
function initTonConnect() {
    tonConnectUI = new TON_CONNECT_UI.TonConnectUI({
        manifestUrl: 'https://your-app.com/tonconnect-manifest.json',
        buttonRootId: 'ton-connect-btn'
    });
}

// TON 购买
async function buyWithTON(goodsId) {
    const item = goods.find(g => g.id === goodsId);
    
    if (!tonConnectUI.connected) {
        tg.showAlert('请先连接钱包！');
        return;
    }
    
    const amountNano = (item.priceTON * 1e9).toString();
    
    try {
        const result = await tonConnectUI.sendTransaction({
            validUntil: Math.floor(Date.now() / 1000) + 300,
            messages: [
                {
                    address: 'YOUR_WALLET_ADDRESS', // 商户收款地址
                    amount: amountNano,
                    payload: btoa(JSON.stringify({ goods_id: goodsId }))
                }
            ]
        });
        
        tg.showAlert(`购买成功！获得「${item.name}」`);
        userPoints += 10; // 购买奖励积分
        updatePoints();
        
    } catch (e) {
        tg.showAlert('支付失败：' + e.message);
    }
}

// 启动
init();
```

---

## 七、调试技巧

### 7.1 在浏览器中调试

开发时可以直接在电脑浏览器中打开页面调试：

```
https://your-app.com
```

但要注意：浏览器中没有 Telegram SDK，`window.Telegram.WebApp` 可能不存在。

**解决方案：使用 Mock 数据**

```javascript
// 开发环境 Mock
if (!window.Telegram) {
    window.Telegram = {
        WebApp: {
            ready: () => {},
            expand: () => {},
            close: () => window.close(),
            showAlert: (msg, cb) => { alert(msg); cb && cb(); },
            showConfirm: (msg, cb) => cb && cb(confirm(msg)),
            MainButton: {
                setText: () => {},
                show: () => {},
                hide: () => {},
                onClick: () => {},
                showProgress: () => {},
                hideProgress: () => {}
            },
            BackButton: { show: () => {}, hide: () => {}, onClick: () => {} },
            initDataUnsafe: {
                user: {
                    id: 123456789,
                    first_name: '测试',
                    last_name: '用户',
                    username: 'testuser',
                    language_code: 'zh'
                }
            },
            initData: 'test_init_data',
            themeParams: {}
        }
    };
}
```

### 7.2 在 Telegram 中调试

**方法一：使用测试 Bot**
- 创建一个测试用的 Bot
- 配置测试环境的 URL
- 在 Telegram 中直接打开调试

**方法二：使用 Chrome 开发者工具**
- 电脑版 Telegram 中打开 Mini App
- 右键选择"检查"或"开发者工具"
- 像普通网页一样调试

### 7.3 常见问题排查

| 问题 | 可能原因 | 解决方法 |
|:---|:---|:---|
| 页面白屏 | JS 报错 | 打开控制台查看错误 |
| SDK 未加载 | 网络问题或路径错 | 检查 script 标签 URL |
| 打开空白页 | HTTPS 证书问题 | 确保域名有有效 SSL 证书 |
| 用户信息为空 | 非 Telegram 环境 | 正常，开发环境用 Mock |
| 支付失败 | 地址或金额格式错 | 检查地址和单位（nanoTON） |

---

## 八、发布与上线

### 8.1 上线检查清单

发布前请确认：

- [ ] 页面在 iOS/Android 上都能正常显示
- [ ] 适配深色/浅色模式
- [ ] 所有按钮和功能测试通过
- [ ] 后端接口安全验证已实现
- [ ] HTTPS 证书有效
- [ ] 加载速度优化（压缩图片和代码）
- [ ] 错误处理和用户提示完善

### 8.2 推广你的 Mini App

**1. 通过 Bot 菜单**
- 用户和 Bot 聊天时点击菜单按钮打开

**2. 通过内联按钮**
- 在频道消息中添加按钮，点击打开 Mini App

**3. 通过链接分享**
- `https://t.me/your_bot/yourapp`
- 可以发在频道、群组或其他平台

**4. 通过内联查询**
- 在聊天中输入 `@your_bot query` 调用 Mini App

### 8.3 数据统计

可以通过以下方式统计使用情况：

- **Google Analytics / 百度统计**：嵌入统计代码
- **自定义埋点**：后端记录用户行为
- **Bot API**：通过 Bot 获取用户数据

---

## 九、常见问题 FAQ

### Q1: Mini App 和 Bot 有什么区别？

Bot 是通过消息命令交互的，而 Mini App 是图形界面的网页应用，交互更丰富，可以做更复杂的功能。

### Q2: 开发 Mini App 需要服务器吗？

简单的静态页面可以不需要后端（纯前端），但如果需要数据库、用户系统、支付等功能，就需要后端服务。

### Q3: Mini App 支持哪些前端框架？

所有前端框架都支持！React、Vue、Angular、Svelte 都可以，因为 Mini App 本质上就是网页。

### Q4: 可以在 Mini App 中使用支付吗？

可以。有几种方式：
1. **Stars 支付**：Telegram 官方星币支付
2. **TON 支付**：通过 TON 钱包转账
3. **第三方支付**：集成支付宝、微信等（需跳转）

### Q5: Mini App 审核严格吗？

相比于苹果 App Store，Telegram Mini App 的审核要宽松得多。你只需要有一个 Bot 和一个 HTTPS 网页，就可以发布。但内容必须遵守 Telegram 服务条款。

### Q6: 如何让更多人使用我的 Mini App？

- 优化 SEO（搜索引擎可能收录）
- 在频道和群组中推广
- 与其他 Bot/频道合作互推
- 提供有价值的功能，让用户自发分享

---

## 十、进阶学习资源

### 官方文档

| 资源 | 地址 |
|:---|:---|
| **Telegram Web Apps 官方文档** | [core.telegram.org/bots/webapps](https://core.telegram.org/bots/webapps) |
| **Bot API 文档** | [core.telegram.org/bots/api](https://core.telegram.org/bots/api) |
| **TON 开发者文档** | [ton.org/docs](https://ton.org/docs) |
| **TonConnect 文档** | [docs.ton.org/.../ton-connect](https://docs.ton.org/develop/dapps/ton-connect/overview) |

### 开源项目

| 项目 | 说明 |
|:---|:---|
| **telegram-web-apps** | 官方示例和模板 |
| **tonstarter** | TON DApp 脚手架 |
| **create-ton** | TON 项目创建工具 |

### 学习路线

```
第1步：掌握 HTML/CSS/JS 基础
  ↓
第2步：用原生 JS 做一个简单 Mini App
  ↓
第3步：学习主流前端框架（React/Vue）
  ↓
第4步：集成 TON 钱包和支付
  ↓
第5步：学习智能合约开发（FunC/Tact）
  ↓
第6步：做一个完整的 Web3 应用
```

---

## 十一、总结

### 开发流程回顾

```
1. 创建 Bot（通过 @BotFather）
        ↓
2. 开发网页（任何前端技术栈）
        ↓
3. 部署到 HTTPS 服务器
        ↓
4. 配置 Bot Web App（@BotFather）
        ↓
5. 测试和调试
        ↓
6. 发布和推广
```

### 给初学者的建议

1. **从简单开始**：先做一个纯静态的展示页，逐步增加功能
2. **善用官方文档**：遇到问题先查官方文档
3. **多看别人的作品**：研究优秀的 Mini App 是怎么做的
4. **先验证再开发**：想好需求再动手，避免返工
5. **关注安全**：后端一定要验证用户身份

::: tip 最后想说
Telegram Mini App 生态正在快速发展，现在正是入场的好时机。

你不需要复杂的技术，一个简单的 HTML 页面也能成为一个有用的 Mini App。最重要的是**找到用户的真实需求**，然后用最小的成本去验证。

打开编辑器，开始你的第一个 Mini App 吧！🚀
:::

---

**相关阅读：**

- [创建机器人教程](../../createrobot.md) — Bot 开发基础
- [API 入门指南](../../api-intro.md) — Bot API 详解
- [TON 钱包入门](../ton/wallet.md) — TON 钱包使用
- [TON DEX 交易指南](../ton/dex.md) — TON 生态应用
- [热门小程序与游戏](./games.md) — 现成的小程序推荐
- [空投游戏完全指南](./airdrop.md) — Tap-to-Earn 游戏介绍