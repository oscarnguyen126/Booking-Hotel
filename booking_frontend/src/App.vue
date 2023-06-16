<script>
import Layout from "./components/Layout.vue";
import Booking from "./pages/booking/Booking.vue";
import Login from "./pages/login/Login.vue";
import { STORED_USER_KEY } from "./services/constants";

export default {
  name: "App",
  components: {
    Booking,
    Layout,
    Login,
  },
  mounted() {
    const isAuthenticated =
      window.localStorage.getItem(STORED_USER_KEY) || false;
      console.log(window.localStorage.getItem(STORED_USER_KEY))

    if (isAuthenticated) {
      this.$router.push("/");
    } else {
      this.$router.push("/login");
    }
  },
};
</script>

<template>
  <Layout>
    <router-view></router-view>
  </Layout>
</template>

<style scope></style>
