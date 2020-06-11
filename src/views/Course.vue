<template>
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
              <v-list-item-title>My Courses</v-list-item-title>
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
              <v-list-item-title>My Courses</v-list-item-title>
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
              My Courses
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
            <v-subheader class="white--text">
              Subject
              
              
            </v-subheader>
          </v-container>
        </v-col>

        <v-col cols="12" sm="4">
          <v-container class="pa-0 ma-0">
            <v-subheader class="white--text">Year</v-subheader>
          </v-container>
        </v-col>
        <v-col cols="12" sm="4">
          <v-container class="pa-0 ma-0">
            <v-subheader class="white--text">
              Branch
              
              
            </v-subheader>
          </v-container>
        </v-col>
       
      </v-row>
      <v-divider class="ma-0 pa-0"></v-divider>
      <v-list class="ma-0 pa-0" dark>
        <v-list-item-group>
          <v-list-item
            class="ma-0 pa-0"
            v-for="item in courses"
            :key="item"
            @dblclick="opentopic(item)"
          >
            <v-container class="ma-0 pa-0">
              <v-row no-gutters>
                <v-col cols="12" sm="4">
                  <v-subheader class="caption font-weight-bold">{{item}}</v-subheader>
                </v-col>
                <v-col cols="12" sm="4">
                  <v-subheader class="caption font-weight-bold">{{classes}}</v-subheader>
                </v-col>
                <v-col cols="12" sm="4">
                  <v-subheader class="caption font-weight-bold">{{branch}}</v-subheader>
                </v-col>
              </v-row>
              <v-divider></v-divider>
            </v-container>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-container>
  </v-container>
</template>

<script>
import db from "@/fb.js";
export default {
  name: "Course",

  data: () => ({
    student: "7354",
    subjects: [
      {
        subject: "SPCC",
        class: "TE COMPUTERS",
        date: Date.now(),
        subjectId: "S1"
      },
      {
        subject: "DLDA",
        class: "SE COMPUTERS",
        date: Date.now(),
        subjectId: "S2"
      },
      {
        subject: "Algorithms",
        class: "SE COMPUTERS",
        date: Date.now(),
        subjectId: "S3"
      }
    ],
    courses: [],
    classes: "",
    branch: ""
  }),
  methods: {
    opentopic(id) {
      this.$router.push({
        name: "Assignments",
        params: { course: id, student: this.student }
      });
    }
  },
  created() {
    db.collection("Student_Auth")
      .doc(this.student)
      .get()
      .then(doc => {
        this.courses = doc.data().Subjects;
        this.branch = doc.data().Branch;
        this.classes = doc.data().Class;
      });
  }
};
</script>
￼
￼
￼
￼



<style >
#app > div > div {
  padding: 0px;
}
</style>