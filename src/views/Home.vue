<template>
  <div class="container">
    <div class="row">
      <div class="col">
        <template v-if="rivers.length > 0">
          <at-table :columns="columns" :data="rivers"></at-table>
        </template>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Home",
  data: () => {
    return {
      errors: {},
      columns: [
        {
          title: "Name",
          key: "name"
        },
        {
          title: "Flow Rate",
          key: "flow-rate",
          sortType: "normal"
        },
        {
          title: "Class",
          key: "grade"
        }
      ]
    };
  },
  methods: {
    async loadRivers() {
      await axios
        .get(
          "https://cors-anywhere.herokuapp.com/http://dckayak.herokuapp.com/api/flows/?format=json"
        )
        .then(resp => {
          this.$store.dispatch("setRivers", resp.data);
          this.$Notify({
            title: "Data Loaded",
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
