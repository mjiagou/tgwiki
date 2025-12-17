---
title: Combot 机器人设置指南：群组活跃度统计、积分排行与防垃圾系统
shortTitle: Combot积分排行
description: 想知道群里谁最活跃？教你使用 Combot 开启群组成员发言排行榜，设置积分系统(XP/Levels)，以及开启 CAS 系统自动拦截恶意广告账号。
icon: chart-line
order: 2
category:
  - 运营工具
tag:
  - Combot
  - 数据统计
  - 积分
---

# Combot 机器人设置指南：群组活跃度统计、积分排行与防垃圾系统

## 为什么选择 Combot？

如果说 Rose 是“管家”，那 **Combot** 就是“数据分析师”。它最强大的功能是**CAS 防垃圾系统**和**群组成员活跃度统计**。

* **机器人 ID**: `@combot`
* **后台管理**: [combot.org](https://combot.org) (网页端设置，功能更强大)

<!-- ![Combot官网后台管理界面](/assets/images/bot/combot-dashboard.jpg) -->

## 核心功能一：开启 CAS 防垃圾系统

CAS (Combot Anti-Spam) 是 Telegram 最著名的第三方反垃圾数据库。如果一个账号在别的群发广告被举报，CAS 会将其拉黑。一旦开启 CAS，这个账号进你的群就会被秒踢。

**设置步骤：**
1.  将 `@combot` 拉入群组并设为管理员。
2.  登录 [Combot 官网](https://combot.org)，点击 **My Groups**。
3.  找到你的群组，点击 **Settings** -> **Moderation**。
4.  找到 **CAS (Combot Anti-Spam)** 选项，将其开启 (Enabled)。
5.  Action 选择 **Ban** (封禁) 或 **Kick** (踢出)。

<!-- ![开启CAS防垃圾设置](/assets/images/bot/combot-cas.jpg) -->

## 核心功能二：活跃度统计与积分排行

想让群员多说话？开启排行榜是最好的激励。

**如何开启：**
1.  在 Combot 网页后台，点击 **Settings** -> **Levels & XP**。
2.  勾选 **Enable leveling system**。
3.  设置 **Announcement mode** (升级通知)：可以选择在群里发消息通知“恭喜 xxx 升到了 Lv.5”。

**查看排行：**
* 群员在群里发送 `/top`，Combot 就会发送一张当前的积分排行榜列表。
* 发送 `/myxt` 或 `/me`，查看自己的等级和积分。

<!-- ![Combot群组活跃度排行榜演示](/assets/images/bot/combot-top.jpg) -->

## 核心功能三：数据分析报表

Combot 会生成详细的群组数据报表，包括：
* **每日消息量趋势图**
* **活跃成员数 (DAU)**
* **最活跃的时间段** (帮你决定什么时候发公告效果最好)

这些数据在 Combot 官网点击 **Analytics** 即可查看，完全免费。