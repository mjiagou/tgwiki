---
title: Telegram群管神器 Miss Rose 机器人中文指令详解与设置教程
shortTitle: Rose机器人
description: 全球第一的Telegram群管机器人！本文提供Miss Rose机器人的常用中文指令对照表，教你设置进群欢迎语、自动踢人、定时消息和关键词回复，轻松管理十万人大群。
icon: robot
order: 1
category:
  - 运营工具
tag:
  - Rose
  - 机器人
  - 群管理
---

# Telegram群管神器 Miss Rose 机器人中文指令详解与设置教程

## 什么是 Miss Rose？

**Miss Rose** (简称 Rose) 是 Telegram 上最流行、功能最全面的免费群组管理机器人。它可以帮你自动删除垃圾广告、欢迎新成员、设置定时公告，甚至进行验证码验证。

* **机器人 ID**: `@MissRose_bot`
* **适用场景**: 从 5 人的小群到 200,000 人的超级群组。

<!-- ![Miss Rose机器人官方简介](/assets/images/bot/rose-profile.jpg) -->

## 第一步：将 Rose 添加到群组

1.  打开你的群组，点击群名进入设置。
2.  点击 **Add Member** (添加成员)。
3.  搜索 `@MissRose_bot` 并邀请入群。
4.  **关键步骤**：入群后，必须将 Rose **提升为管理员 (Promote to Admin)**，并给予所有权限，否则它无法执行踢人或删除消息的操作。

<!-- ![将Rose设置为群管理员](/assets/images/bot/rose-admin.jpg) -->

## 常用指令中文对照表

Rose 的指令非常多，这里列出群主最常用的几个。**注意：所有指令必须在群组内发送。**

### 1. 基础管理
* `/adminlist`: 查看当前群组的管理员列表。
* `/id`: 获取当前群组或回复用户的 ID。
* `/pin`: 置顶回复的那条消息（需开启“通知成员”权限）。

### 2. 欢迎新成员 (Welcome)
让进群更有仪式感。

* **开启欢迎语**: `/welcome on`
* **设置欢迎内容**: `/setwelcome 欢迎 {fullname} 加入本群！请先阅读置顶消息。`
    * `{fullname}`: 自动替换为成员名字。
    * `{id}`: 成员的 ID。
* **预览效果**: `/welcome`

<!-- ![Rose设置欢迎语效果演示](/assets/images/bot/rose-welcome.jpg) -->

### 3. 过滤器 (关键词自动回复)
当群员发送特定词汇时，Rose 自动回复设定好的内容。

* **添加过滤器**: `/filter "价格" 我们的VIP价格是 10U/月，请联系群主购买。`
    * 当有人发“价格”时，Rose 就会自动回复后面那段话。
* **删除过滤器**: `/stop "价格"`
* **列出所有过滤器**: `/filters`

### 4. 反垃圾与清理 (Anti-spam)
* `/purge`: 回复某条消息并输入此命令，会删除从该条消息起、到底部的所有消息（炸群清理神器）。
* `/del`: 删除回复的那条消息。
* `/ban`: 封禁回复的用户。
* `/mute`: 禁言回复的用户。

## 进阶技巧：锁定群组

晚上睡觉不想让人聊天？或者遇到大规模广告攻击？你可以暂时锁定群组。

* **锁定群组 (全体禁言)**: `/lock all`
* **解锁群组**: `/unlock all`
* **禁止发送链接**: `/lock url` (防止发广告链接)
* **禁止转发**: `/lock forward`

<!-- ![Rose锁定群组权限设置](/assets/images/bot/rose-lock.jpg) -->

::: tip 提示
Rose 默认是英文回复。如果你想让它尽量“中文”一点，虽然它没有官方中文包，但你可以通过自定义欢迎语和过滤器来实现“伪汉化”体验。
:::