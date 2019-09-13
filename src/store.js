import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    rivers: []
  },
  mutations: {
    SET_RIVERS(state, data) {
      state.rivers = data;
    }
  },
  actions: {
    setRivers(context, data) {
      context.commit("SET_RIVERS", data);
    }
  }
});
