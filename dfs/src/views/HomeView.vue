<template>
  <div>
    <b-nav tabs>
      <b-nav-item active>Home</b-nav-item>
      <b-nav-item>Post</b-nav-item>
      <b-nav-item>About</b-nav-item>
      <!-- <b-nav-item disabled>Disabled</b-nav-item> -->
      <b-nav-item>User</b-nav-item>
      <b-nav-item>Log Out</b-nav-item>
    </b-nav>

    <div class="vue-tempalte">
      <!-- Navigation -->
      <nav
        class="
          navbar
          shadow
          bg-white
          rounded
          justify-content-between
          flex-nowrap flex-row
          fixed-top
        "
      >
        <div class="container">
          <a
            class="navbar-brand float-left"
            href="https://www.positronx.io"
            target="_blank"
          >
            LOGO MKCL
          </a>
          <a class="navbar-brand float-right" href="" target="_blank"> HOME </a>
          <a class="navbar-brand float-right" href="" target="_blank">
            About
          </a>
          <div v-if="logged">
            <ul class="nav navbar-nav flex-row float-right">
              <li class="nav-item">
                <router-link class="nav-link pr-3" to="/login"
                  >Sign in</router-link
                >
              </li>
              <li class="nav-item">
                <router-link class="btn btn-outline-primary" to="/signup"
                  >Sign up</router-link
                >
              </li>
            </ul>
          </div>
          <div v-else>
            <ul class="nav navbar-nav flex-row float-right">
              <li class="nav-item">
                <button class="nav-link pr-3" @click="logout">
                  <strong>LogOut</strong>
                </button>
              </li>
            </ul>
          </div>
        </div>
      </nav>
      </div>

      <!-- Main -->
      <!-- <div class="App">
        <div class="vertical-center">
          <div class="inner-block">
            <button @click="log">Logg</button>
            <router-view />
          </div>
        </div>
      </div> -->


    <div v-for="(user, index) in user_api_data" :key="index">
      <div class="container mt-5">
        <div class="d-flex justify-content-center row">
          <div class="col-md-8 border border-dark">
            <div class="d-flex flex-column comment-section">
              <div class="bg-white p-2">
                <div class="d-flex flex-row user-info">
                  <img
                    class="rounded-circle"
                    src="https://i.imgur.com/RpzrMR2.jpg"
                    width="40"
                  />
                  <div class="d-flex flex-column justify-content-start ml-2">
                    <span class="d-block font-weight-bold name"
                      >&emsp;{{ user.UserName }}</span
                    ><span class="date text-black-50"
                      >Shared publicly - Jan 2020</span
                    >
                  </div>
                </div>
                <div class="mt-2 bg-light">
                  <p class="comment-text">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                    do eiusmod tempor incididunt ut labore et dolore magna
                    aliqua. Ut enim ad minim veniam, quis nostrud exercitation
                    ullamco laboris nisi ut aliquip ex ea commodo consequat.
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                    do eiusmod tempor incididunt ut labore et dolore magna
                    aliqua. Ut enim ad minim veniam, quis nostrud exercitation
                    ullamco laboris nisi ut aliquip ex ea commodo consequat.
                  </p>
                  <p class="comment-text">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                    do eiusmod tempor incididunt ut labore et dolore magna
                    aliqua. Ut enim ad minim veniam, quis nostrud exercitation
                    ullamco laboris nisi ut aliquip ex ea commodo consequat.
                  </p>
                </div>
              </div>
              <div class="bg-white">
                <div class="d-flex flex-row fs-12">
                  <div @click="like++" class="like p-2 cursor">
                    <i class="fa-solid fa-thumbs-up"></i
                    ><span class="ml-1">Like {{ like }}</span>
                  </div>
                  <div @click="dislike++" class="like p-2 cursor">
                    <i class="fa-solid fa-thumbs-down"></i
                    ><span class="ml-1">Dislike {{ dislike }}</span>
                  </div>
                  <div @click="comment = !comment" class="like p-2 cursor">
                    <i class="fa-regular fa-comment"></i
                    ><span class="ml-1">Comment</span>
                  </div>
                </div>
              </div>
              <div v-show="comment" class="p-2">
                <div class="d-flex flex-row align-items-start">
                  <img
                    class="rounded-circle"
                    src="https://i.imgur.com/RpzrMR2.jpg"
                    width="40"
                  /><b-form-input
                    v-model="cmt"
                    placeholder="Enter your thoughts..."
                  ></b-form-input>
                  <!-- <div class="mt-2">Value: {{ cmt }}</div> -->
                </div>
                <div class="mt-2 text-right">
                  <button
                    @click="postCmt(user.UserId)" class="btn btn-primary btn-sm shadow-none"
                    type="button"
                  >
                    Post comment
                  </button>
                  <span>&emsp;</span>
                  <button
                    @click="cancle" class="btn btn-outline-primary btn-sm ml-1 shadow-none"
                    type="button"
                  >
                    Cancel
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
// import LoginPage from '@/views/LoginPage.vue'
// import { Userdb } from "@/db/Userdb.js";
// import { db } from "@/db/db.js";
export default {
  name: "HomeView",

  data() {
    return {
      // users: [
      //   { username: "advay", password: "mehta" },
      //   { username: "nitish", password: "tiwari" },
      //   { username: "mdlucky", password: "lucky" },
      // ],
      users: [],
      logged: true,
      user_api_data: [],
      like: 0,
      dislike: 0,
      comment: false,
      cmt: "",
    };
  },
  created() {},
  mounted() {
    this.refreshData();
    // console.log("a", this.$store.state.data);
    //     var us = new Userdb();
    //     Userdb.getInstance()
    //       .get()
    //       .then((result) => {
    //         console.log(result);
    //       });
    //     const a = await us.get();

    //     db.users.toArray().then(function (arr) {
    //     console.log('mounted', arr);
    //     // return arr;
    // });

    console.log("route", this.$route.query.action);
    if (this.$route.query.action == "login") {
      this.$store.state.users = this.$route.query.data;
      this.logged = false;
    }
    console.log("log", this.logged);

   
    
    console.log("this.usrs:", this.user);
  },
  methods: {
    refreshData() {
      axios.get(server.API_URL + "user").then((response) => {
        this.user_api_data = response.data;
      });

      console.log("API1", this.user_api_data);
    },



    logout() {
      alert("Logged Out");
      // console.log("API1", this.user_api_data);
      this.logged = true;
      this.user = {};
      // window.location.reload();
      // this.$router.push({
      //   path: "/",
      //   params: null,
      // });
    },

    log() {
      console.log("apppp", this.user_api_data);
    },

    postCmt(userid){
      console.log(this.cmt, userid),

      this.comment = !this.comment,
      this.cmt = ""
    },
    cancle(){
      this.comment = !this.comment,
      this.cmt = ""
    },
  },
};
</script>

<style scoped>
body {
  background: rgb(138, 135, 135);
}

i {
  margin: 2px;
}
.blog {
  background-color: aquamarine;
}
.date {
  font-size: 11px;
}
.comment-text {
  font-size: 12px;
}
.fs-12 {
  font-size: 12px;
}
.shadow-none {
  box-shadow: none;
}
.name {
  color: #007bff;
}
.cursor:hover {
  color: blue;
}
.cursor {
  cursor: pointer;
}
.textarea {
  resize: none;
}
</style>
