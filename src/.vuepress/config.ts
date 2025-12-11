import { defineUserConfig } from "vuepress";

import theme from "./theme.js";

export default defineUserConfig({
  base: "/",
  lang: "zh-CN",
  title: '电报宝典 | Telegram电报中文知识库 & 使用指南',
  shouldPrefetch: false,
  description: '电报宝典 | Telegram电报中文知识库 & 使用指南，是一个由 ygjc.cc 打造的高质量 Telegram (电报/纸飞机) 中文知识库。提供从下载安装、账号注册、汉化中文语言包、解除+86私聊限制、收不到验证码解决，到频道群组推荐、机器人开发及会员开通的全方位教程。新手入门 Telegram 的最佳指南。',
  head: [
    ['meta', { name: 'image', content: '/assets/tgwiki.png' }],
    ['link', { rel: 'icon', href: '/assets/logo.png' }],
    ['script', {async: true, src: 'https://telegram.org/js/telegram-web-app.js' }],
    ['meta', { name: 'keywords', content: 'Telegram, 电报, 纸飞机, TG, Telegram中文, Telegram汉化, Telegram下载, Telegram注册, 收不到验证码, 解除双向限制, +86限制, Telegram群组, Telegram频道, Telegram机器人, TGwiki, 隐私设置, 电报会员' }],
    ['meta', { property: 'og:site_name', content: '电报宝典 | Telegram电报中文知识库' }],
    ['meta', { property: 'og:title', content: '电报宝典 | Telegram电报中文知识库 & 使用指南' }],
    ['meta', { property: 'og:description', content: '小白也能看懂的 Telegram 电报全方位指南，解决汉化、注册、解封等所有难题。' }],
    ['meta', { property: 'og:image', content: '/assets/logo.png' }],
[
  'script', 
  { type: 'text/javascript' }, 
  `try {
    const urlParams = new URLSearchParams(window.location.search);
    const pathParam = urlParams.get('tgWebAppStartParam');
    if (pathParam) {
      // 1. 解码参数
      const path = window.atob(pathParam);

      // 2. 安全验证：确保不包含协议头(http/s)、不包含双斜杠(//)、不包含上级目录跳转(..)
      // 如果检测到恶意特征，则不执行跳转
      if (!/^(http|https|javascript):|\/\/|\.\./i.test(path)) {
        
        // 3. 格式规范：确保路径以 / 开头
        const finalPath = path.startsWith('/') ? path : '/' + path;
        
        // 4. 执行站内跳转
        window.location.href = window.location.origin + finalPath;
      }
    }
  } catch (e) {
    // 捕获解码错误，静默失败，不影响网站正常访问
    console.debug('TG WebApp params parse failed');
  }`
],
[
      'script',
      {
        async: true,
        src: 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1683234937128959',
        crossorigin: 'anonymous'
      }
    ],
  ],
  theme,
});
