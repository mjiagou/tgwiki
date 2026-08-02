---
title: Telegram 贴纸与表情包进阶指南：动态贴纸、视频贴纸与自定义表情
shortTitle: 贴纸进阶指南
description: 从静态贴纸到动态 Lottie 贴纸、视频贴纸和自定义表情包，全面掌握 Telegram 贴纸制作的进阶技巧，附工具推荐、格式规范和设计最佳实践。
icon: face-grin-stars
category:
  - 进阶教程
tag:
  - 贴纸
  - 表情包
  - 动态贴纸
  - 视频贴纸
  - 自定义表情
head:
  - - meta
    - name: keywords
      content: Telegram动态贴纸,Telegram视频贴纸,Telegram TGS,Telegram WebM贴纸,Telegram自定义表情,Telegram Lottie贴纸,Telegram贴纸制作工具,TG动态贴纸,TG视频贴纸,电报动态贴纸,电报视频贴纸,电报自定义表情
---

# Telegram 贴纸与表情包进阶指南：动态贴纸、视频贴纸与自定义表情

已经会用 [@Stickers](https://t.me/Stickers) 机器人上传静态贴纸了？想制作会动的动态贴纸、视频贴纸和自定义表情包？本文带你进阶掌握 Telegram 贴纸系统的所有高级玩法。

::: tip 前置阅读
如果你还没有制作过静态贴纸，建议先阅读 [贴纸制作基础教程](./createsticker.md)。
:::

---

## 一、Telegram 贴纸体系全览

### 1.1 四种贴纸类型对比

| 类型 | 格式 | 文件大小 | 动画 | 透明背景 | 制作难度 | 适用场景 |
|:---|:---|:---|:---|:---|:---:|:---|
| **静态贴纸** | PNG / WEBP | ≤512 KB | ❌ | ✅ | ⭐ | 简单图案、文字 |
| **动态贴纸 (TGS)** | Lottie JSON → TGS | ≤64 KB | ✅ 矢量动画 | ✅ | ⭐⭐⭐ | 精美矢量动画 |
| **视频贴纸** | WebM (VP9) | ≤256 KB | ✅ 视频动画 | ✅ | ⭐⭐ | GIF 转 视频、实拍 |
| **自定义表情** | 同上三种 | 同上 | 同上 | 同上 | 同上 | 替换系统 emoji |

### 1.2 尺寸规范速查

| 用途 | 尺寸要求 |
|:---|:---|
| **贴纸（静态/动态/视频）** | 一边必须为 512px，另一边 512px 或更小 |
| **自定义表情（静态/动态）** | 必须正好 100×100 px |
| **自定义表情（视频）** | 必须正好 100×100 px |
| **贴纸包图标** | 100×100 px（PNG/WEBP，透明背景） |

### 1.3 @Stickers 机器人命令速查

| 命令 | 功能 |
|:---|:---|
| `/newpack` | 创建静态贴纸包 |
| `/newanimated` | 创建动态贴纸包（TGS） |
| `/newvideo` | 创建视频贴纸包（WebM） |
| `/newemoji` | 创建自定义表情包（Premium 专属） |
| `/editpack` | 编辑贴纸包信息 |
| `/addsticker` | 向已有包添加贴纸 |
| `/delsticker` | 删除贴纸 |
| `/ordersticker` | 调整贴纸顺序 |
| `/setpackicon` | 设置贴纸包图标 |
| `/stats` | 查看贴纸包使用统计 |
| `/cancel` | 取消当前操作 |

---

## 二、动态贴纸（TGS）制作

### 2.1 什么是 TGS 格式

TGS（Telegram Animated Stickers）是基于 **Lottie** 动画框架的矢量动画格式。它的优势是：

- **文件极小**：通常只有 10-60 KB（同等内容 GIF 可能 500KB+）
- **无损缩放**：矢量格式，放大不失真
- **流畅动画**：支持 60fps
- **透明背景**：原生支持透明

### 2.2 用 Adobe After Effects 制作

TGS 贴纸的标准制作流程是 **After Effects → Lottie → TGS**。

**第一步：在 AE 中制作动画**

```
项目设置：
- 合成尺寸：512×512 px
- 帧速率：30 fps 或 60 fps
- 时长：建议 1-3 秒（最长不超过 10 秒）
- 背景透明：关闭背景颜色
```

::: warning 注意事项
Lottie 不支持 AE 的所有功能。以下效果**无法导出**：
- 粒子系统
- 模糊特效（部分支持）
- 渐变描边
- 路径修剪动画（部分支持）

推荐使用：形状图层、路径动画、变换动画、遮罩
:::

**第二步：安装 Bodymovin 插件**

1. 在 AE 中打开 **扩展管理器**，搜索并安装 **Bodymovin**（ZXP Install）
2. 或从 [LottieFiles 官网](https://lottiefiles.com/plugins/after-effects) 下载插件
3. 安装后在 AE 的 **窗口 → 扩展 → Bodymovin** 中打开

**第三步：导出 Lottie JSON**

1. 在 Bodymovin 面板中选择你的合成
2. 设置导出路径
3. **关键设置**：
   - 勾选 `Standard`（标准模式）
   - 勾选 `Glyphs`（包含字体轮廓）
   - 不勾选 `Hidden layers`（排除隐藏图层）
4. 点击 Render 导出 `.json` 文件

**第四步：将 JSON 转为 TGS**

TGS 本质上是 **gzip 压缩的 Lottie JSON 文件**。

```bash
# 使用 gzip 压缩
gzip -c animation.json > sticker.tgs

# 或者使用 Python
import gzip
import shutil

with open("animation.json", "rb") as f_in:
    with gzip.open("sticker.tgs", "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)
```

::: tip 验证 TGS 文件
压缩后的 TGS 文件必须 ≤ 64 KB。如果超限，在 AE 中减少动画复杂度或缩短时长。
:::

**第五步：上传到 Telegram**

1. 在 Telegram 中找到 [@Stickers](https://t.me/Stickers)
2. 发送 `/newanimated`
3. 输入贴纸包名称
4. 发送 `.tgs` 文件（作为文档发送，不要压缩）
5. 发送对应的 emoji 表情
6. 重复以上步骤添加更多贴纸
7. 发送 `/publish` 完成发布

### 2.3 用 LottieFiles 在线制作（免 AE）

如果没有 After Effects，可以使用 [LottieFiles](https://lottiefiles.com/) 平台：

1. **免费动画库**：在 LottieFiles 市场浏览数千个免费 Lottie 动画
2. **在线编辑器**：LottieFiles Editor 可以在线修改动画颜色、速度
3. **Lottie to TGS 转换器**：直接将下载的 JSON 转为 TGS

**操作步骤：**

1. 访问 [LottieFiles.com](https://lottiefiles.com/)，搜索合适的动画
2. 下载 JSON 格式
3. 使用 [Lottie to TGS Converter](https://lottie.github.io/lottie-docs/) 在线转换
4. 或用命令行转换（见上文）
5. 上传到 @Stickers 机器人

### 2.4 动态贴纸设计技巧

| 技巧 | 说明 |
|:---|:---|
| **循环动画** | 首尾帧衔接，实现无缝循环 |
| **简洁配色** | 使用 3-5 种颜色，避免渐变过多 |
| **大轮廓** | 贴纸在小尺寸下需要清晰可辨 |
| **表情夸张** | 动画贴纸的精髓在于夸张的表情和动作 |
| **时长控制** | 1-3 秒最佳，太长会增大文件 |
| **预留边距** | 四周留 10-20px 边距，避免被裁剪 |

---

## 三、视频贴纸（WebM）制作

### 3.1 什么是视频贴纸

视频贴纸使用 **WebM 格式（VP9 编码）**，适合从 GIF、实拍视频或动画渲染转换而来。相比 TGS，它支持更复杂的色彩和效果。

### 3.2 视频贴纸格式规范

| 参数 | 要求 |
|:---|:---|
| **格式** | WebM (VP9 编码) |
| **尺寸** | 一边 512px，另一边 ≤512px |
| **时长** | ≤3 秒（推荐 1-2 秒） |
| **帧率** | ≤30 fps |
| **文件大小** | ≤256 KB |
| **音频** | 必须无音频流 |
| **透明** | 支持 Alpha 通道透明 |

### 3.3 GIF 转视频贴纸

这是最常见的制作方式——把现有 GIF 转为符合规范的 WebM。

**方法一：在线转换（简单）**

1. 访问 [CDKM GIF to WebM](https://cdkm.com/cn/gif-to-webm)
2. 上传 GIF 文件
3. 设置：
   - 视频尺寸：自定义 → `512×512`
   - 编码：VP9
4. 转换并下载

**方法二：FFmpeg 命令行（精确控制）**

```bash
# GIF 转 WebM（带透明通道）
ffmpeg -i input.gif \
  -c:v libvpx-vp9 \
  -pix_fmt yuva420p \
  -b:v 200k \
  -crf 30 \
  -an \
  -s 512x512 \
  -r 30 \
  -t 3 \
  output.webm

# 参数说明：
# -pix_fmt yuva420p  保留 Alpha 透明通道
# -b:v 200k          视频码率
# -crf 30            质量（数字越大文件越小，18-30 推荐）
# -an                去除音频
# -s 512x512         尺寸
# -r 30              帧率
# -t 3               时长 3 秒
```

**方法三：Python 脚本批量转换**

```python
"""
GIF 批量转 WebM 视频贴纸
依赖：pip install Pillow
系统依赖：ffmpeg
"""
import subprocess
import os
from PIL import Image

def gif_to_webm_sticker(gif_path, output_path, max_size=512, duration=3, fps=30):
    """将 GIF 转为 Telegram 视频贴纸"""

    # 获取 GIF 尺寸
    with Image.open(gif_path) as img:
        w, h = img.size

    # 计算缩放尺寸（保持宽高比，最大边 512px）
    if w >= h:
        new_w = max_size
        new_h = int(h * max_size / w)
    else:
        new_h = max_size
        new_w = int(w * max_size / h)

    # FFmpeg 转换
    cmd = [
        "ffmpeg", "-y",
        "-i", gif_path,
        "-c:v", "libvpx-vp9",
        "-pix_fmt", "yuva420p",
        "-b:v", "200k",
        "-crf", "30",
        "-an",
        "-s", f"{new_w}x{new_h}",
        "-r", str(fps),
        "-t", str(duration),
        output_path
    ]
    subprocess.run(cmd, check=True)

    # 检查文件大小
    size = os.path.getsize(output_path)
    if size > 256 * 1024:  # 256 KB
        print(f"⚠️ {output_path} 超过 256KB ({size/1024:.0f}KB)，需要降低质量")
        # 降低码率重新转换
        cmd[cmd.index("200k")] = "100k"
        subprocess.run(cmd, check=True)

    print(f"✅ {gif_path} → {output_path} ({os.path.getsize(output_path)/1024:.0f}KB)")

# 批量转换
gif_dir = "./gifs"
output_dir = "./webm_stickers"
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(gif_dir):
    if filename.endswith(".gif"):
        gif_path = os.path.join(gif_dir, filename)
        output_path = os.path.join(output_dir, filename.replace(".gif", ".webm"))
        try:
            gif_to_webm_sticker(gif_path, output_path)
        except Exception as e:
            print(f"❌ {filename} 转换失败：{e}")
```

### 3.4 视频转贴纸（从视频片段制作）

从 YouTube、B 站等视频截取片段制作贴纸：

```bash
# 从视频中截取 3 秒片段并转为贴纸
ffmpeg -ss 00:01:30 -i input.mp4 \
  -t 3 \
  -c:v libvpx-vp9 \
  -pix_fmt yuva420p \
  -b:v 200k \
  -crf 30 \
  -an \
  -s 512x512 \
  -r 30 \
  -vf "chromakey=0x00FF00:0.3:0.1" \
  output.webm

# chromakey 参数用于绿幕抠像
# 0x00FF00 = 纯绿色，0.3 = 相似度阈值，0.1 = 混合度
```

### 3.5 抠图与透明背景处理

视频贴纸需要透明背景，以下是几种抠图方法：

| 方法 | 工具 | 适合 |
|:---|:---|:---|
| **绿幕抠像** | FFmpeg chromakey | 有绿幕背景的视频 |
| **AI 抠图** | rembg / unscreen.com | 复杂背景的人物/物体 |
| **AE 抠像** | After Effects Roto Brush | 精细抠像 |
| **手动遮罩** | After Effects Mask | 简单形状 |

**使用 rembg AI 抠图：**

```bash
# 安装 rembg
pip install rembg[cli]

# 对视频进行 AI 抠图
rembg p input.mp4 output.mp4

# 然后转为 WebM
ffmpeg -i output.mp4 -c:v libvpx-vp9 -pix_fmt yuva420p ... sticker.webm
```

### 3.6 上传视频贴纸

1. 找到 [@Stickers](https://t.me/Stickers)
2. 发送 `/newvideo`
3. 输入贴纸包名称
4. 发送 `.webm` 文件（作为文档发送）
5. 发送对应的 emoji
6. 重复添加
7. `/publish` 完成

---

## 四、自定义表情包（Custom Emoji）

### 4.1 什么是自定义表情

自定义表情包是 **Telegram Premium** 专属功能。你可以创建自己的表情包，在聊天中替代系统默认 emoji 使用。与普通贴纸不同，自定义表情：

- 尺寸为 **100×100 px**（不是 512×512）
- 在 emoji 面板中显示，而非贴纸面板
- 可以在消息中内联使用
- 需要 Premium 订阅才能显示动画

### 4.2 创建自定义表情包

**静态自定义表情：**

1. 准备 100×100 px 的 PNG/WEBP 图片
2. 在 @Stickers 中发送 `/newemoji`
3. 输入表情包名称
4. 发送图片（作为文档）
5. 发送对应的系统 emoji（用于触发建议）
6. 重复添加
7. `/publish` 完成

**动态自定义表情（TGS）：**

1. 在 AE 中制作 100×100 px 的 Lottie 动画
2. 导出 JSON 并转为 TGS
3. 发送 `/newanimated` → 选择 emoji 模式
4. 上传 TGS 文件

**视频自定义表情（WebM）：**

1. 制作 100×100 px 的 WebM 视频
2. 发送 `/newvideo` → 选择 emoji 模式
3. 上传 WebM 文件

### 4.3 自定义表情使用技巧

- **触发方式**：在消息中输入关联的系统 emoji，会弹出自定义表情建议
- **面板使用**：emoji 面板底部会显示已安装的自定义表情包
- ** Premium 限制**：非 Premium 用户只能看到静态版本
- **群组使用**：所有群成员都能看到，但非 Premium 用户看到的是静态版

---

## 五、贴纸设计工具大全

### 5.1 工具对比表

| 工具 | 平台 | 适合 | 价格 | 难度 |
|:---|:---|:---|:---|:---:|
| **Adobe After Effects** | 桌面 | TGS 动态贴纸 | 付费 | ⭐⭐⭐⭐ |
| **LottieFiles** | 在线 | TGS 动态贴纸 | 免费/付费 | ⭐⭐ |
| **Figma** | 在线 | 静态贴纸设计 | 免费/付费 | ⭐⭐ |
| **Photoshop** | 桌面 | 静态贴纸、批处理 | 付费 | ⭐⭐ |
| **Procreate** | iPad | 手绘贴纸 | 付费 | ⭐⭐ |
| **Stickerify** | iOS/Android | GIF/视频转贴纸 | 免费/付费 | ⭐ |
| **FFmpeg** | 命令行 | 批量转换 | 免费 | ⭐⭐⭐ |
| **AE + LottieFiles 插件** | 桌面 | TGS 一键导出 | 免费 | ⭐⭐⭐ |

### 5.2 Figma 设计贴纸

Figma 是免费且强大的设计工具，非常适合制作静态贴纸：

1. 创建 512×512 px 画板
2. 设计贴纸图案
3. 导出为 PNG（勾选"包含透明背景"）
4. 批量导出多个贴纸

**Figma 贴纸模板技巧：**
- 使用 Components 组件系统管理表情系列
- 使用 Auto Layout 自动排列
- 使用 Variants 管理不同状态

### 5.3 Stickerify 手机 App

[Stickerify](https://stickerify.app/) 是一款手机端贴纸制作工具：

- 支持 GIF → WebM 一键转换
- 自动裁剪和缩放到 512px
- 自动去除背景
- 直接发送到 Telegram

### 5.4 LottieFiles 插件（AE 辅助）

安装 LottieFiles 的 AE 插件后可以：

- **预览 Lottie 动画**：在导出前预览效果
- **一键导出 TGS**：直接导出为 TGS 格式，无需手动 gzip
- **优化文件大小**：自动检测并提示减小文件体积
- **动画库**：直接在 AE 中浏览和导入免费动画

---

## 六、批量制作与管理

### 6.1 批量处理图片脚本

```python
"""
批量处理图片为 Telegram 贴纸格式
依赖：pip install Pillow
"""
import os
from PIL import Image

def process_sticker(input_path, output_path, size=512, max_file_kb=512):
    """处理单张图片为贴纸格式"""
    img = Image.open(input_path).convert("RGBA")

    # 等比缩放，最大边 512px
    w, h = img.size
    if w >= h:
        new_w = size
        new_h = int(h * size / w)
    else:
        new_h = size
        new_w = int(w * size / h)

    img = img.resize((new_w, new_h), Image.LANCZOS)

    # 创建 512×512 透明画布并居中
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    offset = ((size - new_w) // 2, (size - new_h) // 2)
    canvas.paste(img, offset, img)

    # 保存为 WebP
    canvas.save(output_path, "WEBP", quality=90, method=6)

    # 检查文件大小
    file_size = os.path.getsize(output_path) / 1024
    if file_size > max_file_kb:
        # 降低质量重新保存
        quality = 80
        while file_size > max_file_kb and quality > 30:
            canvas.save(output_path, "WEBP", quality=quality, method=6)
            file_size = os.path.getsize(output_path) / 1024
            quality -= 10

    return file_size

# 批量处理
input_dir = "./ originals"
output_dir = "./stickers"
os.makedirs(output_dir, exist_ok=True)

for filename in sorted(os.listdir(input_dir)):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + ".webp")
        size_kb = process_sticker(input_path, output_path)
        print(f"✅ {filename} → {os.path.basename(output_path)} ({size_kb:.0f}KB)")
```

### 6.2 贴纸包管理最佳实践

| 操作 | 命令 | 说明 |
|:---|:---|:---|
| 添加贴纸 | `/addsticker` | 向已有贴纸包添加新贴纸 |
| 删除贴纸 | `/delsticker` | 删除指定贴纸 |
| 调整顺序 | `/ordersticker` | 修改贴纸排列顺序 |
| 修改标题 | `/editpack` → Title | 修改贴纸包名称 |
| 修改图标 | `/setpackicon` | 设置贴纸包图标 |
| 查看统计 | `/stats` | 查看每日使用人数 |
| 设置关联 | `/setsticker` | 设置贴纸的关联 emoji |

### 6.3 贴纸包 SEO 优化

让你的贴纸包更容易被搜索到：

1. **名称优化**：使用关键词，如 "猫咪日常 | Cat Daily Stickers"
2. **名称链接**：设置简短易记的分享链接，如 `t.me/addstickers/CatDaily`
3. **图标设计**：制作辨识度高的 100×100 图标
4. **发布推广**：在频道、群组中分享贴纸包链接

---

## 七、贴纸变现与商业化

### 7.1 免费贴纸包引流

1. 创建高质量免费贴纸包
2. 在贴纸包名称中加入频道链接
3. 用户搜索下载贴纸时自然发现你的频道
4. 通过贴纸包为频道导流

### 7.2 付费定制贴纸

| 服务 | 定价参考 | 说明 |
|:---|:---|:---|
| 静态贴纸包（10 个） | ¥50-200 | 基础图案设计 |
| 动态贴纸包（10 个） | ¥300-800 | AE 动画制作 |
| 视频贴纸包（10 个） | ¥200-500 | GIF 转换 + 抠像 |
| 品牌专属贴纸包 | ¥500-2000 | 企业定制 |

### 7.3 贴纸包推广渠道

- **Telegram 贴纸目录站**：[combot.org/stickers](https://combot.org/stickers)
- **频道推广**：在相关频道投放贴纸包链接
- **社交媒体**：在微博、小红书、Twitter 分享
- **贴纸群组**：加入贴纸分享群组

---

## 八、常见问题排查

### 8.1 上传失败

| 问题 | 原因 | 解决方案 |
|:---|:---|:---|
| 文件太大 | 超过大小限制 | 降低质量/时长/分辨率 |
| 格式不对 | 不是标准格式 | 检查编码（VP9 for WebM） |
| 有音频流 | WebM 包含音频 | FFmpeg 加 `-an` 参数去除 |
| 尺寸不对 | 不是 512px | 重新调整尺寸 |
| TGS 不合法 | JSON 格式错误 | 用 Lottie 验证工具检查 |

### 8.2 动画播放问题

| 问题 | 原因 | 解决方案 |
|:---|:---|:---|
| TGS 显示为静态 | 不支持的 AE 效果 | 简化动画，使用基础效果 |
| 动画卡顿 | 帧率太高或文件太大 | 降低帧率到 30fps，减少时长 |
| 透明背景变黑 | 导出设置错误 | 确保使用 yuva420p 像素格式 |
| 颜色偏差 | 色彩空间问题 | 使用 sRGB 色彩空间 |

### 8.3 FFmpeg 常用修复命令

```bash
# 检查 WebM 文件信息
ffprobe -v error -show_format -show_streams sticker.webm

# 去除音频流
ffmpeg -i input.webm -c copy -an output.webm

# 调整码率减小文件
ffmpeg -i input.webm -c:v libvpx-vp9 -b:v 100k -crf 35 -an output.webm

# 裁剪到 3 秒
ffmpeg -i input.webm -t 3 -c copy output.webm

# 调整尺寸
ffmpeg -i input.webm -vf scale=512:512 -c:v libvpx-vp9 -pix_fmt yuva420p output.webm
```

---

## 九、贴纸设计最佳实践

### 9.1 视觉设计原则

1. **辨识度优先**：在 100×100 px 的小尺寸下依然清晰可辨
2. **轮廓清晰**：使用深色描边或阴影增强可见性
3. **表情夸张**：贴纸的表情和动作比真实更夸张才有效果
4. **色彩饱和**：使用高饱和度颜色，避免灰暗色调
5. **留白适当**：四周留 10-20px 边距，不要占满整个画布
6. **风格统一**：同一贴纸包内的风格保持一致

### 9.2 动画设计原则

1. **快速进入**：前 0.3 秒抓住注意力
2. **循环无缝**：首尾帧自然衔接
3. **节奏明快**：避免缓慢的动画
4. **一次一个焦点**：不要同时有多个动画元素
5. **表情变化**：动画的核心是表情/状态的变化

### 9.3 配色方案推荐

| 风格 | 配色 | 适合 |
|:---|:---|:---|
| **可爱风** | 粉色系 + 白色描边 | 萌宠、日常 |
| **科技风** | 蓝色系 + 渐变 | 科技、极客 |
| **复古风** | 暖黄 + 棕色 | 文艺、怀旧 |
| **极简风** | 黑白 + 一个强调色 | 商务、品牌 |
| **活力风** | 高饱和多色 | 表情、情绪 |

---

## 十、灵感与资源

### 10.1 贴纸灵感来源

- [Telegram Stickers 目录](https://t.me/stickers) — 官方精选
- [Combot Stickers](https://combot.org/stickers) — 热门贴纸排行
- [LottieFiles 社区](https://lottiefiles.com/community) — 动画灵感
- [Dribbble](https://dribbble.com/search/sticker) — 设计灵感
- [Behance](https://www.behance.net/search/sticker) — 专业设计

### 10.2 免费素材

| 资源 | 类型 | 链接 |
|:---|:---|:---|
| LottieFiles | 免费 Lottie 动画 | lottiefiles.com |
| Freepik | 矢量图素材 | freepik.com |
| Unscreen | 在线视频抠图 | unscreen.com |
| remove.bg | 在线图片抠图 | remove.bg |
| SVG Repo | 免费 SVG 图标 | svgrepo.com |

### 10.3 学习资源

- [Lottie 官方文档](https://lottiefiles.github.io/lottie-docs/) — Lottie 动画技术文档
- [AE Lottie 教程](https://lottiefiles.com/blog/working-with-lottie-animations) — 官方制作教程
- [Telegram Stickers API](https://core.telegram.org/stickers) — 官方贴纸规范
- [TGS 验证工具](https://lottie.github.io/lottie-docs/) — 在线验证 TGS 文件

---

## 总结

本文覆盖了 Telegram 贴纸系统的进阶制作：

| 类型 | 核心工具 | 文件限制 | 适合 |
|:---|:---|:---|:---|
| 静态贴纸 | Photoshop / Figma | 512 KB | 入门、简单图案 |
| 动态贴纸 (TGS) | After Effects + Lottie | 64 KB | 精美矢量动画 |
| 视频贴纸 (WebM) | FFmpeg / 在线转换 | 256 KB | GIF 转换、实拍 |
| 自定义表情 | 同上三种 | 同上 | Premium 专属 |

**上手路径建议：**

1. **入门**：先用 Figma 制作静态贴纸包
2. **进阶**：学习 FFmpeg 把 GIF 转为视频贴纸
3. **高级**：学习 After Effects 制作动态贴纸
4. **终极**：创建自定义表情包，打造专属 emoji

贴纸是 Telegram 社交中最有表现力的元素，一套好的贴纸包不仅能提升聊天体验，还能成为频道引流的利器。开始动手制作你的专属贴纸吧！

---

**相关阅读：**

- [贴纸制作基础教程](./createsticker.md) — 静态贴纸上传入门
- [Premium 会员详解](./premium.md) — 自定义表情是 Premium 专属功能
- [频道运营全攻略](./createchannel.md) — 用贴纸包为频道引流
- [引流与推广](./promotion.md) — 贴纸包作为推广工具
- [消息格式](./format.md) — 在消息中使用贴纸和表情