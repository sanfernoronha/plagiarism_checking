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
                My Assignments
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
          <v-col cols="12" sm="2" md="2" lg="2">
            <v-container class="pa-0 ma-0">
              <v-subheader class="white--text">
                Topic
                <v-btn icon class="white--text">
                  <v-icon>mdi-arrow-up</v-icon>
                </v-btn>
                <v-btn icon class="white--text">
                  <v-icon>mdi-arrow-down</v-icon>
                </v-btn>
              </v-subheader>
            </v-container>
          </v-col>

          <v-col cols="12" sm="2" md="2" lg="2">
            <v-container class="pa-0 ma-0">
              <v-subheader class="white--text">Some header</v-subheader>
            </v-container>
          </v-col>
          <v-col cols="12" sm="4" md="4" lg="4">
            <v-container class="pa-0 ma-0">
              <v-subheader class="white--text">Upload file</v-subheader>
            </v-container>
          </v-col>
          <v-col cols="12" sm="2" md="2" lg="2">
            <v-container class="pa-0 ma-0">
              <v-subheader class="white--text">Actions</v-subheader>
            </v-container>
          </v-col>
          <v-col cols="12" sm="2" md="2" lg="2">
            <v-container class="pa-0 ma-0 text-center">
              <v-subheader class="white--text">Status</v-subheader>
            </v-container>
          </v-col>
        </v-row>
        <v-divider class="ma-0 pa-0"></v-divider>
        <v-list class="ma-0 pa-0" dark>
          <v-list-item-group>
            <v-list-item class="ma-0 pa-0" v-for="item in assignments" :key="item.name">
              <v-container class="ma-0 pa-0">
                <v-row no-gutters>
                  <v-col cols="12" sm="2" md="2" lg="2">
                    <v-subheader class="caption font-weight-bold">
                      {{
                      item.name
                      }}
                    </v-subheader>
                  </v-col>

                  <v-col cols="12" sm="2" md="2" lg="2">
                    <v-subheader class="caption font-weight-bold">
                      {{
                      item.deadline
                      }}
                    </v-subheader>
                  </v-col>
                  <v-col cols="12" sm="4" md="4" lg="4">
                    <v-file-input
                      class="mt-5"
                      dense
                      v-model="item.file"
                      color="deep-purple accent-4"
                      counter
                      label="File input"
                      placeholder="Select your files"
                      prepend-icon="mdi-paperclip"
                      outlined
                      :show-size="1000"
                    >
                      <template v-slot:selection="{ index, text }">
                        <v-chip
                          v-if="index < 2"
                          color="deep-purple accent-4"
                          dark
                          label
                          small
                        >{{ text }}</v-chip>

                        <span
                          v-else-if="index === 2"
                          class="overline grey--text text--darken-3 mx-2"
                        >+{{ files.length - 2 }} File(s)</span>
                      </template>
                    </v-file-input>
                  </v-col>
                  <v-col cols="12" sm="2" md="2" lg="2">
                    <v-tooltip bottom>
                      <template v-slot:activator="{ on }">
                        <v-btn
                          icon
                          v-on="on"
                          class="mt-3 ml-6"
                          @click="send(item.url, item.file,item.name,item.total)"
                        >
                          <v-icon>mdi-check-circle-outline</v-icon>
                        </v-btn>
                      </template>
                      <span>Submit</span>
                    </v-tooltip>
                  </v-col>
                  <v-col cols="12" sm="2" md="2" lg="2"></v-col>
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
import axios from "axios";
import db from "@/fb.js";
import firebase from "firebase";
export default {
  name: "Assignments",

  data: () => ({
    target_url: "",
    target_file: "",
    target_name: "",
    subjects: [
      {
        subject: "SPCC1",
        class: "TE COMPUTERS",
        date: Date.now(),
        subjectId: "S1",
        file: []
      },
      {
        subject: "SPCC2",
        class: "TE COMPUTERS",
        date: Date.now(),
        subjectId: "S2",
        file: []
      },
      {
        subject: "SPCC3",
        class: "TE COMPUTERS",
        date: Date.now(),
        subjectId: "S3",
        file: []
      }
    ],
    assignments: [],
    url: "",
    target_total: null,
    student_name: "",
    student: []
  }),
  methods: {
    send(url, file, name, total) {
      this.target_total = total;
      this.target_url = url;
      this.target_file = file;
      this.target_name = name;
      var formData = new FormData();
      formData.set("file", this.target_file);
      formData.set("url", this.target_url);
      console.log(formData);
      axios({
        method: "post",
        url: "/api/test/",
        data: formData,
        config: { headers: { "Content-Type": "multipart/form-data" } }
      })
        .then(response => {
          console.log(response.data.status);
          console.log(response.data.result);
          console.log(response.data.flag);
          if (response.data.flag) {
            var file = this.target_file;
            var ref = firebase
              .storage()
              .ref(
                "submissions/" +
                  this.$route.params.course +
                  "/" +
                  this.target_name +
                  "/" +
                  this.$route.params.student +
                  "_submission.txt"
              );
            var task = ref.put(file);
            task.on(
              "state_changed",
              snapshot => {
                this.upload =
                  (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
              },
              error => {
                console.log(error.message);
              },
              () => {
                this.upload = 100;
                task.snapshot.ref.getDownloadURL().then(url => {
                  this.url = url;
                  console.log(url);
                  this.target_total += 1;

                  db.collection("Assignments")
                    .doc(this.target_name)
                    .update({
                      total: this.target_total
                    });

                  db.collection("Submissions")
                    .doc(this.$route.params.course)
                    .collection(this.target_name)
                    .doc(this.$route.params.student)
                    .set({
                      Name: this.student[0].name,
                      label: response.data.result,
                      url: this.url
                    });
                });
                // this.$router.go();
              }
            );
          } else {
            window.alert("hello not submitted");
          }
        })
        .catch(error => {
          console.log(error);
        });
    }
  },
  created() {
    db.collection("Assignments")
      .where("subject", "==", this.$route.params.course)
      .get()
      .then(querySnapshot => {
        querySnapshot.forEach(doc => {
          let data = {
            name: doc.id,
            deadline: doc.data().deadline,
            url: doc.data().url,
            file: [],
            total: doc.data().total
          };
          this.assignments.push(data);
        });
      })
      .catch(function(error) {
        window.alert("You have no assignments for this subject!" + error);
      });

    db.collection("Student_Auth")
      .where("Roll", "==", this.$route.params.student)
      .get()
      .then(querySnapshot => {
        querySnapshot.forEach(doc => {
          let data = {
            name: doc.data().Name,
            roll: doc.data().Roll
          };
          this.student.push(data);
        });
      });
  }
};
</script>

<style>
#app > div > div {
  padding: 0px;
}
#app > div {
  background-color: grey;
}
</style>
