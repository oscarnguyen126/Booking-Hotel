<script>
import LoginForm from "./components/LoginForm.vue";
import RegisterForm from "./components/RegisterForm.vue";
import { login } from "../../services/login.service";

const views = {
  LOGIN: "login",
  REGISTER: "register",
};

export default {
  name: "Login",
  components: { LoginForm, RegisterForm },
  data() {
    return {
      views,
      currentView: views.LOGIN,
    };
  },
  methods: {
    switchView() {
      this.currentView =
        this.currentView === views.LOGIN ? views.REGISTER : views.LOGIN;
    },
    async loginUser(data) {
      try {
        const isSuccess = await login(data);

        if (isSuccess) {
          this.$router.push("/");
        } else {
          window.location.reload();
        }
      } catch (e) {
        alert(e.message);
      }
    },
  },
  mounted() {},
};
</script>

<template>
  <div v-if="currentView === views.LOGIN">
    <LoginForm :loginUser="loginUser" />
  </div>
  <div v-if="currentView === views.REGISTER">
    <RegisterForm />
  </div>
  <button @click="switchView">
    {{ currentView === views.LOGIN ? "Register" : "Login" }}
  </button>
</template>

<style></style>
