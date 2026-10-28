<script setup lang="ts">
import { Layout } from "vuepress-theme-hope/client";
import { usePageFrontmatter } from "vuepress/client";
import ArticleTopAd from "../components/ArticleTopAd.vue";

const frontmatter = usePageFrontmatter();
</script>

<template>
  <Layout>
    <!-- 在文章页标题上方放置广告 -->
    <template #pageTop>
      <ArticleTopAd v-if="!frontmatter.home" />
    </template>

    <!-- 通过 contentAfter 插槽在 Markdown 内容末尾添加官方 Telegram 频道与 X (Twitter) 账号 -->
    <template #contentAfter>
      <div v-if="!frontmatter.home" class="article-follow-container">
        <!-- Telegram 官方频道卡片 -->
        <div class="article-follow-box tg-box">
          <div class="follow-content">
            <div class="follow-icon tg-icon">
              <svg viewBox="0 0 24 24" width="22" height="22" fill="currentColor">
                <path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/>
              </svg>
            </div>
            <div class="follow-info">
              <div class="follow-title">加入电报宝典官方频道</div>
              <div class="follow-desc">第一时间获取 Telegram 最新动态、实用技巧、防封指南与福利资源</div>
            </div>
          </div>
          <a
            href="https://t.me/tgbaodian"
            target="_blank"
            rel="noopener noreferrer"
            class="follow-btn tg-btn"
          >
            加入 @tgbaodian
            <svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
              <polyline points="15 3 21 3 21 9"></polyline>
              <line x1="10" y1="14" x2="21" y2="3"></line>
            </svg>
          </a>
        </div>

        <!-- X (Twitter) 账号卡片 -->
        <div class="article-follow-box">
          <div class="follow-content">
            <div class="follow-icon x-icon">
              <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor">
                <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
              </svg>
            </div>
            <div class="follow-info">
              <div class="follow-title">关注官方 X (Twitter)</div>
              <div class="follow-desc">获取 Telegram 实用技巧、最新资讯与玩法指南</div>
            </div>
          </div>
          <a
            href="https://x.com/hasenbalg673018"
            target="_blank"
            rel="noopener noreferrer"
            class="follow-btn x-btn"
          >
            关注 @hasenbalg673018
            <svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
              <polyline points="15 3 21 3 21 9"></polyline>
              <line x1="10" y1="14" x2="21" y2="3"></line>
            </svg>
          </a>
        </div>
      </div>
    </template>
  </Layout>
</template>

<style scoped>
.article-follow-container {
  margin: 2.5rem 0 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 0.875rem;
}

.article-follow-box {
  padding: 1.15rem 1.5rem;
  border-radius: 12px;
  background: var(--vp-c-bg-alt, rgba(0, 0, 0, 0.03));
  border: 1px solid var(--vp-c-border, rgba(0, 0, 0, 0.08));
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
  transition: all 0.25s ease;
}

.article-follow-box.tg-box {
  background: linear-gradient(135deg, rgba(36, 161, 222, 0.08) 0%, rgba(36, 161, 222, 0.02) 100%);
  border-color: rgba(36, 161, 222, 0.22);
}

[data-theme="dark"] .article-follow-box {
  background: rgba(255, 255, 255, 0.04);
  border-color: rgba(255, 255, 255, 0.1);
}

[data-theme="dark"] .article-follow-box.tg-box {
  background: linear-gradient(135deg, rgba(36, 161, 222, 0.14) 0%, rgba(36, 161, 222, 0.04) 100%);
  border-color: rgba(36, 161, 222, 0.3);
}

.article-follow-box:hover {
  border-color: var(--vp-c-accent-hover, #3eaf7c);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
}

.article-follow-box.tg-box:hover {
  border-color: #24a1de;
  box-shadow: 0 4px 16px rgba(36, 161, 222, 0.12);
}

.follow-content {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.follow-icon {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.tg-icon {
  background: #24a1de;
  color: #fff;
}

.x-icon {
  background: #000;
  color: #fff;
}

[data-theme="dark"] .x-icon {
  background: #fff;
  color: #000;
}

.follow-title {
  font-size: 1rem;
  font-weight: 600;
  color: var(--vp-c-text, #2c3e50);
  margin-bottom: 0.25rem;
}

.follow-desc {
  font-size: 0.875rem;
  color: var(--vp-c-text-muted, #6a737d);
}

.follow-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.6rem 1.2rem;
  font-size: 0.9rem;
  font-weight: 600;
  border-radius: 9999px;
  text-decoration: none !important;
  transition: all 0.2s ease;
  white-space: nowrap;
}

.tg-btn {
  color: #fff !important;
  background: #24a1de;
}

.tg-btn:hover {
  background: #1b8ec7;
  transform: translateY(-1px);
  box-shadow: 0 2px 10px rgba(36, 161, 222, 0.35);
}

.x-btn {
  color: #fff !important;
  background: #0f1419;
}

[data-theme="dark"] .x-btn {
  background: #eff3f4;
  color: #0f1419 !important;
}

.x-btn:hover {
  opacity: 0.9;
  transform: translateY(-1px);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}

@media (max-width: 600px) {
  .article-follow-box {
    flex-direction: column;
    align-items: flex-start;
  }
  .follow-btn {
    width: 100%;
    justify-content: center;
  }
}
</style>
