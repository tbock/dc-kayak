<template>
  <div class="home">
    <h1>HOME</h1>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Home",
  data: () => {
    return {
      errors: {}
    };
  },
  methods: {
    async loadRivers() {
      await axios
        .get("https://cors-anywhere.herokuapp.com/http://dckayak.herokuapp.com/api/flows/?format=json")
        .then(resp => {
          this.$store.dispatch("setRivers", resp.data);
          this.$Notify({
            title: 'Data Loaded',
            type: "success",
            duration: 5000
          });
        })
        .catch(err => {
          this.errors = err;
          this.$Notify({
            title: err.name,
            message: err.message,
            type: "error",
            duration: 10000
          });
        });
    }
  },
  computed: {
    rivers() {
      return this.$store.state.rivers;
    }
  },
  created() {
    this.loadRivers();
  }
};
</script>
