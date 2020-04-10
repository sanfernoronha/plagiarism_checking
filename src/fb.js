import firebase from "firebase";
import "firebase/firestore";
import "firebase/storage";

var firebaseConfig = {
  apiKey: "AIzaSyCh7EYG7LPrDGRxq8K5G2Vg7YwZv9ORZGo",
  authDomain: "nlp-submission-portal.firebaseapp.com",
  databaseURL: "https://nlp-submission-portal.firebaseio.com",
  projectId: "nlp-submission-portal",
  storageBucket: "nlp-submission-portal.appspot.com",
  messagingSenderId: "677264496557",
  appId: "1:677264496557:web:cf34bc8ce86dcc6b37b324",
  measurementId: "G-2J7WTM11CS",
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

const db = firebase.firestore();
// const storageRef = firebase.storage();

export default db;
