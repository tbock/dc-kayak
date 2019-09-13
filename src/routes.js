import Home from "./components/routes/home/Home";
// import About from "./components/routes/about/About";

const routes = {
  mode: "history",
  routes: [
    {
      path: "/",
      component: Home,
      name: "home"
    }
  ]
};

export default routes;
