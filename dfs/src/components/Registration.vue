<template>
  <div>
    <form>
      <h3>Sign Up</h3>

      <div class="form-group">
        <label>Full Name</label>
        <input
          type="text"
          class="form-control form-control-lg"
          v-model="form.fullName"
        />
      </div>

      <div class="form-group">
        <label>Email address</label>
        <input
          type="email"
          class="form-control form-control-lg"
          v-model="form.UserName"
        />
      </div>

      <div class="form-group">
        <label>Password</label>
        <input
          type="password"
          class="form-control form-control-lg"
          v-model="form.UserPassword"
        />
      </div>

      <button @click="onSubmit" class="btn btn-dark btn-lg btn-block">
        Sign Up
      </button>

      <p class="forgot-password text-right">
        Already registered
        <router-link :to="{ name: 'login' }">sign in?</router-link>
      </p>
    </form>
  </div>
</template>
 
<script>
export default {
  data() {
    return {
      form: {
        fullName: "",
        UserName: "",
        UserPassword: "",
      },
    };
  },

  created() {
    console.log("hea;lke ");
  },

  methods: {
    onSubmit(event) {
      event.preventDefault();
      console.log(this.form);

      let data = this.form;

      axios
        .post(server.API_URL + "user", data)
        .then(function (response) {
          console.log(response);
          if(response){
            alert("successfully added to db");
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
};
</script>