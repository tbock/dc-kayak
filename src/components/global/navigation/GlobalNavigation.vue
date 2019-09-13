<template>
  <header>
    <span>DC KAYAK</span>
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
  </header>
</template>
<script>
export default {
  name: "GlobalNavigation",
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
  min-height: 50px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 2rem;
  nav {
    a {
      margin-left: 1rem;
    }
  }
}
</style>