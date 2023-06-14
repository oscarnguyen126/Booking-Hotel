import { createApp } from "vue";
import App from "./App.vue";
import ToastPlugin from "vue-toast-notification";
import "./style.css";
import "vue-toast-notification/dist/theme-default.css";
import routes from "./routes";
import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(),
  routes,
});

createApp(App).use(ToastPlugin).use(router).mount("#app");
