---
title: Telegram 代理设置与 MTProto 自建防封锁完全攻略
shortTitle: 代理设置
description: 觉得 Telegram 连接不稳定或太慢？本文详解 Telegram 内置代理设置（SOCKS5/MTProto），提供主流代理软件（Clash Verge/Sing-box/v2rayN）本地端口查看方法，并包含使用 Docker 自建 MTProto 混淆代理（含赞助频道设置）的详细教程。
icon: network-wired
category:
  - 基础教程
tag:
  - 代理
  - 网络
  - MTProto
  - Docker
head:
  - - meta
    - name: keywords
      content: Telegram代理设置,Telegram代理,Telegram内置代理,Telegram自定义代理,MTProto代理,自建MTProto,Socks5代理,TG代理,电报代理,Clash端口,Sing-box代理
---

# Telegram 代理设置与 MTProto 自建防封锁完全攻略

在部分网络环境下，Telegram 可能会出现“一直处于连接中 (Connecting...)”或收发消息缓慢的情况。除了使用常规 VPN 全局代理外，Telegram 内置了极强的**代理 (Proxy)** 支持。

本文将为您详解如何配置本地客户端代理、常见代理软件的默认端口、SOCKS5 与 MTProto 的区别，以及如何使用 Docker 在 VPS 上自建防封锁的 MTProto 混淆代理。

---

## 一、主流客户端本地代理配置指南

大多数时候，我们电脑或手机上已经运行了代理软件（如 Clash Verge, Sing-box, v2rayN 等）。我们可以直接配置 Telegram 客户端，让其**直连本地代理软件的端口**，而无需开启系统全局代理。

### 1.1 Telegram Desktop (Windows / macOS / Linux)
Telegram 桌面端默认不走系统代理，需要手动配置：
1. 打开 Telegram 桌面版 -> 左上角菜单 -> **设置 (Settings)** -> **高级 (Advanced)**。
2. 找到 **网络和代理 (Connection type)** -> 点击 **代理类型 (Proxy)**。
3. 选择 **使用自定义代理 (Use custom proxy)** -> 点击 **添加代理 (Add proxy)**。
4. 选择 **SOCKS5**（推荐）或 **HTTP**：
   - **服务器 (Server)**：输入 `127.0.0.1`（代表本机本地环回地址）。
   - **端口 (Port)**：填写你的代理软件本地监听端口（查看下表）。
   - **用户名/密码**：留空即可。
5. 点击 **保存 (Save)**。

::: details 🖥️ 常见代理软件默认端口一览表
| 代理软件名称 | 默认 SOCKS5 端口 | 默认 HTTP 端口 |
| :--- | :--- | :--- |
| **Clash Verge / Clash for Windows** | `7890` | `7890` (混合端口) |
| **Sing-box** | `2080` (取决于配置) | `2080` (取决于配置) |
| **v2rayN** | `10808` | `10809` |
| **xray / 3X-UI 客户端** | `1080` | `1081` |
| **Shadowsocks (SS/SSR)** | `1080` | `1080` |
| **ClashX (macOS)** | `7891` | `7890` |
| **V2rayU (macOS)** | `1080` | `1087` |
:::

### 1.2 Telegram macOS 原生端 (Telegram for macOS)
注意，Mac App Store 下载的原生端与 Telegram Lite (Desktop) 设置略有不同：
- **配置路径**：`设置 (Settings)` -> `数据与存储 (Data and Storage)` -> `使用代理 (Use Proxy)` -> `添加代理 (Add proxy)`。
- **配置参数**：服务器同样填 `127.0.0.1`，端口填写对应的 Mac 代理软件端口（如 ClashX 的 `7891`）。
- **提示**：如果在 Mac 上代理软件开启了 **“增强模式 (Enhanced Mode) / Tun 模式”**，则 Telegram 会自动走全局代理，无需在客户端内单独配置。

### 1.3 Telegram iOS / Android 移动端
- 在手机上，Shadowrocket (小火箭)、Loon、Surge、Clash 或 v2rayNG 等代理软件启动后会自动接管整机的网络流量（TUN/VPN 虚拟网卡模式），因此**无需在 Telegram App 内做额外配置**。
- 如果 Telegram 依旧连不上，请检查代理软件的**分流规则**，确保 `telegram.org`、`telegram.me`、`t.me` 以及 Telegram 的服务器 IP 段没有被错误拦截。

---

## 二、SOCKS5 vs MTProto 代理对比

内置代理支持两种主要协议：

| 维度 | SOCKS5 代理 | MTProto 代理 (Telegram 专属) |
| :--- | :--- | :--- |
| **协议类型** | 通用网络代理协议 | Telegram 专用混淆协议 |
| **安全性** | 流量本身加密，但握手特征明显 | 高度混淆（Fake-TLS），伪装成常规 HTTPS |
| **搭建难度** | 简单，但极易被防火墙 (GFW) 识别并封锁 IP | 略高，防封锁能力极强 |
| **商业/运营特权**| 无 | 支持**绑定赞助频道 (Sponsored Channel)** |
| **适用范围** | 几乎所有软件均可使用 | 仅限 Telegram 官方及第三方客户端 |

---

## 三、实战：使用 Docker 自建 MTProto 混淆代理

如果你拥有一台海外的 VPS（虚拟专用服务器），可以轻松搭建一个专供自己和朋友使用的 MTProto 代理。我们采用官方推荐的 **Fake-TLS** 混淆方案，让代理流量看起来像在访问正常的知名网站（如 `cloudflare.com`），从而防封锁。

### 3.1 步骤一：生成混淆密钥 (Secret)
登录 VPS 终端，运行以下命令生成一个符合 Telegram 规范的 32 位十六进制随机密钥：
```bash
openssl rand -hex 16
```
假定生成的密钥为：`a1b2c3d4e5f67890abcdef1234567890`。

为了启用 Fake-TLS 混淆，我们必须在密钥前加上 `ee` 前缀，并后缀上一个知名网站域名的十六进制编码。例如，我们使用 `ee` 前缀，并加上 `cloudflare.com` 的十六进制（`636c6f7564666c6172652e636f6d`），拼接后的密钥格式为：
`eea1b2c3d4e5f67890abcdef1234567890636c6f7564666c6172652e636f6d`。

### 3.2 步骤二：使用 Docker 一键运行
在 VPS 上安装 Docker，然后执行以下命令启动代理服务。我们将服务端口设为 `443`（标准的 HTTPS 端口，混淆效果最好）：

```bash
docker run -d -p 443:443 --name mtproto-proxy --restart=always \
  -e SECRET=eea1b2c3d4e5f67890abcdef1234567890636c6f7564666c6172652e636f6d \
  -e TAG=YOUR_PROMO_TAG_HERE \
  telegrammessenger/proxy:latest
```

::: tip 💡 关于 TAG 环境变量
`TAG` 是用来关联赞助频道的标识符。如果你不需要在代理中推广频道，可以删除 `-e TAG=...` 这一行。
:::

### 3.3 步骤三：在 `@MTProxybot` 中注册并关联赞助频道
如果你希望所有使用你这个代理的用户，其聊天列表最上方都会置顶显示你的频道（即赞助频道）：

1. 在 Telegram 中私聊官方 [@MTProxybot](https://t.me/MTProxybot)。
2. 发送 `/newproxy` 开启向导。
3. 按照提示输入你的代理服务器：`IP:443`。
4. 输入你的 `Secret` 密钥（必须是不含 `ee` 前缀的原始 32 位十六进制密钥，例如 `a1b2c3d4e5f67890abcdef1234567890`）。
5. 机器人会返回给你一个 **Tag**（推广标识，例如 `34d1ab3...`），将其填入上文 Docker 命令的 `TAG` 变量中，重新运行 Docker 容器。
6. 在机器人中发送 `/myproxies` 选择你的代理，点击 **Set promotion**，输入你想要推广的频道用户名（例如 `@mychannel`）即可完成绑定。

### 3.4 步骤四：分享与连接
配置完成后，你可以将链接发给朋友或直接在浏览器打开：
- **链接格式**：`https://t.me/proxy?server=你的VPS_IP&port=443&secret=eea1b2c3d4e5f67890abcdef1234567890636c6f7564666c6172652e636f6d`
- 点击此链接后，手机或电脑客户端会弹出确认窗口，点击“启用代理”即可。

---

## 四、安全与风险防范须知

### 4.1 使用公共 MTProto 代理安全吗？
网络上存在很多免费分享的 MTProto 代理渠道。使用这些公共代理的安全性分析如下：
- **消息内容安全**：**绝对安全。** Telegram 的所有聊天流量在客户端发出前已经过了端到端或客户端到服务器的强加密（MTProto 协议本身）。代理服务器充当的是中继角色，**无法解密和窥探你的聊天内容、密码或图片**。
- **隐私泄露风险**：**中等。** 代理服务器所有者可以知道你的**真实公网 IP 地址**、你连接 Telegram 的**时间段**以及**产生的数据流量大小**。
- **骚扰风险**：**低。** 使用他人的免费代理，你的聊天列表顶部会被强制置顶显示对方的“赞助频道”（通常为广告、币圈群等），可能会打扰日常使用。

### 4.2 警惕修改版内置代理客户端
很多非官方的 Telegram “汉化版”、“特权版”客户端，宣称“内置免代理直连”。此类客户端通常被植入了恶意后门，能够绕过加密直接读取你的聊天记录，甚至自动给他人发送垃圾群发消息。**请务必只从官网或正规应用商店下载官方客户端**。