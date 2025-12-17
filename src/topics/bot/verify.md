---
title: 如何防止炸群广告？Telegram 群组开启“入群验证” (CAPTCHA) 教程
shortTitle: 入群验证设置
description: 群里总有阿拉伯人发广告？本文推荐几款好用的入群验证机器人(Group Help / Rose)，开启算术验证或按钮验证，将广告机器人拒之门外。
icon: user-shield
order: 3
category:
  - 运营工具
tag:
  - 防广告
  - 验证码
---

# 如何防止炸群广告？Telegram 群组开启“入群验证” (CAPTCHA) 教程

## 为什么必须开启入群验证？

Telegram 上有海量的“广告机器人”，它们会自动扫描公开群组，进群瞬间发送大量博彩、色情广告（俗称“炸群”）。

**入群验证 (Captcha)** 的原理是：新成员进群后，**默认被禁言**。只有在规定时间内（如 60 秒）点击了验证按钮或回答了算术题，才能解开禁言权限。机器号无法完成此操作，就会被踢出。

## 方案一：使用 Rose 开启按钮验证 (最简单)

Miss Rose 自带验证功能，设置非常简单。

1.  确保 Rose 是管理员。
2.  在群里发送命令：`/captcha on` (开启验证)。
3.  **设置模式**: `/captchamode button` (设置为点击按钮模式，体验最好)。
4.  **设置验证文字**: `/setcaptchatext 欢迎 {fullname}！请在 1 分钟内点击下方按钮，否则将被踢出。`
5.  **查看效果**: 找个小号退群重进试试。

<!-- ![Rose按钮验证效果截图](/assets/images/bot/verify-button.jpg) -->

## 方案二：使用 Group Help 开启算术验证

如果你觉得点击按钮太容易被破解，可以使用 `@GroupHelpBot` 进行算术验证。

1.  邀请 `@GroupHelpBot` 入群并给管理员权限。
2.  发送 `/settings` 打开设置面板。
3.  点击 **Security** (安全) -> **Welcome & Captcha**。
4.  选择 **Captcha**，将其状态设为 ✅。
5.  在 **Type** 中选择 **Math** (算术题)。

<!-- ![GroupHelp算术验证设置](/assets/images/bot/verify-math.jpg) -->

## 方案三：Telegram 原生验证 (无需机器人)

Telegram 官方最近也更新了原生的入群验证功能（适合频道关联的群组）。

1.  进入群组 **Manage Group** (管理群组)。
2.  点击 **Members** (成员) -> **Permissions** (权限)。
3.  在底部找到 **Approve New Members** (批准新成员)。
4.  开启后，任何人进群都需要管理员手动点击“通过”，或者生成一个**带有申请门槛的邀请链接**。

::: tip 建议
对于 500 人以下的群组，开启 Rose 的按钮验证通常就足够拦截 99% 的广告号了，且不会太影响真实用户的体验。
:::