import Booking from "./pages/booking/Booking.vue";
import Login from "./pages/login/Login.vue";

export default [
  { path: "/", component: Booking, name: "home" },
  { path: "/login", component: Login, name: "login" },
];
