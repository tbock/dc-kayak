import Vue from "vue";
import VueRouter from "vue-router";
import routes from "./routes";
import store from "./store";
import App from "./App.vue";
import AtComponents from "at-ui";

import "at-ui-style"; // Import CSS
// NOTE: we'll want to use the unbuilt version eventually
// import 'at-ui-style/src/index.scss'

Vue.use(AtComponents);
Vue.use(VueRouter);

new Vue({
  router: new VueRouter(routes),
  store,
  render: h => h(App)
}).$mount("#app");
