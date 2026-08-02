---
title: Telegram 主题美化与自定义完全指南：创建专属主题、聊天背景与夜间模式
shortTitle: 主题美化进阶
description: Telegram 官方内置主题不够用？本文详解桌面端/移动端主题创建与颜色参数、自定义聊天背景（图片/图案/纯色）、夜间模式与护眼模式、主题导入导出与分享链接、热门主题站与配色方案推荐。
icon: palette
category:
  - 进阶教程
tag:
  - 主题
  - 美化
  - 自定义
  - 夜间模式
  - 背景
head:
  - - meta
    - name: keywords
      content: Telegram主题美化,Telegram自定义主题,Telegram创建主题,Telegram聊天背景,Telegram夜间模式,Telegram护眼模式,Telegram主题分享,Telegram主题参数,电报主题,电报自定义主题,电报美化,TG主题
---

# Telegram 主题美化与自定义完全指南：创建专属主题、聊天背景与夜间模式

嫌 Telegram 官方的几个默认主题太单调？想让自己的客户端配色更有个性？

Telegram 拥有聊天软件中**最强大的主题引擎**，你可以自定义几乎每一个界面元素的颜色和样式，制作出独一无二的专属主题。本文从客户端基础美化到主题文件的深入定制，手把手带你打造高颜值 Telegram 客户端。

::: tip 前置阅读
如果你只想快速切换主题，请先阅读 [主题设置基础教程](./theme.html)。
:::

---

## 一、主题系统全览

### 1.1 四种美化层级

| 层级 | 修改范围 | 难度 | 效果 |
|:---|:---|:---:|:---|
| **1. 切换预设主题** | 换色、换背景 | ⭐ | 快速换肤 |
| **2. 自定义聊天背景** | 单聊/群聊背景图 | ⭐⭐ | 个性化聊天窗口 |
| **3. 调整颜色参数** | 修改指定元素颜色 | ⭐⭐⭐ | 深度定制 |
| **4. 编写主题文件** | 所有元素完全可控 | ⭐⭐⭐⭐ | 发布分享级主题 |

### 1.2 主题格式差异

| 客户端 | 主题格式 | 编辑方式 | 平台 |
|:---|:---|:---|:---|
| **Telegram Desktop** | `.tdesktop-theme` / `.tdf` | 内置编辑器 / 文件 | Windows/macOS/Linux |
| **Telegram Android** | `.attheme` | 内置编辑器 / 代码编辑 | Android |
| **Telegram for macOS** | `.tdesktop-theme` | 导入文件，不能直接编辑 | macOS App Store |
| **Telegram iOS** | 无独立格式 | 内置编辑器 + 同步色板 | iOS |
| **第三方客户端** | 各自扩展 | 参考各客户端文档 | Nagram / 64Gram 等 |

### 1.3 官方预设主题快速切换

所有客户端都内置了以下主题：

- 🌙 **Dark Blue（深蓝黑）**：官方夜间模式
- 🌑 **Dark（炭黑）**：纯黑主题（OLED 屏省电）
- 🌳 **Classic（经典蓝）**：传统 Telegram 蓝
- ☁️ **Light Day（日间白）**：默认浅色
- 🌸 **Arctic（北极）**：清爽浅灰蓝
- 🌿 **Matrix（黑客绿）**：荧光绿主题

**快速切换：** `设置 → 外观 → 选择主题`

---

## 二、桌面端（Telegram Desktop）深度自定义

### 2.1 内置主题编辑器

Telegram 桌面端内置了强大的主题编辑器，可以可视化调整颜色：

**打开编辑器：** `设置 → 外观 → 选择当前主题右侧「…」 → 「编辑当前主题」`

编辑器中可以修改以下 5 大类颜色：

| 分类 | 包含元素 | 示例 |
|:---|:---|:---|
| **背景色** | 主背景、聊天列表背景、输入框背景 | 夜间模式改成纯黑 `#000000` |
| **主色/强调色** | 按钮、选中项、气泡箭头、链接 | 默认蓝 `#2AABEE` 可改为紫/粉 |
| **文字颜色** | 主文字、次文字、链接文字、标签文字 | 保证对比度 ≥ 4.5:1 |
| **消息气泡** | 自己气泡、对方气泡、回复气泡、引用气泡 | 左右气泡不同色更有层次 |
| **分隔/阴影** | 分隔线、卡片阴影、菜单阴影 | 扁平化风格可以把阴影设为透明 |

::: tip 💡 技巧
点击任意颜色选择框 → 「切换到输入」→ 可以直接输入 **HEX 颜色值**（如 `#FF0096`），实现精确配色。
:::

### 2.2 重要颜色参数速查

以下是 Telegram Desktop 主题的**高频修改参数**，也是 `.tdesktop-theme` 文件中的 key：

| 参数名 | 说明 | 推荐参考色（深色） |
|:---|:---|:---|
| `windowBg` | 主窗口背景 | `#101010` |
| `windowBgRipple` | 点击涟漪效果 | `#ffffff18` |
| `windowFg` | 主文字颜色 | `#ffffff` |
| `windowSubTextFg` | 次级文字（时间/预览） | `#ffffff80` |
| `chatBg` | 聊天区背景 | `#17212B`（深蓝灰） |
| `msgFileBg` | 自己的消息气泡 | `#2B5278`（Telegram蓝） |
| `msgFileBgHover` | 气泡悬停色 | 在 msgFileBg 上加亮 10% |
| `msgFileShadowFg` | 气泡阴影 | `#00000030` |
| `historyPeer1UserpicBg` | 头像渐变1 | `#FF5B37` 橙红 |
| `historyPeer2UserpicBg` | 头像渐变2 | `#FFB037` 橙黄 |
| `historyPeer3UserpicBg` | 头像渐变3 | `#40BD40` 绿 |
| `historyPeer4UserpicBg` | 头像渐变4 | `#4FADE8` 浅蓝 |
| `historyPeer5UserpicBg` | 头像渐变5 | `#8A77FF` 紫 |
| `historyPeer6UserpicBg` | 头像渐变6 | `#FF3674` 粉 |
| `historyPeer7UserpicBg` | 头像渐变7 | `#FF5B37` 循环 |
| `historyPeer8UserpicBg` | 头像渐变8 | `#FFB037` 循环 |
| `medialoaderThumbnailBg` | 媒体缩略图背景 | `#222` |
| `serviceBg` | 系统消息气泡（入群提示等） | `#00000040`（半透明黑） |
| `linkFg` | 链接文字颜色 | `#6ABDFF` |
| `botKbBg` | 机器人按钮背景 | 建议与 msgFileBg 一致 |
| `sendBg` | 发送按钮背景 | `#2AABEE` |

### 2.3 手动修改主题文件

`.tdesktop-theme` 文件本质上是一个 `zip` 压缩包，包含：
- `colors.tdesktop-theme`（颜色定义，JSON 格式）
- `background.pattern` 或 `background.jpg`（可选：内置背景图）

**手动修改流程：**

```bash
# 1. 导出当前主题
# 设置 → 外观 → … → Share theme → 导出文件，得到 my.tdesktop-theme

# 2. 解压
mkdir extracted-theme
cd extracted-theme
unzip ../my.tdesktop-theme
# 解压后得到 colors.tdesktop-theme 和背景文件

# 3. 编辑颜色文件
vim colors.tdesktop-theme
# （其实就是 JSON，按照上一节的参数名修改颜色值）

# 4. 重新打包
zip -r ../my-custom.tdesktop-theme *

# 5. 导入到 Telegram
# 双击 .tdesktop-theme 文件，或发送到 Telegram 任意对话 → 点击应用
```

**示例 colors.tdesktop-theme：**

```json
{
  "background": "#17212b",
  "windowBg": "#0f1318",
  "windowFg": "#ffffff",
  "windowSubTextFg": "#ffffff80",
  "chatBg": {
    "paper": "#17212b"
  },
  "msgFileBg": "#19364f",
  "msgFileBgSelected": "#1e4263",
  "serviceBg": "#00000040",
  "linkFg": "#6abdff",
  "sendBg": "#2aabee",
  "historyPeer1UserpicBg": "#ff5b37",
  "historyPeer2UserpicBg": "#ffb037"
}
```

### 2.4 制作主题包（可分享）

制作好的主题可以导出为分享链接或文件：

1. `设置 → 外观 → 当前主题右侧「…」 → Share theme`
2. 选择 **Create link** → 生成 `t.me/addtheme/xxx` 链接（推荐）
3. 或选择 **Export file** → 导出 `.tdesktop-theme` 文件

**链接方式更方便**：接收方在 Telegram 内点击链接即可一键安装。

---

## 三、移动端（Android/iOS）深度自定义

### 3.1 Android 端 `.attheme` 文件

Android 端的主题文件是 `.attheme` 格式，**纯文本格式**，可以用任意文本编辑器打开。

**格式示例：**

```
// 以 // 开头的行是注释
windowBackground=#FF0F0F0F
actionBarDefault=#FF121212
actionBarDefaultTitle=#FFFFFFFF
actionBarDefaultSubtitle=#B3FFFFFF
chat_wallpaper=#00000000          // 00 开头 = 透明，使用自定义壁纸
chat_wallpaper_2=#00000000
chat_in=#FF182533                   // 对方气泡
chat_inSelector=#FF203040
chat_out=#FF2B5278                  // 自己气泡
chat_outSelector=#FF355f8a
chat_inBubbleSelected=#FF2a3f55
chat_outBubbleSelected=#FF375f8c
profile_messageLinkOut=#FF6ABDFF    // 链接颜色
highlightColor=#FF4081C0            // 选中文字高亮
chat_nameColor=#CCFFFFFF            // 聊天昵称颜色
divider=#1FFFFFFF                   // 分隔线（8位AARRGGBB）
```

::: tip 🎨 Android 颜色格式
`.attheme` 使用 **AARRGGBB** 格式（8位十六进制）：
- 前2位 = Alpha 透明度（`FF` = 不透明，`00` = 完全透明）
- 后6位 = RGB 颜色值
- 例：`#80FF0000` = 50% 透明度的纯红色
:::

### 3.2 Android 端内置编辑器

1. `设置 → 外观 → 主题 → 点击当前主题右侧的「编辑」`
2. 每种颜色都可以长按查看参数名，双击修改
3. 修改后点击「三点 → 保存 → 分享主题」生成分享链接

### 3.3 iOS 端颜色同步

iOS 端虽然没有独立的主题文件，但支持**颜色编辑器**：

1. `设置 → 外观 → 主题 → 编辑`
2. 长按任意界面元素（如消息气泡）弹出拾色器
3. 支持导入桌面端的 HEX 颜色
4. iOS 支持「跟随系统」的**自动深色模式**：设置 → 外观 → 自动切换

---

## 四、聊天背景高级技巧

### 4.1 背景类型对比

| 背景类型 | 效果 | 适合 |
|:---|:---|:---|
| **纯色** | 无图案，只有颜色 | 极简风格 / 省电 |
| **渐变图案（Pattern）** | 官方内置的 repeating 花纹 | 轻量、不干扰文字 |
| **自定义图片** | 上传任意照片 / 壁纸 | 个性化展示 |
| **渐变混合** | 图片 + 颜色渐变叠加 | 降低背景干扰 |
| **模糊** | 高斯模糊处理 | 让图片更有层次 |

### 4.2 设置全局聊天背景

**桌面端：** `设置 → 外观 → 聊天背景 → 从文件选择 / 选颜色 / 选图案`

**移动端：** `设置 → 外观 → 聊天背景 → 从相册上传 / 选颜色 / 选图案`

::: tip 全局 vs 单聊
- **全局背景**：在设置中修改，所有聊天默认使用
- **单聊/群聊自定义背景**：打开对话 → 点击对方头像 → 更多 → 设置聊天背景
:::

### 4.3 背景图片最佳尺寸

| 设备 | 推荐分辨率 | 说明 |
|:---|:---|:---|
| 手机竖屏 | `1080 × 1920` 或 `1440 × 2560` | 9:16 比例，200KB 以内最佳 |
| 桌面宽屏 | `1920 × 1080` 或 `2560 × 1440` | 16:9 比例，支持平铺（Tiled） |
| 适配所有端 | `2560 × 2560` 正方形 | 居中裁剪，通用但文件大 |

::: warning 文件大小
背景图片超过 2MB 时，Telegram 会自动强压缩导致画质糊。建议控制在 **500KB - 1MB**，优先使用 **WebP / JPEG 格式**（WebP 更小且画质更好）。
:::

### 4.4 图片处理脚本（Python 批量）

```python
"""
批量将图片处理为 Telegram 聊天背景
输出：1080x1920 居中裁剪 + WebP 压缩 75%
依赖：pip install Pillow
"""
import os
from PIL import Image

def process_wallpaper(input_path, output_path, size=(1080, 1920), quality=75):
    img = Image.open(input_path).convert("RGB")
    src_ratio = img.width / img.height
    dst_ratio = size[0] / size[1]

    # 按比例裁剪居中
    if src_ratio > dst_ratio:
        # 图片更宽 → 裁剪两边
        new_w = int(img.height * dst_ratio)
        left = (img.width - new_w) // 2
        img = img.crop((left, 0, left + new_w, img.height))
    else:
        # 图片更高 → 裁剪上下
        new_h = int(img.width / dst_ratio)
        top = (img.height - new_h) // 2
        img = img.crop((0, top, img.width, top + new_h))

    img = img.resize(size, Image.LANCZOS)
    img.save(output_path, "WEBP", quality=quality, method=6)
    size_kb = os.path.getsize(output_path) / 1024
    print(f"✅ {os.path.basename(input_path)} → {os.path.basename(output_path)} ({size_kb:.0f}KB)")

# 批量处理
src_dir = "./wallpapers-in"
out_dir = "./wallpapers-out"
os.makedirs(out_dir, exist_ok=True)

for fn in sorted(os.listdir(src_dir)):
    if fn.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
        process_wallpaper(
            os.path.join(src_dir, fn),
            os.path.join(out_dir, os.path.splitext(fn)[0] + ".webp")
        )
```

### 4.5 Telegram Pattern 生成器（Pattern）

如果不喜欢图片，可以使用 Telegram 的「Pattern」图案背景。

**使用方法：**
1. 选择纯色背景后，点击「图案（Pattern）」
2. 选择花纹类型（点阵 / 网格 / 条纹 / 曲线 / 斜纹）
3. 调整亮度、大小、对比度

**Pattern 适合场景：**
- ✅ 不想让图片抢了文字的注意力
- ✅ 想要品牌感（如公司配色 + 点阵图案）
- ✅ 夜间模式下更柔和的视觉层次

---

## 五、夜间模式与护眼方案

### 5.1 三种夜间模式对比

| 模式 | 背景色 | 省电（OLED） | 护眼 | 适合 |
|:---|:---|:---:|:---:|:---|
| **深蓝（Dark Blue）** | `#17212B` | ⭐⭐ | ⭐⭐⭐⭐ | 通用、官方推荐 |
| **炭黑（Charcoal）** | `#101010` | ⭐⭐⭐ | ⭐⭐⭐ | 看久了有点闷 |
| **纯黑（True Black / AMOLED）** | `#000000` | ⭐⭐⭐⭐⭐ | ⭐⭐ | OLED 手机 / 超省电 |

### 5.2 自制 AMOLED 纯黑主题

OLED 屏幕显示纯黑像素是不发光的，极致省电。手动把桌面主题的关键色改成：

```json
{
  "windowBg": "#000000",
  "chatBg": { "paper": "#000000" },
  "serviceBg": "#00000080",
  "msgFileBg": "#111111",
  "windowFg": "#e8e8e8",
  "windowSubTextFg": "#808080"
}
```

**⚠️ 注意事项：**
- 纯黑主题容易让**分隔线和轮廓消失**，请适当调高头像阴影和气泡的颜色对比
- 消息气泡建议用 `#111` ~ `#1a1a1a` 的深灰，而不是纯黑，否则会分不清气泡和背景

### 5.3 护眼暖色（低蓝光）主题

长时间看屏幕建议用暖色调主题，降低蓝光。配色参考：

```json
{
  "windowBg": "#1A1512",
  "chatBg": { "paper": "#221B15" },
  "windowFg": "#F5E6D3",
  "msgFileBg": "#3D2B1F",
  "linkFg": "#E8985E",
  "sendBg": "#C47A3E"
}
```

特点：底色偏棕色/琥珀色，文字偏米白，长时间阅读比冷色更柔和。

### 5.4 跟随系统自动切换

**iOS / Android 12+ 系统级深色模式：**
1. `设置 → 外观 → 主题`
2. 开启「自动切换深色」
3. 选择触发条件：跟随系统 / 日落到日出 / 自定义时段

---

## 六、头像与用户名颜色

### 6.1 颜色轮循机制

Telegram 会给**每个用户/群组/频道**自动分配一个头像渐变底色，用于在没有设置头像时显示首字母头像。

这个颜色分配是**按 ID 轮循** 8 种默认色，顺序固定：

```
1. #FF5B37 橙红  2. #FFB037 橙黄  3. #40BD40 绿  4. #4FADE8 浅蓝
5. #8A77FF 紫    6. #FF3674 粉    7. 循环到1    8. 循环到2
```

**颜色规则：**
- 同一 ID 在任何设备上显示的颜色**永远一致**（因为是 ID 取模）
- 用户改头像不会改变颜色分配
- Premium 会员可以在设置中**锁定**自己的用户名颜色

### 6.2 第三方客户端颜色增强

在 **Nagram** / **64Gram** / **Cherrygram** 等第三方客户端中，还可以：
- 把自己的名字颜色改成**任意自定义色**
- 给不同群组设置不同的名字色
- 给指定用户的消息加高亮背景色（方便追踪重要发言）

---

## 七、主题分享与导入

### 7.1 三种分享方式

| 方式 | 生成方式 | 接收方使用 |
|:---|:---|:---|
| **addtheme 链接** | 设置 → 外观 → … → Share theme → Create link | 点击链接一键安装 |
| **主题文件** | 设置 → 外观 → … → Export file | 发送文件 → 打开 → 应用 |
| **主题包 Bot** | [@themeBot](https://t.me/themeBot) / [@ThemerBot](https://t.me/ThemerBot) | Bot 内生成主题 |

### 7.2 导入主题

**从文件导入：**
1. 把 `.tdesktop-theme`（桌面）或 `.attheme`（Android）发送到任意对话
2. 点击文件 Telegram 会自动预览
3. 点击「应用主题」即可

**从链接导入：**
1. 点击 `t.me/addtheme/xxxx` 链接
2. 打开后点击「安装」

---

## 八、热门主题站与资源

### 8.1 官方主题社区

| 名称 | 链接 | 说明 |
|:---|:---|:---|
| **Themes Channel** | [@themes](https://t.me/themes) | 官方桌面端主题频道 |
| **Android Themes** | [@AndroidThemes](https://t.me/AndroidThemes) | 官方 Android 主题频道 |
| **iOS Themes** | [@IOSTelegramThemes](https://t.me/IOSTelegramThemes) | iOS 主题分享频道 |
| **Desktop Themes** | [@TelegramThemes](https://t.me/TelegramThemes) | 社区桌面主题 |
| **Theme Chat** | [@AndroidThemesGroup](https://t.me/AndroidThemesGroup) | 制作与讨论群组 |

### 8.2 第三方主题制作工具

| 工具 | 平台 | 功能 |
|:---|:---|:---|
| **[Attheme Editor](https://github.com/Satarus/attheme-editor)** | Web 在线 | `.attheme` 在线编辑器 |
| **[Telegram Theme Builder](https://tgb.wxzg.org/)** | Web 在线 | 桌面/安卓双端主题生成 |
| **[Theme Creator Bot](https://t.me/themeBot)** | Bot | 用 Bot 命令行创建主题 |
| **64Gram 自带编辑器** | 桌面端 | 点按钮即可导出所有颜色 JSON |
| **Figma Telegram Kit** | Figma | 用 Figma 设计稿 → 导出主题 |

### 8.3 推荐色板与配色工具

**色板网站（直接复制 HEX 用）：**
- [Coolors.co](https://coolors.co/) —— 随机生成 5 色搭配
- [ColorHunt.co](https://colorhunt.co/) —— 精选 4 色调色板
- [Realtime Colors](https://www.realtimecolors.com/) —— 实时预览 UI 配色
- [Material Design Color Tool](https://material.io/resources/color) —— 合规对比度计算

**常见好看的强调色搭配：**

| 风格 | 强调色（自己气泡/按钮） | 背景色（聊天区） | 文字色 |
|:---|:---|:---|:---|
| 💜 极光紫 | `#8A77FF` | `#1A1830` | `#EDEAFB` |
| 🌸 樱粉 | `#FF3674` | `#201820` | `#FFE4EC` |
| 🌿 森绿 | `#4CAF50` | `#102018` | `#D4E5D4` |
| 🌊 海洋蓝 | `#2AABEE` | `#0F2030` | `#E0F0FF` |
| 🍊 柑橘橙 | `#FF7A00` | `#1F1510` | `#FFE8D4` |
| 🖤 极简黑 | `#FFFFFF` | `#000000` | `#EEEEEE` |

**🪄 快速配色公式（不会出错）：**

```
背景色 = HSL(220, 20%, 8%)  ← 偏冷的深灰（220度是蓝色调）
自己气泡 = 背景色 明度 +30%, 饱和度 +20%
对方气泡 = 背景色 明度 +10%
文字色 = 白/灰，透明度 85%（主） 45%（副）
```

---

## 九、常见问题排查

### 9.1 导入主题后字看不清？

→ 颜色对比度不足。用 [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) 检查文字与背景的对比度，**≥ 4.5:1 才符合 WCAG 标准**。

### 9.2 图片背景上传后变糊？

→ 文件太大被 Telegram 二次压缩。处理方法：
1. 上传前先压缩到 500KB - 1MB
2. 发送图片时选择「发送为文件」而不是「发送为图片」
3. 使用 WebP 格式比 JPEG 画质更好

### 9.3 主题分享链接失效？

→ 链接失效通常是因为：
1. 作者在 Bot 里撤销了分享（用 `/reset` 可以恢复）
2. 主题属于旧版格式（客户端版本不兼容）
3. 在旧版客户端创建的主题，新版 Telegram 对部分参数进行了重命名

### 9.4 聊天背景为什么变灰色了？

→ 可能是手机开启了**系统级夜间模式**的「降低白点值」或**灰阶模式**。关闭后即可正常显示颜色。

### 9.5 为什么我设置的颜色在图片气泡中不生效？

→ 带图片/视频的媒体消息气泡默认有一层模糊遮罩，颜色会被半透明覆盖，这是**设计如此**。如果要完全控制，可以把背景模糊值调低或使用纯色背景。

---

## 十、主题设计最佳实践

### 10.1 设计原则

1. **对比度优先**：文字与背景对比度 ≥ 4.5:1，否则字会糊
2. **气泡层次**：自己的气泡比对方的更亮/更饱和，视觉上区分"我说的"和"别人说的"
3. **强调色克制**：强调色只用在按钮、链接、选中项，大面积使用会刺眼
4. **系统消息要弱化**：入群提示、时间戳使用半透明色，不要抢主消息的注意力
5. **头像颜色统一**：8 种头像底色尽量在同一色相范围（比如都是暖色系），视觉更统一

### 10.2 常见误区

| ❌ 错误做法 | ✅ 正确做法 |
|:---|:---|
| 纯黑背景 + 纯白文字（刺眼） | 深灰 `#111` + 米白 `#eee` |
| 粉色强调色放在浅粉背景（分不清） | 强调色与背景明度差 ≥ 40% |
| 聊天区背景用花哨图片（字看不清） | 背景图加深色遮罩（半透明黑） |
| 所有元素都改颜色（混乱） | 保持 80% 默认，只改 20% 核心色 |
| 链接色和普通文字颜色一致 | 链接色要明显更亮/更饱和 |

### 10.3 检查清单

- [ ] 主文字对比度 ≥ 4.5:1
- [ ] 次级文字对比度 ≥ 3:1
- [ ] 左右气泡可一眼区分
- [ ] 链接颜色明显可识别
- [ ] 系统消息（时间戳/入群提示）不突兀
- [ ] 头像 8 种颜色之间辨识度足够
- [ ] 深色和浅色两个版本都能正常使用（可选）

---

## 总结

本文覆盖了 Telegram 主题美化的从入门到发布：

| 主题 | 核心知识点 |
|:---|:---|
| 桌面端自定义 | 参数速查、`.tdesktop-theme` 解压修改 |
| 移动端自定义 | `.attheme` 8 位 AARRGGBB 格式 |
| 聊天背景 | 尺寸规范、Python 批量处理脚本、Pattern 图案 |
| 夜间/护眼 | AMOLED 纯黑、暖色调色板、自动切换方案 |
| 分享导入 | 链接 / 文件 / Bot 三种方式 |
| 资源工具 | 主题站、配色网站、在线编辑器 |

**上手路径建议：**

1. **新手**：先从修改官方主题的 2-3 个颜色开始（强调色、聊天背景、自己气泡色）
2. **进阶**：解压导出的主题文件，修改参数表中的高频颜色
3. **高级**：使用在线编辑器制作完整主题，并发布分享链接给朋友使用

Telegram 的主题引擎自由度非常高，只要花一点时间调配，就能得到真正属于自己的高颜值聊天界面。

---

**相关阅读：**

- [主题基础教程](./theme.md) — 快速切换主题的入门篇
- [Premium 会员详解](./premium.md) — Premium 专属的动态头像与名字颜色
- [第三方客户端](./thirdparty.md) — 更多主题自定义能力的客户端
- [Nagram 客户端](./nagram.md) — Android 最强美化型第三方客户端
- [聊天分组与文件夹](./folder.md) — 配合主题提升效率