import { defineUserConfig } from "vuepress";
import { getDirname, path } from "vuepress/utils";

import theme from "./theme.js";

const __dirname = getDirname(import.meta.url);

export default defineUserConfig({
  base: "/",
  lang: "zh-CN",
  title: 'Telegram电报中文知识库 & 使用指南',
  shouldPrefetch: false,
  description: '电报宝典 | Telegram电报中文知识库 & 使用指南，是一个由 ygjc.cc 打造的高质量 Telegram (电报/纸飞机) 中文知识库。提供从下载安装、账号注册、汉化中文语言包、解除+86私聊限制、收不到验证码解决，到频道群组推荐、机器人开发及会员开通的全方位教程。新手入门 Telegram 的最佳指南。',
  alias: {
    "@theme-hope/components/navbar/NavbarBrand": path.resolve(
      __dirname,
      "./components/NavbarBrand.vue"
    ),
  },
  extendsMarkdown: (md) => {
    // 移除 markdown 正文首个重复的 H1 标题，避免与主题 PageTitle 产生双 H1
    md.core.ruler.push("remove_first_h1", (state) => {
      const tokens = state.tokens;
      let firstHeadingOpenIndex = -1;
      for (let i = 0; i < tokens.length; i++) {
        if (tokens[i].type === "heading_open") {
          firstHeadingOpenIndex = i;
          break;
        }
      }
      if (
        firstHeadingOpenIndex !== -1 &&
        tokens[firstHeadingOpenIndex].tag === "h1"
      ) {
        let closeIndex = firstHeadingOpenIndex;
        while (
          closeIndex < tokens.length &&
          tokens[closeIndex].type !== "heading_close"
        ) {
          closeIndex++;
        }
        tokens.splice(
          firstHeadingOpenIndex,
          closeIndex - firstHeadingOpenIndex + 1
        );
      }
    });
  },
  head: [
    ['link', { rel: 'icon', href: '/assets/logo.png' }],
    ['script', { async: true, src: 'https://telegram.org/js/telegram-web-app.js' }],

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
    // Google Analytics (gtag.js)
    ['script', { async: true, src: 'https://www.googletagmanager.com/gtag/js?id=G-B7D68BX58B' }],
    [
      'script',
      {},
      `window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-B7D68BX58B');`
    ],
  ],
  theme,
});
