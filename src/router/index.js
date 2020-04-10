import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../components/HelloWorld.vue";
import Mytopic from "../views/Mytopic.vue";
import Submissions from "../views/Submissions.vue";
import Course from "../views/Course.vue";
import Assignments from "../views/Assignments.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/mytopic/:id",
    name: "Mytopic",
    component: Mytopic,
  },
  {
    path: "/submissions/:subject/:topic",
    name: "Submissions",
    component: Submissions,
  },
  {
    path: "/student/course",
    name: "Course",
    component: Course,
  },
  {
    path: "/student/assignments/:course/:student",
    name: "Assignments",
    component: Assignments,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
