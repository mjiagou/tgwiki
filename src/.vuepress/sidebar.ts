import { sidebar } from "vuepress-theme-hope";

export default sidebar({
  "/": [
    // --- 1. 新增：热门专题 (使用 structure 自动读取子文件夹内容) ---
    {
      text: "热门专题",
      icon: "fire",
      prefix: "topics/",
      collapsible: true,
      children: [
        {
          text: "TON 生态与钱包",
          icon: "wallet",
          prefix: "ton/",
          children: "structure", // 自动读取 topics/ton/ 下的文章
        },
        {
          text: "群管机器人",
          icon: "robot",
          prefix: "bot/",
          children: "structure", // 自动读取 topics/bot/ 下的文章
        },
        {
          text: "小程序与游戏",
          icon: "gamepad",
          prefix: "game/",
          children: "structure", // 自动读取 topics/game/ 下的文章
        },
        {
          text: "资源寻找与下载",
          icon: "magnifying-glass",
          prefix: "resource/",
          children: "structure", // 自动读取 topics/resource/ 下的文章
        },
      ],
    },
    
    // --- 2. 原有：电报入门 ---
    {
      text: "电报入门",
      icon: "rocket",
      collapsible: true,
      children: [
        { text: "文档指南", icon: "lightbulb", link: "guide.md" },
        { text: "名词解释", icon: "info-circle", link: "term.md" },
        { text: "中文语言包", icon: "language", link: "language.md" },
        { text: "谨防诈骗", icon: "shield-cat", link: "scam.md" },
        { text: "Telegram限制", icon: "ruler-combined", link: "limit.md" },
        { text: "数据中心DC", icon: "server", link: "dc.md" },
      ],
    },

    // --- 3. 原有：基础操作 ---
    {
      text: "基础操作",
      icon: "star",
      collapsible: true,
      children: [
        { text: "消息格式", icon: "paragraph", link: "format.md" },
        { text: "图片排版", icon: "image", link: "editphoto.md" },
        { text: "内置搜索", icon: "magnifying-glass", link: "search.md" },
        { text: "创建贴纸", icon: "face-smile", link: "createsticker.md" },
        { text: "创建机器人", icon: "robot", link: "createrobot.md" },
        { text: "内置浏览器", icon: "compass", link: "browser.md" },
      ],
    },

    // --- 4. 原有：进阶/高级功能 ---
    {
      text: "进阶玩法",
      icon: "wand-magic-sparkles",
      collapsible: true,
      children: [
        { text: "Premium会员", icon: "gem", link: "premium.md" },
        { text: "Telegraph文章", icon: "pen-nib", link: "telegraph.md" },
        { text: "私聊机器人", icon: "headset", link: "livegram.md" },
        { text: "频道/群组助推", icon: "rocket", link: "boost.md" },
        { text: "频道开启评论", icon: "comments", link: "comment.md" },
        { text: "第三方客户端", icon: "mobile-screen", link: "thirdparty.md" },
      ],
    },

    // --- 5. 原有：账号与安全 ---
    {
      text: "账号与安全",
      icon: "user-shield",
      collapsible: true,
      children: [
        { text: "隐私设置", icon: "shield-halved", link: "privacy.md" },
        { text: "缓存与下载", icon: "broom", link: "download.md" },
        { text: "邮箱登录", icon: "envelope", link: "emaillogin.md" },
        { text: "收不到验证码", icon: "comment-slash", link: "notcomesms.md" },
        { text: "账号申诉/解封", icon: "ban", link: "banned.md" },
        { text: "解除私聊限制", icon: "user-slash", link: "spam.md" },
        { text: "解除敏感限制", icon: "eye-slash", link: "pornios.md" },
        { text: "联系官方", icon: "address-card", link: "contact.md" },
      ],
    },
  ],
});