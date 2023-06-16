<script>
export default {
  props: ["loginUser"],
  data() {
    return {
      form: {
        username: "",
        password: "",
      },
    };
  },
};
</script>

<template>
  <form class="login" @submit.prevent="loginUser(form)">
    <div class="input-group">
      <label class="input-label" for="username">USERNAME</label>
      <input
        v-model="form.username"
        class="input-place"
        type="text"
        name="username"
        placeholder="USERNAME"
      />
    </div>
    <div class="input-group">
      <label class="input-label" for="password">PASSWORD</label>
      <input
        v-model="form.password"
        class="input-place"
        type="password"
        name="password"
        placeholder="Enter password"
      />
    </div>
    <div>
      <button class="btn-login">Login</button>
    </div>
  </form>
</template>

<style>
.login {
  display: flex;
  flex-direction: column;
  justify-items: center;
  text-align: left;
  margin: 10px auto;
  width: 300px;
  padding: 20px;
  background: rgb(27, 26, 26);
  border-radius: 30px;
  box-shadow: 0 0 20px #eee;
  border: 2px solid rgb(221, 6, 139);
}
.input-group {
  display: flex;
  flex-direction: column;
}
.input-label {
  font-weight: 600px;
  margin: 2%;
}

.btn-wrapper {
  display: flex;
  justify-content: center;
  margin-top: 10px;
}
.btn-login {
  background-image: linear-gradient(
    to right,
    #ff0084 0%,
    #33001b 51%,
    #ff0084 100%
  );
  margin: 10px auto;
  padding: 15px 45px;
  text-align: center;
  text-transform: uppercase;
  transition: 0.5s;
  background-size: 200% auto;
  color: white;
  border-radius: 10px;
  display: block;
}
.btn-login:hover {
  box-shadow: 0 0 20px #eee;
  background-position: right center;
  color: #fff;
  text-decoration: none;
}

.input-place {
  border-radius: 50px;
  height: 40px;
  color: white;
  border: 1px solid white;
}
</style>
