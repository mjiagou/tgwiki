import { hopeTheme } from "vuepress-theme-hope";

import navbar from "./navbar.js";
import sidebar from "./sidebar.js";

export default hopeTheme({
  hostname: "https://tg.ygjc.cc",
  author: {
    name: "TGwiki",
    url: "https://x.com/hasenbalg673018",
  },
  logo: "/assets/icon/logo.svg",
  logoDark: "/assets/icon/logo2.svg",
  repo: "mjiagou/tgwiki",
  docsDir: "src",
  copyright: false,
  breadcrumb: false,
  editLink: false,
  navbar,   // 导航栏
  sidebar,  // 侧边栏
  footer: "Copyright © 2025 <a href='https://github.com/mjiagou/tgwiki' target='_blank'>TGwiki</a> | Powered by <a href='https://ygjc.cc/' target='_blank'>ygjc.cc</a>",  // 页脚
  displayFooter: true,
  fullscreen: true,
  // 加密配置
  // encrypt: {
  //   config: {
  //     "/demo/encrypt.html": ["1234"],
  //   },
  // },
  // 多语言配置
  metaLocales: {
    editLink: "编辑此页",
  },
  // 此处开启了很多功能用于演示，你应仅保留用到的功能。
    markdown: {
      align: true,
      attrs: true,
      codeTabs: true,
      component: true,
      demo: false,
      figure: true,
      footnote: true,
      imgLazyload: true,
      imgSize: true,
      include: false,
      linkify: true,
      mark: true,
      plantuml: false,
      spoiler: true,
      stylize: [
        {
          matcher: "Recommended",
          replacer: ({ tag }) => {
            if (tag === "em")
              return {
                tag: "Badge",
                attrs: { type: "tip" },
                content: "Recommended",
              };
          },
        },
      ],
      sub: true,
      sup: true,
      tabs: true,
      tasklist: true,
      vPre: false,

      // 在启用之前安装 chart.js
      chartjs: true,

      // insert component easily

      // 在启用之前安装 echarts
      // echarts: true,

      // 在启用之前安装 flowchart.ts
      // flowchart: true,

      // gfm requires mathjax-full to provide tex support
      // gfm: true,

      math: {
        type: "katex", // 或 'mathjax'
      },

      // 在启用之前安装 mermaid
      // mermaid: true,

      // playground: {
      //   presets: ["ts", "vue"],
      // },

      // 在启用之前安装 reveal.js
      // revealJs: {
      //   plugins: ["highlight", "math", "search", "notes", "zoom"],
      // },

      // 在启用之前安装 @vue/repl
      // vuePlayground: true,

      // install sandpack-vue3 before enabling it
      // sandpack: true,
    },

  // 如果想要实时查看任何改变，启用它。注: 这对更新性能有很大负面影响
  // hotReload: true,
  // 在这里配置主题提供的插件
  plugins: {
    // 注意: 仅用于测试! 你必须自行生成并在生产环境中使用自己的评论服务
    // comment: {
    //   provider: "Giscus",
    //   repo: "vuepress-theme-hope/giscus-discussions",
    //   repoId: "R_kgDOG_Pt2A",
    //   category: "Announcements",
    //   categoryId: "DIC_kwDOG_Pt2M4COD69",
    // },
    components: {
      components: ["Badge"],
    },
    icon: {
      assets: "fontawesome-with-brands",
    },
    // SEO 与 结构化数据优化
    seo: {
      canonical: "https://tg.ygjc.cc",
      fallBackImage: "https://tg.ygjc.cc/assets/og-image.png",
      twitterID: "hasenbalg673018",
      ogp: (ogp) => {
        ogp["og:site_name"] = "电报宝典 | Telegram电报中文知识库";
        return ogp;
      },
      jsonLd: (jsonLD, page) => {
        if (jsonLD["@type"] === "Article") {
          jsonLD.publisher = {
            "@type": "Organization",
            name: "电报宝典 | TGwiki",
            url: "https://tg.ygjc.cc",
            logo: {
              "@type": "ImageObject",
              url: "https://tg.ygjc.cc/assets/logo.png",
            },
          };
          jsonLD.mainEntityOfPage = {
            "@type": "WebPage",
            "@id": `https://tg.ygjc.cc${page.path}`,
          };
        }
        return jsonLD;
      },
    },
    // Sitemap 站点地图优化
    sitemap: {
      changefreq: "weekly",
      excludePaths: ["/404.html"],
    },


    // 如果你需要 PWA。安装 @vuepress/plugin-pwa 并取消下方注释
    pwa: {
      favicon: "/favicon.ico",
      cacheHTML: true,
      cacheImage: true,
      appendBase: true,
      apple: {
        icon: "/assets/icon/apple-icon-152.png",
        statusBarColor: "black",
      },
      manifest: {
        icons: [
          {
            src: "/assets/icon/chrome-mask-512.png",
            sizes: "512x512",
            purpose: "maskable",
            type: "image/png",
          },
          {
            src: "/assets/icon/chrome-mask-192.png",
            sizes: "192x192",
            purpose: "maskable",
            type: "image/png",
          },
          {
            src: "/assets/icon/chrome-512.png",
            sizes: "512x512",
            type: "image/png",
          },
          {
            src: "/assets/icon/chrome-192.png",
            sizes: "192x192",
            type: "image/png",
          },
        ],
        shortcuts: [
          {
            name: "TGwiki - Telegram知识库",
            short_name: "TGwiki",
            url: "/",
            icons: [
              {
                src: "/assets/icon/chrome-mask-192.png",
                sizes: "192x192",
                purpose: "maskable",
                type: "image/png",
              },
            ],
          },
        ],
      },
    },
    docsearch: {
      appId: 'FLBJDNSJ4H',
      apiKey: 'f0fde104fdda0ec7d000a2b7e2234200',
      indexName: 'tgwiki_tgwiki',
      locales: {
        '/': {
          placeholder: '搜索文档',
          maxResultsPerGroup: 20,
          translations: {
            button: {
              buttonText: '搜索文档',
              buttonAriaLabel: '搜索文档',
            },
            modal: {
              searchBox: {
                resetButtonTitle: '清除查询条件',
                resetButtonAriaLabel: '清除查询条件',
                cancelButtonText: '取消',
                cancelButtonAriaLabel: '取消',
              },
              startScreen: {
                recentSearchesTitle: '搜索历史',
                noRecentSearchesText: '没有搜索历史',
                saveRecentSearchButtonTitle: '保存至搜索历史',
                removeRecentSearchButtonTitle: '从搜索历史中移除',
                favoriteSearchesTitle: '收藏',
                removeFavoriteSearchButtonTitle: '从收藏中移除',
              },
              errorScreen: {
                titleText: '无法获取结果',
                helpText: '你可能需要检查你的网络连接',
              },
              footer: {
                selectText: '选择',
                navigateText: '切换',
                closeText: '关闭',
                searchByText: '搜索提供者',
              },
              noResultsScreen: {
                noResultsText: '无法找到相关结果',
                suggestedQueryText: '你可以尝试查询',
                reportMissingResultsText: '你认为该查询应该有结果？',
                reportMissingResultsLinkText: '点击反馈',
              },
            },
          },
        },
      },
    },
  },
},{ custom: true },);
