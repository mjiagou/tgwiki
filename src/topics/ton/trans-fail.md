---
title: Telegram转账USDT没到账？忘记填Memo/Tag的找回方法
shortTitle: 转账没到账
description: 往交易所充值TON或USDT忘记填Memo/Tag导致丢币怎么办？本文提供各大交易所（币安/欧易/Gate）的资产找回申诉流程，挽回你的损失。
icon: circle-exclamation
order: 3
category:
  - 常见问题
tag:
  - 转账
  - 故障排除
---

# Telegram转账USDT没到账？忘记填Memo/Tag的找回方法

## 为什么转账 TON 需要填 Memo/Tag？

很多新手在从交易所（如欧易 OKX、币安）提现 TON 或 USDT-TON 到 **交易所** 或 **Telegram 内置钱包** 时，因为忘记填写 **Memo (或称为 Tag / Comment / 备注)**，导致币没有到账。

**原理通俗解释：**
* **地址 (Address)** 就像是“大楼的地址”。交易所的 TON 钱包是一个公共大账户。
* **Memo (Tag)** 就像是“房间号”。

如果你只填了地址没填 Memo，快递员（区块链）就把包裹扔到了大楼大堂，交易所不知道这个包裹具体是给哪个用户的，所以无法入账。

<!-- ![交易所充值页面提示需要填写Tag/Memo](/assets/images/ton/exchange-memo-warning.jpg) -->

::: tip 只有去中心化钱包不需要 Memo
如果你是提现到 **Tonkeeper** 这种去中心化钱包，通常只需要地址，不需要 Memo（除非特定说明）。但充值到 **Telegram 内置钱包** 必须填！
:::

## 忘记填了怎么办？(补救措施)

**不要慌！币通常没有丢，只是卡在交易所的公账上了。** 你需要向收款方（交易所或钱包客服）发起申诉。

### 情况一：充值到 Telegram 内置钱包 (@wallet) 没填 Memo

1.  打开 @wallet 机器人。
2.  点击 **Settings** (设置) -> **Support** (支持)。
3.  告诉客服：“I deposited funds but forgot the Comment/Memo.”
4.  准备好以下证据：
    * **TxID (Hash)**：转账哈希值（在提币平台找）。
    * **截图**：提币成功的界面截图。
5.  官方客服核实后，通常会将币原路退回到你的付款账户。

<!-- ![联系Wallet官方客服支持](/assets/images/ton/wallet-support.jpg) -->

### 情况二：充值到 欧易 OKX / 币安 没填 Memo

各大交易所都有自助找回通道：

#### 🔴 欧易 (OKX) 找回流程
1.  打开 OKX App。
2.  点击左上角九个点 -> **帮助中心**。
3.  搜索“**充值未到账**”。
4.  选择“充值未到账自查” -> 选择币种 (TON/USDT) -> 填入哈希值 (TxID)。
5.  如果系统识别到是 Tag 缺失，会要求你提供“原路退回地址”或进行“补充入账”。

<!-- ![欧易OKX充值未到账自助申诉入口](/assets/images/ton/okx-recovery.jpg) -->

#### 🟡 币安 (Binance) 找回流程
1.  访问 [币安充值状态查询页面](https://www.binance.com/zh-CN/my/wallet/recovery/form/d).
2.  申请类型选择：**标签/Memo填错或未填**。
3.  提交 TxID 和发送方地址。
4.  **注意**：找回资产通常需要支付少量的手续费（如 5 USDT），且处理时间可能需要 3-7 个工作日。

## 如何避免再次出错？

1.  **开启白名单**：在交易所提币地址簿中，将常用的地址保存，并连同 Memo 一起保存。
2.  **小额测试**：第一次向新地址转账，先转 1 USDT 测试，确认到账后再转大额。
3.  **看清提示**：所有交易所提币页面，如果有 Memo 框，通常会有红字提示“如果不填可能导致资产丢失”。