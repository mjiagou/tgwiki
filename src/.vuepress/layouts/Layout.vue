<script setup lang="ts">
import { Layout } from "vuepress-theme-hope/client";
import { usePageFrontmatter } from "vuepress/client";

const frontmatter = usePageFrontmatter();
</script>

<template>
  <Layout>
    <!-- 通过 contentAfter 插槽在 Markdown 内容末尾添加 X (Twitter) 账号 -->
    <template #contentAfter>
      <div v-if="!frontmatter.home" class="article-x-follow-box">
        <div class="x-follow-content">
          <div class="x-follow-icon">
            <svg viewBox="0 0 24 24" width="22" height="22" fill="currentColor">
              <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
            </svg>
          </div>
          <div class="x-follow-info">
            <div class="x-follow-title">关注官方 X (Twitter)</div>
            <div class="x-follow-desc">获取 Telegram 实用技巧、最新资讯与玩法指南</div>
          </div>
        </div>
        <a
          href="https://x.com/hasenbalg673018"
          target="_blank"
          rel="noopener noreferrer"
          class="x-follow-btn"
        >
          关注 @hasenbalg673018
          <svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
            <polyline points="15 3 21 3 21 9"></polyline>
            <line x1="10" y1="14" x2="21" y2="3"></line>
          </svg>
        </a>
      </div>
    </template>
  </Layout>
</template>

<style scoped>
.article-x-follow-box {
  margin: 2.5rem 0 1.5rem;
  padding: 1.25rem 1.5rem;
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

[data-theme="dark"] .article-x-follow-box {
  background: rgba(255, 255, 255, 0.04);
  border-color: rgba(255, 255, 255, 0.1);
}

.article-x-follow-box:hover {
  border-color: var(--vp-c-accent-hover, #3eaf7c);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
}

.x-follow-content {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.x-follow-icon {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: #000;
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

[data-theme="dark"] .x-follow-icon {
  background: #fff;
  color: #000;
}

.x-follow-title {
  font-size: 1rem;
  font-weight: 600;
  color: var(--vp-c-text, #2c3e50);
  margin-bottom: 0.25rem;
}

.x-follow-desc {
  font-size: 0.875rem;
  color: var(--vp-c-text-muted, #6a737d);
}

.x-follow-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.6rem 1.2rem;
  font-size: 0.9rem;
  font-weight: 600;
  color: #fff !important;
  background: #0f1419;
  border-radius: 9999px;
  text-decoration: none !important;
  transition: all 0.2s ease;
  white-space: nowrap;
}

[data-theme="dark"] .x-follow-btn {
  background: #eff3f4;
  color: #0f1419 !important;
}

.x-follow-btn:hover {
  opacity: 0.9;
  transform: translateY(-1px);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}

@media (max-width: 600px) {
  .article-x-follow-box {
    flex-direction: column;
    align-items: flex-start;
  }
  .x-follow-btn {
    width: 100%;
    justify-content: center;
  }
}
</style>
