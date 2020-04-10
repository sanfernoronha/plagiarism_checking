<template>
  <v-app>
    <v-container>
      <v-app-bar app flat dark>
        <v-spacer></v-spacer>
        <v-tooltip bottom>
          <template v-slot:activator="{ on }">
            <v-btn text icon style="margin-right:10px;" v-on="on">
              <v-icon>mdi-help-circle-outline</v-icon>
            </v-btn>
          </template>
          <span>Support</span>
        </v-tooltip>
        <v-tooltip bottom>
          <template v-slot:activator="{ on }">
            <v-btn text icon style="margin-right:30px;" v-on="on">
              <v-icon>mdi-wrench</v-icon>
            </v-btn>
          </template>
          <span>Settings</span>
        </v-tooltip>
        <v-tooltip bottom>
          <template v-slot:activator="{ on }">
            <v-btn text icon style="margin-right:10px;" v-on="on">
              <v-icon>mdi-apps</v-icon>
            </v-btn>
          </template>
          <span>Links</span>
        </v-tooltip>

        <v-btn x-small fab color="success" elevation="1">
          <div style="font-size: 1.5em;">S</div>
        </v-btn>
      </v-app-bar>

      <v-navigation-drawer permanent app dark>
        <v-list-item style="margin-bottom:7px;">
          <v-list-item-content>
            <v-list-item-title class="headline">Storage</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-divider></v-divider>

        <v-list shaped dense>
          <v-list-item-group color="amber">
            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-format-list-bulleted</v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title>My storage</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-star-outline</v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title>Starred</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-format-list-bulleted</v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title>My storage</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-navigation-drawer>
      <!-- content -->

      <v-row class="text-center">
        <v-toolbar dense flat dark class="grey darken-2">
          <v-menu offset-y>
            <template v-slot:activator="{ on }">
              <v-btn class="mb-auto" text style="border-radius:10px;" v-on="on">
                Submissions
                <v-icon color="grey">mdi-menu-down</v-icon>
              </v-btn>
            </template>
            <v-card style="width: 350px;">
              <v-list dense>
                <v-list-item-group></v-list-item-group>
              </v-list>
            </v-card>
          </v-menu>

          <v-spacer></v-spacer>
        </v-toolbar>
      </v-row>
      <v-divider></v-divider>

      <v-container>
        <v-row no-gutters>
          <v-col cols="12" sm="4">
            <v-container class="pa-0 ma-0">
              <v-subheader class="white--text">Student Name</v-subheader>
            </v-container>
          </v-col>

          <v-col cols="12" sm="4">
            <v-container class="pa-0 ma-0">
              <v-subheader class="white--text">P Class</v-subheader>
            </v-container>
          </v-col>
          <!-- <v-col cols="12" sm="3">
            <v-container class="pa-0 ma-0">
              <v-subheader class="white--text">
                Some sortable header
                <v-btn icon class="white--text">
                  <v-icon>mdi-arrow-up</v-icon>
                </v-btn>
                <v-btn icon class="white--text">
                  <v-icon>mdi-arrow-down</v-icon>
                </v-btn>
              </v-subheader>
            </v-container>
          </v-col>-->
          <v-col cols="12" sm="4">
            <v-container class="pa-0 ma-0">
              <v-subheader class="white--text">View</v-subheader>
            </v-container>
          </v-col>
        </v-row>
        <v-divider class="ma-0 pa-0"></v-divider>
        <v-alert
          :value="alert"
          color="primary"
          icon="mdi-alert"
          class="white white--text mt-5"
          border="left"
          dark
          prominent
        >No submissions yet!</v-alert>
        <v-list class="ma-0 pa-0" dark>
          <v-list-item-group>
            <v-list-item class="ma-0 pa-0" v-for="item in submitted" :key="item.name">
              <v-container class="ma-0 pa-0">
                <v-row no-gutters>
                  <v-col cols="12" sm="4">
                    <v-subheader class="caption font-weight-bold">{{item.name}}</v-subheader>
                  </v-col>
                  <v-col cols="12" sm="4">
                    <v-chip class="ma-2" :color="item.color" text-color="white">
                      <v-subheader class="caption font-weight-bold black--text">{{item.label}}</v-subheader>
                    </v-chip>
                  </v-col>
                  <!-- <v-col cols="12" sm="3">
                    <v-subheader class="caption font-weight-bold">Bleh</v-subheader>
                  </v-col>-->
                  <v-col cols="12" sm="4">
                    <v-btn rounded color="primary" dark class="mt-1" @click="view(item.url)">
                      <v-icon left>mdi-open-in-new</v-icon>Link
                    </v-btn>
                  </v-col>
                </v-row>
                <v-divider></v-divider>
              </v-container>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-container>
    </v-container>
  </v-app>
</template>

<script>
import db from "@/fb";
export default {
  name: "Submissions",

  data: () => ({
    submissions: [
      {
        subject: "SPCC1",
        class: "TE COMPUTERS",
        date: Date.now(),
        subjectId: "S1"
      },
      {
        subject: "SPCC2",
        class: "TE COMPUTERS",
        date: Date.now(),
        subjectId: "S2"
      },
      {
        subject: "SPCC3",
        class: "TE COMPUTERS",
        date: Date.now(),
        subjectId: "S3"
      }
    ],
    submitted: [],
    count: null,
    alert: false
  }),
  methods: {
    view(url) {
      window.open(url, "_blank");
    }
  },
  created() {
    db.collection("Assignments")
      .doc(this.$route.params.topic)
      .get()
      .then(doc => {
        this.count = doc.data().total;
        if (this.count == 0) {
          this.alert = true;
          console.log("hgeeg");
        } else {
          this.alert = false;
          db.collection("Submissions")
            .doc(this.$route.params.subject)
            .collection(this.$route.params.topic)
            .get()
            .then(querySnapshot => {
              querySnapshot.forEach(doc => {
                let data = {
                  name: doc.data().Name,
                  label: doc.data().label,
                  url: doc.data().url,
                  color: ""
                };
                if (data.label == "Non-Plagiarized") {
                  data.color = "green";
                } else if (data.label == "Lightly Plagiarized") {
                  data.color = "amber";
                } else {
                  data.color = "error";
                }

                this.submitted.push(data);
              });
            });
        }
      });
  }
};
</script>

<style >
#app > div > div {
  padding: 0px;
}
</style>