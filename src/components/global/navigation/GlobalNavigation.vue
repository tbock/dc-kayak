<template>
  <header>
    <div :class="[windowWidth > breakpoints.md ? 'container' : '']">
      <div class="row nav-wrapper">
        <main-logo />
        <!-- <nav>
      <router-link v-for="(item, index) in navItems" :key="index" :to="item.path">{{ item.title }}</router-link>
        </nav>-->
        <at-menu :mode="nav" :theme="theme">
          <at-menu-item name="1">
            <i class="icon icon-activity"></i>River Flows
          </at-menu-item>
          <at-menu-item name="2">
            <i class="icon icon-map"></i>Playspots Map
          </at-menu-item>
          <at-menu-item name="3">
            <i class="icon icon-thumbs-up"></i>Support
          </at-menu-item>
        </at-menu>
      </div>
    </div>
  </header>
</template>
<script>
import MainLogo from "./components/MainLogo";
import CheckWindow from "@/utils/mixins/CheckWindow";
import Breakpoints from "@/utils/Breakpoints.js";
export default {
  name: "GlobalNavigation",
  mixins: [CheckWindow],
  components: {
    "main-logo": MainLogo
  },
  data: () => {
    return {
      breakpoints: Breakpoints,
      navItems: [
        {
          path: "/",
          title: "home"
        },
        {
          path: "/",
          title: "link"
        },
        {
          path: "/",
          title: "link"
        }
      ]
    };
  },
  computed: {
    nav() {
      if (this.windowWidth > this.breakpoints.md) {
        return "horizontal";
      } else {
        return "vertical";
      }
    },
    theme() {
      if (this.windowWidth > this.breakpoints.md) {
        return "light";
      } else {
        return "dark";
      }
    }
  }
};
</script>
<style lang="scss" scoped>
header {
  width: 100vw;
  border-bottom: 1px solid #e2ecf4;
  .nav-wrapper {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
}
</style>
