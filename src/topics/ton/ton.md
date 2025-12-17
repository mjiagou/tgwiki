---
title: TON链新手入门：Tonkeeper去中心化钱包使用指南与安全避坑
shortTitle: Tonkeeper教程
description: 不想用官方托管钱包？本文详解最受欢迎的去中心化钱包 Tonkeeper 的安装与创建流程，助记词安全保存方法，以及它与内置钱包的区别。
icon: shield-cat
order: 2
category:
  - 科普知识
tag:
  - TON
  - Tonkeeper
  - 去中心化
---

# TON链新手入门：Tonkeeper去中心化钱包使用指南与安全避坑

## 为什么需要 Tonkeeper？

虽然 Telegram 内置钱包很方便，但它是一个**中心化钱包**。如果你追求绝对的资产控制权，或者想玩 TON 生态的小游戏、DeFi、购买 NFT，你需要一个**非托管钱包**。

**Tonkeeper** 是目前 TON 生态体验最好、用户最多的去中心化钱包。
* **私钥自持**：只有你拥有助记词，官方也无法动用你的资产。
* **生态入口**：可以直接连接 Fragment 购买匿名账号，连接 STON.fi 进行交易。

<!-- ![Tonkeeper钱包主界面](/assets/images/ton/tonkeeper-home.jpg) -->

## 下载与安装

* **iOS**: App Store 搜索 "Tonkeeper"
* **Android**: Google Play 搜索 "Tonkeeper"
* **官网下载**: [tonkeeper.com](https://tonkeeper.com/) (⚠️ 请务必通过官网跳转，防止下载到假冒App)

## 创建钱包与安全备份 (生命线)

1.  打开 App，选择 **Create new wallet** (创建新钱包)。
2.  App 会生成 **24 个英文单词**。这就是你的**助记词 (Seed Phrase)**。

<!-- ![Tonkeeper创建钱包与助记词备份页面](/assets/images/ton/tonkeeper-seed.jpg) -->

::: danger 🚨 绝对安全警示
**1. 永远不要截图！** 手机相册可能会被恶意 App 读取。
**2. 永远不要复制到剪贴板！** 剪贴板会被输入法或流氓软件监控。
**3. 永远不要发给任何人！** 客服、群管如果问你要助记词，**100% 是骗子**。
**4. 正确做法**：拿纸和笔，按顺序抄写在纸上，藏在保险柜或书里。
:::

3.  App 会要求你按顺序验证几个单词，以确保你抄写正确。
4.  设置一个 4 位数 PIN 码，开启 FaceID。恭喜，你的去中心化钱包创建成功了！

## 如何连接 Telegram 游戏和小程序

很多 Telegram 小游戏（如 Notcoin, Hamster Kombat）领空投时，都需要连接钱包。

1.  打开游戏机器人，点击 **Connect Wallet**。
2.  在弹出的选项中选择 **Tonkeeper**。
3.  系统会自动唤起 Tonkeeper App。
4.  核对请求内容，点击 **Connect Wallet** 确认。
5.  **注意**：仅仅是“连接”操作是不需要输入密码或支付费用的。如果连接时要求你支付 TON，请立刻拒绝！

<!-- ![连接Tonkeeper钱包授权界面](/assets/images/ton/tonkeeper-connect.jpg) -->

## 内置钱包 vs Tonkeeper 对比

| 特性 | 内置 Wallet (@wallet) | Tonkeeper |
| :--- | :--- | :--- |
| **类型** | 托管 (像银行账户) | 非托管 (像现金钱包) |
| **安全性** | 账号被封则资产冻结 | 只要助记词在，资产永远在 |
| **使用场景** | 发红包、P2P买币 | 玩游戏、买NFT、DeFi |
| **KYC** | 需要实名 | **不需要实名** |
| **防丢币** | 充值需要 Memo | 充值一般不需要 Memo |