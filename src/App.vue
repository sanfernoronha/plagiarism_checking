<template>
  <v-app>
    <v-content>
      <router-view>
        <HelloWorld />
      </router-view>
    </v-content>
  </v-app>
</template>

<script>
// import axios from "axios";
import HelloWorld from "./components/HelloWorld";

export default {
  name: "App",

  components: {
    HelloWorld
  },

  data: () => ({}),
  methods: {},
  created() {
    //  axios.post("/api/test/",{
    //    username: "Sanfer",
    //    password: "hey"
    //  }).then(response=>{
    //    console.log(response.data.status)
    //  }).catch(error =>{
    //    console.log(error)
    //  })
  }
};
</script>

<style>
#app > div.v-application--wrap > main > div > div {
  padding: 0px;
}
#app > div.v-application--wrap > main > div {
  background-color: grey;
}
#app > div.v-application--wrap > main > div > div > div.container {
  padding: 0;
}
</style>
