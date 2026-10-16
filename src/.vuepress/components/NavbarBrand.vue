<script setup lang="ts">
import { computed } from "vue";
import { RouteLink, withBase } from "vuepress/client";
import { useData } from "vuepress-theme-hope/client";

import "vuepress-theme-hope/styles/navbar/navbar-brand.scss";

const { routeLocale, siteLocale, themeLocale } = useData();

const siteBrandLink = computed(
  () => themeLocale.value.home ?? routeLocale.value,
);

const siteTitle = computed(() => siteLocale.value.title);
const siteBrandTitle = computed(
  () => themeLocale.value.navbarTitle ?? siteTitle.value ?? "电报宝典",
);

const siteBrandLogo = computed(() =>
  themeLocale.value.logo ? withBase(themeLocale.value.logo) : null,
);

const siteBrandLogoDark = computed(() =>
  themeLocale.value.logoDark ? withBase(themeLocale.value.logoDark) : null,
);
</script>

<template>
  <RouteLink
    :to="siteBrandLink"
    class="vp-brand"
    :aria-label="themeLocale.routerLocales?.home || '首页'"
  >
    <img
      v-if="siteBrandLogo"
      class="vp-nav-logo"
      :class="{ light: Boolean(siteBrandLogoDark) }"
      :src="siteBrandLogo"
      alt="电报宝典"
    />
    <img
      v-if="siteBrandLogoDark"
      class="vp-nav-logo dark"
      :src="siteBrandLogoDark"
      alt="电报宝典"
    />
    <span
      v-if="siteBrandTitle"
      class="vp-site-name"
      :class="{
        'hide-in-pad':
          siteBrandLogo && (themeLocale.hideSiteNameOnMobile ?? true),
      }"
    >
      {{ siteBrandTitle }}
    </span>
  </RouteLink>
</template>
