<template>
  <main>
    <template v-if="rivers.length !== 0">
      <div v-for="(river, index) in rivers" class="river" :key="index">
        <span>{{ river.name }}</span>
        <span>Flow Rate: {{ river.latest_flow }}</span>
      </div>
    </template>
    <template v-else>
      <p>something went wrong.</p>
    </template>
  </main>
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
        .get("http://dckayak.herokuapp.com/api/flows/?format=json")
        .then(resp => {
          this.$store.dispatch("setRivers", resp.data);
        })
        .catch(err => {
          this.errors = err;
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

<style lang="scss" scoped>
main {
  width: 80vw;
  margin: 0 auto;
}
.river {
  align-items: center;
  cursor: pointer;
  width: 100%;
  height: 75px;
  display: flex;
  justify-content: space-evenly;
  padding: 0 2rem;
  margin-bottom: 0.5rem;
  border-bottom: 1px solid #fefefe;

  &:hover {
    box-shadow: 0px 4px 8px 0px rgba(#ccc, 0.75);
  }
}
</style>