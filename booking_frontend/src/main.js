import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import ToastPlugin from "vue-toast-notification";
import "vue-toast-notification/dist/theme-default.css";

createApp(App).use(ToastPlugin).mount("#app");
