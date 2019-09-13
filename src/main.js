import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "./registerServiceWorker";
import AtComponents from 'at-ui';
import 'at-ui-style';
// import 'at-ui-style/src/index.scss'

Vue.use(AtComponents);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
