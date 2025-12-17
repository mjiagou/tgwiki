---
title: Telegram内置钱包(@Wallet)保姆级教程：激活、KYC认证与USDT充提全攻略
shortTitle: 官方钱包教程
description: Telegram可以直接转账USDT了！本文手把手教你如何开通官方内置钱包@Wallet，完成KYC实名认证，以及从欧易/币安交易所充值USDT到电报钱包的详细步骤。
icon: wallet
order: 1
category:
  - 进阶教程
tag:
  - 钱包
  - USDT
  - 支付
---

# Telegram内置钱包(@Wallet)保姆级教程：激活、KYC认证与USDT充提全攻略

## 什么是 Telegram 内置钱包 (@Wallet)？

Telegram 内置钱包（官方名称为 **Wallet**）是一个托管式的加密货币钱包，它作为一个机器人集成在 Telegram 应用中。

**它的核心优势是：**
* **零门槛**：不需要下载额外的 App，像发微信红包一样发送 USDT。
* **免手续费**：Telegram 好友之间转账 USDT **完全免费**。
* **法币购买**：支持使用银行卡或 P2P 市场（类似闲鱼）购买 USDT 和 TON。

::: warning 风险提示
@Wallet 是**托管钱包**（Custodial Wallet），这意味着私钥由官方保管，类似你在交易所的账户。如果你的 Telegram 账号被封禁，钱包资产可能面临风险。**大额资产建议存放在冷钱包或 Tonkeeper 中。**
:::

<!-- ![Telegram内置钱包界面概览](/assets/images/ton/wallet-home.jpg) -->

## 第一步：如何激活钱包

如果你在 Telegram 的侧边栏菜单中没有看到“Wallet”选项，请按照以下步骤激活：

1.  在 Telegram 顶部搜索栏输入 `@wallet`。
2.  点击带有蓝色验证对勾 ✅ 的机器人。
3.  点击底部的 **Start** 或 **开始**。
4.  点击 **Open Wallet**。
5.  按照提示同意服务条款，你的钱包就激活成功了！现在它会永久出现在你的侧边栏菜单中。

<!-- ![如何搜索并激活Wallet机器人](/assets/images/ton/wallet-activate.jpg) -->

## 第二步：KYC 身份认证流程

为了防止洗钱，使用 P2P 交易或大额充值需要完成 KYC（实名认证）。

1.  打开 Wallet，点击右上角的设置齿轮图标。
2.  选择 **Identification Levels** (认证等级)。
3.  **基础认证 (Basic)**：
    * 需要提供：手机号 + 出生日期。
    * 限制：每日限额较低，无法使用 P2P 卖币。
4.  **进阶认证 (Extended)**：
    * 需要提供：**身份证/护照/驾照** 的照片 + **人脸扫描**。
    * **建议**：推荐使用护照（Passport）通过率最高。如果只有身份证，请确保光线充足，文字清晰。
    * 审核时间：通常在 15 分钟到 24 小时内完成。

<!-- ![KYC身份认证等级选择界面](/assets/images/ton/wallet-kyc.jpg) -->

## 第三步：如何充值 USDT (重要！)

这是新手最容易出错的地方。向 Telegram 钱包充值 USDT 有两种网络通道，请务必分清！

### 通道 A：使用 TON 网络 (推荐 🔥)
这是最便宜、最快的方式。

1.  在 Wallet 点击 **Deposit** (充值) -> **USDT**。
2.  选择网络为 **TON**。
3.  复制显示的 **Address (地址)**。
4.  **⚠️ 关键点**：如果从交易所（如欧易 OKX / 币安 Binance）提币，**一定要填写 Comment / Memo / Tag！**
    * Wallet 页面会显示一串数字 Comment。
    * 在交易所提币时，将这串数字填入 "备注/Memo" 栏。
    * **不填 Memo 币会丢失！**

<!-- ![充值TON网络USDT显示的Memo备注](/assets/images/ton/wallet-deposit-ton.jpg) -->

### 通道 B：使用 TRC20 网络
1.  在 Wallet 点击 **Deposit** -> **USDT**。
2.  选择网络为 **TRX (TRC20)**。
3.  此方式**不需要 Memo**，直接复制地址即可。
4.  **缺点**：交易所提币手续费较高（通常 1 USDT），到账速度稍慢。

<!-- ![充值TRC20网络USDT界面](/assets/images/ton/wallet-deposit-trc20.jpg) -->

## 常见问题 (FAQ)

**Q: 给好友转账需要手续费吗？**
A: 不需要。在 Telegram 对话框中，点击附件图标（回形针）-> Wallet -> 发送 USDT 给联系人，是**0手续费**且即时到账的。

**Q: 为什么我的钱包被限制了？**
A: 通常是因为触发了风控（如频繁 P2P 交易或资金来源可疑）。请联系 Wallet 内置的客服支持。

**Q: 内置钱包安全吗？**
A: 相对安全，但不如 Tonkeeper (去中心化钱包) 隐私。建议将其作为“零钱袋”，随用随充。