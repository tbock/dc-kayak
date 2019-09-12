<template>
  <div>
    <global-navigation />
    <router-view></router-view>
  </div>
</template>
<script>
import GlobalNavigation from './components/global/navigation/GlobalNavigation.vue';
export default {
  name: "App",
  components: {
      "global-navigation":GlobalNavigation
  }
};
</script>