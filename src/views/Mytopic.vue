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
        <v-dialog v-model="dialog" persistent max-width="600px">
          <template v-slot:activator="{ on }">
            <v-btn x-large rounded color="black--text white" dark class="ma-3" v-on="on">
              <v-icon class="mr-4">mdi-plus</v-icon>
              <div class="subtitle">New</div>
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">New Assignment</span>
            </v-card-title>
            <v-container>
              <v-form ref="form" v-model="valid" :lazy-validation="lazy">
                <v-card-text>
                  <v-row>
                    <v-col cols="12" sm="6" md="12">
                      <v-text-field
                        prepend-icon="mdi-rename-box"
                        v-model="subject"
                        label="Topic Name"
                        required
                        :rules="nameRules"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="12">
                      <v-menu
                        v-model="menu2"
                        :close-on-content-click="false"
                        transition="scale-transition"
                        offset-y
                        max-width="290px"
                        min-width="290px"
                      >
                        <template v-slot:activator="{ on }">
                          <v-text-field
                            v-model="computedDateFormatted"
                            label="Deadline Date"
                            hint="MM/DD/YYYY format"
                            persistent-hint
                            prepend-icon="mdi-calendar"
                            readonly
                            v-on="on"
                            :rules="dateRules"
                          ></v-text-field>
                        </template>
                        <v-date-picker v-model="date" no-title @input="menu2 = false"></v-date-picker>
                      </v-menu>
                    </v-col>

                    <v-col cols="12" sm="6" md="12">
                      <v-menu
                        ref="menu"
                        v-model="menu"
                        :close-on-content-click="false"
                        :nudge-right="40"
                        :return-value.sync="time"
                        transition="scale-transition"
                        offset-y
                        max-width="290px"
                        min-width="290px"
                      >
                        <template v-slot:activator="{ on }">
                          <v-text-field
                            v-model="time"
                            label="Deadline Time"
                            prepend-icon="mdi-clock"
                            readonly
                            v-on="on"
                            :rules="timeRules"
                          ></v-text-field>
                        </template>
                        <v-time-picker
                          v-if="menu"
                          v-model="time"
                          full-width
                          @click:minute="$refs.menu.save(time)"
                        ></v-time-picker>
                      </v-menu>
                    </v-col>

                    <v-col cols="12" sm="6" md="12">
                      <v-file-input
                        v-model="files"
                        color="deep-purple accent-4"
                        counter
                        label="File input"
                        placeholder="Select your files"
                        prepend-icon="mdi-paperclip"
                        outlined
                        :show-size="1000"
                        :rules="fileRules"
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
                  </v-row>
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="blue darken-1" @click="reset()">Close</v-btn>
                  <v-btn color="blue darken-1" :disabled="!valid" @click="add()">Save</v-btn>
                </v-card-actions>
              </v-form>
            </v-container>
          </v-card>
        </v-dialog>

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
                My Topics
                <v-icon color="grey">mdi-menu-down</v-icon>
              </v-btn>
            </template>
            <v-card style="width: 350px;">
              <v-list dense>
                <v-list-item-group>
                  <!-- <v-dialog v-model="dialog" persistent max-width="600px">
                    <template v-slot:activator="{ on }">
                      <v-list-item class="mt-3 mb-2" v-on="on">
                        <v-list-item-icon class="ml-2">
                          <v-icon>mdi-folder-plus</v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                          <v-list-item-title>New assignment</v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>
                    </template>
                    <v-card>
                      <v-card-title>
                        <span class="headline">New Assignment</span>
                      </v-card-title>
                      <v-card-text>
                        <v-container>
                          <v-row>
                            <v-col cols="12" sm="6" md="12">
                              <v-text-field v-model="subject" label="Topic Name" required></v-text-field>
                            </v-col>
                            <v-col cols="12" sm="6" md="12">
                              <v-text-field v-model="myclass" label="Some field" required></v-text-field>
                            </v-col>
                            <v-col cols="12" sm="6" md="12">
                              <v-text-field v-model="subjectId" label="Some field" required></v-text-field>
                            </v-col>
                            <v-col cols="12" sm="6" md="12">
                              <v-file-input
                                v-model="files"
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
                          </v-row>
                        </v-container>
                      </v-card-text>
                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="blue darken-1" text @click="reset()">Close</v-btn>
                        <v-btn color="blue darken-1" text @click="add()">Save</v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>-->
                </v-list-item-group>
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
              <v-subheader class="white--text">Topic</v-subheader>
            </v-container>
          </v-col>

          <v-col cols="12" sm="4">
            <v-container class="pa-0 ma-0">
              <v-subheader class="white--text">Deadline</v-subheader>
            </v-container>
          </v-col>
          <v-col cols="12" sm="4">
            <v-container class="pa-0 ma-0">
              <v-subheader class="white--text">Number of Submissions</v-subheader>
            </v-container>
          </v-col>
          <!-- <v-col cols="12" sm="3">
            <v-container class="pa-0 ma-0">
              <v-subheader></v-subheader>
            </v-container>
          </v-col>-->
        </v-row>
        <v-divider class="ma-0 pa-0"></v-divider>
        <v-list class="ma-0 pa-0" flat min-width="100%" dark>
          <v-list-item-group>
            <v-list-item
              class="ma-0 pa-0"
              v-for="item in topics"
              :key="item.topic"
              @dblclick="opentopic(item.topic)"
            >
              <v-container class="ma-0 pa-0">
                <v-row no-gutters>
                  <v-col cols="12" sm="4">
                    <v-subheader class="caption font-weight-bold">{{item.topic}}</v-subheader>
                  </v-col>
                  <v-col cols="12" sm="4">
                    <v-subheader class="caption font-weight-bold">{{item.deadline}}</v-subheader>
                  </v-col>
                  <v-col cols="12" sm="4">
                    <v-subheader class="caption font-weight-bold">{{item.total}}</v-subheader>
                  </v-col>
                  <!-- <v-col cols="12" sm="3">
                    
                  </v-col>-->
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
import db from "@/fb.js";
import firebase from "firebase";
export default {
  name: "Mytopic",

  data: () => ({
    files: null,
    dialog: false,
    subject: "",

    url: "",
    subjects: [
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
    topics: [],
    upload: "",

    //datepickers
    menu2: false,
    date: "",

    //timepickers
    time: null,
    menu: false,
    valid: true,
    lazy: false,
    nameRules: [v => !!v || "Title is required"],
    dateRules: [v => !!v || "Date is required"],
    timeRules: [v => !!v || "Time is required"],
    fileRules: [v => !!v || "File is required"]
  }),
  computed: {
    computedDateFormatted() {
      return this.formatDate(this.date);
    }
  },
  /* eslint-disable */
  watch: {
    date(val) {
      this.dateFormatted = this.formatDate(this.date);
    }
  },
  /* eslint-enable */

  methods: {
    /* eslint-disable */

    formatDate(date) {
      if (!date) return null;

      const [year, month, day] = date.split("-");
      return `${month}/${day}/${year}`;
    },
    parseDate(date) {
      if (!date) return null;

      const [month, day, year] = date.split("/");
      return `${year}-${month.padStart(2, "0")}-${day.padStart(2, "0")}`;
    },

    add() {
      var file = this.files;
      var ref = firebase
        .storage()
        .ref(this.$route.params.id + "/" + this.subject + "/original.txt");
      var task = ref.put(file);
      task.on(
        "state_changed",
        snapshot => {
          this.upload = (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
        },
        error => {
          console.log(error.message);
        },
        () => {
          this.upload = 100;
          task.snapshot.ref.getDownloadURL().then(url => {
            this.url = url;
            console.log(url);

            db.collection("Assignments")
              .doc(this.subject)
              .set({
                deadline: this.formatDate(this.date),
                time: this.time,
                subject: this.$route.params.id,
                url: this.url,
                total: 0
              })
              .then(docRef => {
                this.$router.go();
              });
          });
        }
      );
    },
    /* eslint-enable */
    reset() {
      (this.subject = ""), (this.subjectId = ""), (this.myclass = "");
      this.dialog = false;
      this.files = [];
      this.$router.go();
    },
    remove() {
      this.subjects.pop();
    },
    opentopic(id) {
      this.$router.push({
        name: "Submissions",
        params: { topic: id, subject: this.$route.params.id }
      });
    }
  },
  created() {
    db.collection("Assignments")
      .where("subject", "==", this.$route.params.id)
      .get()
      .then(querySnapshot => {
        querySnapshot.forEach(doc => {
          let data = {
            topic: doc.id,
            deadline: doc.data().deadline,
            url: doc.data().url,
            total: doc.data().total
          };

          this.topics.push(data);
        });
      })
      .catch(function(error) {
        window.alert("You have no assignments!" + error);
      });
  }
};
</script>

<style scoped>
#app > div.v-application--wrap > main > div > div {
  padding: 0px;
}

#app > div.v-application--wrap > main > div > div > div.container {
  padding: 0;
}
</style>