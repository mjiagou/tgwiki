import { defineUserConfig } from "vuepress";

import theme from "./theme.js";

export default defineUserConfig({
  base: "/",
  lang: "zh-CN",
  title: '一个机场玩转Telegram教程知识库',
  shouldPrefetch: false,
  description: 'TGwiki (Telegram Wiki) - Telegram知识库，由TGNAV打造的高质量Telegram知识库，汇集了Telegram常用功能介绍和使用说明，帮助用户更全面地了解Telegram的各种功能。',
  head: [
    ['meta', { name: 'image', content: '/assets/tgwiki.png' }],
    ['link', { rel: 'icon', href: '/assets/logo.png' }],
    ['script', {async: true, src: 'https://telegram.org/js/telegram-web-app.js' }],
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
