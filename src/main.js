import Vue from "vue";
// import "./plugins/axios";

// import axios from "axios";
// import VueAxios from "vue-axios";
import App from "./App.vue";
import router from "./router";

import vuetify from "./plugins/vuetify";

Vue.config.productionTip = false;
// Vue.use(VueAxios, axios);

new Vue({
  router,
  vuetify,
  render: (h) => h(App),
}).$mount("#app");
