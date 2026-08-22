import { defineClientConfig } from 'vuepress/client';
import Layout from "./layouts/Layout.vue";
import aiLayout from "./layouts/aiLayout.vue";
import VPCard from "./components/VPCard.vue";

function reloadScript(url: string): void {
  // 确保只在浏览器环境中执行，避免 Node.js (SSR) 报错
  if (typeof document !== 'undefined') {
    // 查找并安全移除所有具有相同 URL 的旧 script 标签
    const existingScripts = document.querySelectorAll(`script[src="${url}"]`);
    existingScripts.forEach((script) => script.remove());

    // 创建并追加新的 script 标签
    const script = document.createElement('script');
    script.src = url;
    script.async = true;

    if (document.body) {
      document.body.appendChild(script);
    }
  }
}

// 定义客户端配置
export default defineClientConfig({
  layouts: {
    Layout,
    aiLayout: aiLayout,
  },
  // enhance 钩子用于增强 Vue 应用实例、路由器等
  enhance({ app, router, siteData }) {
    app.component("VPCard", VPCard);
    // router.beforeEach 钩子在路由切换前触发
    router.beforeEach((to, from) => {
      // 您的 beforeEach 逻辑，通常不涉及 DOM 操作，无需额外判断
      // 如果您的逻辑中确实有涉及 document 的部分，也需要添加 typeof window !== 'undefined'
    });

    // router.afterEach 钩子在路由切换后触发
    router.afterEach(() => {
      // 在这里调用 reloadScript 时，同样需要确保只在浏览器环境中执行
      // 这是因为 afterEach 钩子也可能在 SSR 过程中被调用
      if (typeof window !== 'undefined') {
        // 调用 reloadScript 函数来加载您的脚本
        reloadScript("https://busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js");
        reloadScript("https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8134487633157988");
      }
    });
  },
  // setup 钩子用于定义 Vue 组合式 API 的 setup 逻辑
  setup() {
    // 如果 setup 钩子中包含任何需要访问 DOM 的代码，也应该包裹在条件判断中
    if (typeof window !== 'undefined') {
      // 您的 setup 逻辑，例如初始化客户端特有的库或功能
      // console.log('Client-side setup: document is available');
    }
  },
  // rootComponents 选项用于在 Vue 应用的根组件中注册额外的组件
  rootComponents: [],
});
