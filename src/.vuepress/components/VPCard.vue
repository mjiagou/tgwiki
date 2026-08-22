<script setup lang="ts">
import { computed } from "vue";
import { RouteLink, withBase } from "vuepress/client";

interface Props {
  title: string;
  desc?: string;
  logo?: string;
  icon?: string;
  link?: string;
  background?: string;
  color?: string;
}

const props = withDefaults(defineProps<Props>(), {
  desc: "",
  logo: "",
  icon: "",
  link: "",
  background: "",
  color: "",
});

const isLinkExternal = (url: string): boolean => {
  return /^(https?:|\/\/|mailto:|tel:)/i.test(url);
};

const isImg = computed(() => {
  const target = props.logo || "";
  if (!target) return false;
  return (
    target.startsWith("/") ||
    target.startsWith("./") ||
    target.startsWith("../") ||
    target.startsWith("http://") ||
    target.startsWith("https://") ||
    target.startsWith("data:") ||
    /\.(png|jpg|jpeg|svg|webp|gif|ico)(\?.*)?$/i.test(target)
  );
});

const iconName = computed(() => {
  if (isImg.value) return "";
  return props.icon || props.logo || "";
});

const isExternal = computed(() => {
  return Boolean(props.link && isLinkExternal(props.link));
});

const cardStyle = computed(() => {
  const style: Record<string, string> = {};
  if (props.background) style.background = props.background;
  if (props.color) style.color = props.color;
  return style;
});
</script>

<template>
  <component
    :is="link ? (isExternal ? 'a' : RouteLink) : 'div'"
    :class="['vp-card', { link: Boolean(link) }]"
    :href="isExternal ? link : undefined"
    :to="!isExternal && link ? link : undefined"
    :target="isExternal ? '_blank' : undefined"
    :style="cardStyle"
  >
    <!-- 图片 Logo -->
    <img
      v-if="isImg"
      class="vp-card-logo"
      :src="withBase(logo)"
      loading="lazy"
      no-view
      alt=""
    />
    <!-- 图标 Icon -->
    <div v-else-if="iconName" class="vp-card-icon-wrapper">
      <VPIcon :icon="iconName" class="vp-card-icon-symbol" />
    </div>

    <!-- 卡片主体内容 -->
    <div class="vp-card-content">
      <div class="vp-card-title" v-html="title"></div>
      <hr />
      <div v-if="desc" class="vp-card-desc" v-html="desc"></div>
    </div>
  </component>
</template>

<style scoped>
.vp-card-icon-wrapper {
  width: 3rem;
  height: 3rem;
  margin-inline-end: 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  border-radius: 50%;
  background: rgba(0, 0, 0, 0.05);
  font-size: 1.5rem;
  color: var(--vp-c-accent, #3eaf7c);
  transition: all 0.2s ease;
}

[data-theme="dark"] .vp-card-icon-wrapper {
  background: rgba(255, 255, 255, 0.08);
}

.vp-card:hover .vp-card-icon-wrapper {
  transform: scale(1.08);
}

.vp-card-icon-symbol {
  width: 1.5rem;
  height: 1.5rem;
}
</style>
