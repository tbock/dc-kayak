<template>
  <header>
    <span>DC KAYAK</span>
    <nav>
      <router-link v-for="(item, index) in navItems" :key="index" :to="item.path">{{ item.title }}</router-link>
    </nav>
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
  height: 50px;
  background-color: #ccc;
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