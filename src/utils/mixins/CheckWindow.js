const CheckWindow = {
  data: () => {
    return {
      windowWidth: 0
    };
  },
  methods: {
    checkWindow() {
      this.windowWidth = window.innerWidth;
      this.$nextTick(() => {
        window.addEventListener("resize", () => {
          this.windowWidth = window.innerWidth;
        });
      });
    }
  },
  mounted() {
    this.checkWindow();
  }
};
export default CheckWindow;
