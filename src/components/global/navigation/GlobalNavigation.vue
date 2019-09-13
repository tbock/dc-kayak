<template>
  <header>
    <div class="container ">
      <div class="row nav-wrapper">
        <main-logo />
    <!-- <nav>
      <router-link v-for="(item, index) in navItems" :key="index" :to="item.path">{{ item.title }}</router-link>
    </nav>-->
    <at-menu mode="horizontal">
      <at-menu-item name="1">
        <i class="icon icon-activity"></i>River Flows
      </at-menu-item>
      <at-menu-item name="4">
        <i class="icon icon-map"></i>Playspots Map
      </at-menu-item>
      <at-menu-item name="4">
        <i class="icon icon-thumbs-up"></i>Support
      </at-menu-item>
    </at-menu>
      </div>
    </div>
  </header>
</template>
<script>
import MainLogo from "./components/MainLogo";
export default {
  name: "GlobalNavigation",
  components: {
    "main-logo": MainLogo
  },
  data: () => {
    return {
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
  }
};
</script>
<style lang="scss" scoped>
header {
  width: 100vw;
  border-bottom:1px solid #e2ecf4;
  .nav-wrapper {
    min-height: 50px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  }
}
</style>