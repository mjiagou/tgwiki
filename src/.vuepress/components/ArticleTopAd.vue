<script setup lang="ts">
import { withBase } from "vuepress/client";

interface AdItem {
  name: string;
  desc: string;
  link: string;
  icon: string;
}

const ads: AdItem[] = [
    {
    name: "极速Cloud",
    desc: "原生住宅宽带 9折: ikds88",
    link: "https://191.101.132.80/#/register?code=OdBrieT3",
    icon: "/logo/logo_png_under.png",
  },
  {
    name: "闪跃机场",
    desc: "全场套餐 8折优惠码: shanyue",
    link: "https://y-m.top/go/shanyue",
    icon: "/logo/lightspeed_logo.webp",
  },
  {
    name: "星岛梦",
    desc: "IEPL高速专线 9折: nmw888",
    link: "https://y-m.top/go/xdm",
    icon: "/logo/xdm_logo.webp",
  },

];
</script>

<template>
  <div class="article-top-ad-container">
    <div class="article-top-ad-grid">
      <a
        v-for="ad in ads"
        :key="ad.name"
        :href="ad.link"
        target="_blank"
        rel="sponsored noreferrer"
        class="article-top-ad-card"
      >
        <div class="ad-card-row">
          <img
            :src="withBase(ad.icon)"
            :alt="ad.name"
            class="ad-card-icon"
            width="32"
            height="32"
            loading="lazy"
          />
          <span class="ad-card-name">{{ ad.name }}</span>
        </div>
        <p class="ad-card-desc">{{ ad.desc }}</p>
      </a>
    </div>
  </div>
</template>

<style scoped>
.article-top-ad-container {
  max-width: var(--content-width);
  margin: 1.75rem auto 1rem;
  padding: 0 2.5rem;
  box-sizing: border-box;
  width: 100%;
}

@media (max-width: 959px) {
  .article-top-ad-container {
    margin: 1.25rem auto 0.75rem;
    padding: 0 1.5rem;
  }
}

.article-top-ad-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.75rem;
}

.article-top-ad-card {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 0.875rem 1rem;
  border-radius: 12px;
  background-color: var(--vp-c-bg-alt, #f6f6f7);
  border: 1px solid var(--vp-c-border, rgba(0, 0, 0, 0.06));
  text-decoration: none !important;
  color: var(--vp-c-text, #2c3e50);
  transition: all 0.25s ease;
  min-width: 0;
}

[data-theme="dark"] .article-top-ad-card {
  background-color: rgba(255, 255, 255, 0.04);
  border-color: rgba(255, 255, 255, 0.08);
}

.article-top-ad-card:hover {
  transform: translateY(-2px);
  border-color: var(--vp-c-accent-hover, #3eaf7c);
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.06);
}

[data-theme="dark"] .article-top-ad-card:hover {
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.25);
  border-color: var(--vp-c-accent-hover, #3eaf7c);
}

.ad-card-row {
  display: flex;
  align-items: center;
  gap: 0.625rem;
  width: 100%;
  min-width: 0;
}

.ad-card-icon {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  flex-shrink: 0;
  object-fit: cover;
}

.ad-card-name {
  font-size: 0.9375rem;
  font-weight: 600;
  color: var(--vp-c-text, #2c3e50);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

[data-theme="dark"] .ad-card-name {
  color: #f3f4f6;
}

.ad-card-desc {
  margin: 0.5rem 0 0 0;
  font-size: 0.775rem;
  font-weight: 400;
  color: var(--vp-c-text-muted, #6a737d);
  line-height: 1.4;
  word-break: break-all;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  width: 100%;
}

[data-theme="dark"] .ad-card-desc {
  color: #9ca3af;
}

@media (max-width: 768px) {
  .article-top-ad-grid {
    grid-template-columns: repeat(1, 1fr);
    gap: 0.5rem;
  }
  
  .article-top-ad-card {
    padding: 0.75rem 0.875rem;
  }
}
</style>
