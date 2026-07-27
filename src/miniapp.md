---
title: Telegram小程序(Mini App)开发入门与使用指南 (TON生态)
shortTitle: 小程序MiniApp
description: 像微信一样用Telegram！详解Telegram Mini App（小程序）生态，教你如何打开小程序、添加到主屏幕以及基础开发文档入口。
icon: microchip
category:
  - 开发者
tag:
  - 小程序
  - MiniApp

head:
  - - meta
    - name: keywords
      content: Telegram小程序,Telegram迷你应用程序,Telegram Mini App,Telegram Web App,TG小程序,TG迷你应用程序,TG Mini App,TG Web App,电报小程序,电报迷你应用程序,电报 Mini App,电报 Web App
---

# Telegram小程序(Mini App)开发入门与使用指南 (TON生态)

Telegram小程序（迷你应用程序）不仅仅是一个简单的工具，而且是一个可以替代普通网站的强大平台。

::: tip

本知识库完成了Telegram小程序的初步适配，您可以打开 [@TGwikiAppBot](https://t.me/TGwikiAppBot/tgwiki) 进行体验。

:::

## 功能和特性

以下是一些主要功能：

- 灵活的界面：开发者可以使用JavaScript创建无限灵活的前端应用，直接在Telegram内启动小程序。
- 无缝授权：小程序支持无缝授权，用户可以方便地登录和使用。
- 集成支付：支持20多家支付提供商，包括Google Pay和Apple Pay，方便用户进行支付。
- 推送通知：小程序可以向用户发送定制的推送通知，保持用户的参与度。
- 多种启动方式：小程序可以通过键盘按钮、内联按钮、机器人菜单按钮、内联模式、直接链接和附件菜单启动。
- 与区块链交互：小程序可以与区块链和智能合约直接交互，提高账户安全性。

::: details 界面截图

![tfa-miniapp1.jpg](https://cdn.jsdelivr.net/gh/tgwiki/images/tfa/miniapp1.jpg)

![tfa-miniapp2.jpg](https://cdn.jsdelivr.net/gh/tgwiki/images/tfa/miniapp2.jpg)

:::

## 创建小程序

1. 创建机器人：按照 [教程](./createrobot.html) 创建一个机器人。

2. 私聊 [@BotFather](https://t.me/BotFather) ，点击`Menu`（菜单）-> 点击 `/mybots`（我的机器人）->选择机器人->点击`Bot Settings`->点击`Configure Mini App`->`Enable Mini App`

3. 发送`/newapp`命令。选择你想要创建小程序的机器人。

   ::: details 操作演示

   ![tfa-miniapp3.jpg](https://cdn.jsdelivr.net/gh/tgwiki/images/tfa/miniapp3.jpg)

   :::

4. 为你的小程序提供一个标题、简短的描述和一张图片（尺寸必须为`640`x`360`）。上传预览GIF（发送`/empty`跳过）。

   ::: details 操作演示

   ![tfa-miniapp4.jpg](https://cdn.jsdelivr.net/gh/tgwiki/images/tfa/miniapp4.jpg)

   :::

5. 设置小程序打开时显示的URL。设置一个小程序短后缀（`3`~`30`字符），用户将可以使用`t.me/your_robot/short_name`链接直接打开小程序。

   ::: details 操作演示

   ![tfa-miniapp5.jpg](https://cdn.jsdelivr.net/gh/tgwiki/images/tfa/miniapp5.jpg)

   :::

6. 配置服务器并开发小程序

   Telegram小程序支持丰富的前端功能，可以与用户进行交互。你可以使用 Telegram 提供的 Web App JS SDK 来与 Telegram 客户端进行交互（如获取用户信息、触感反馈、拉起支付等）。

::: tip 💡 完整开发实战教程
想从零开始搭建你的第一个 Mini App？请参阅我们的深度实战教程：[Telegram Mini App 开发入门与实战](./topics/game/miniapp-dev.md)，包含前端环境配置、TON 钱包集成、支付功能以及简易积分商城项目代码。
:::

::: info

有关 Telegram 小程序官方 API 规范，亦可参阅 [Telegram Mini Apps 官方文档](https://core.telegram.org/bots/webapps)。

:::

---

## 相关阅读

- [Telegram Mini App 开发入门与实战](./topics/game/miniapp-dev.md) — 零基础开发第一个小程序
- [机器人创建教程](./createrobot.md) — 零基础创建 BotFather 机器人
- [API 开发者入门](./api-intro.md) — Bot API 与 Telegram 开发全景
- [热门小程序与工具汇总](./topics/game/tools.md) — 常用 Mini App 推荐

