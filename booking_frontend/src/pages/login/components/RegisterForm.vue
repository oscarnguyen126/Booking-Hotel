<script>
export default {};
</script>

<template>
  <form class="register">
    <div class="input-group">
      <label class="input-label" for="username">USERNAME</label>
      <input
        class="input-place"
        type="text"
        name="username"
        placeholder="USERNAME"
      />
    </div>
    <div class="input-group">
      <label class="input-label" for="email">EMAIL</label>
      <input class="input-place" type="text" name="email" placeholder="EMAIL" />
    </div>
    <div class="input-group">
      <label class="input-label" for="password">PASSWORD</label>
      <input
        class="input-place"
        type="password"
        name="password"
        placeholder="PASSWORD"
      />
    </div>
    <div class="input-group">
      <label class="input-label" for="confirm-password">CONFIRM PASSWORD</label>
      <input
        class="input-place"
        type="password"
        name="confirm-password"
        placeholder="CONFIRM PASSWORD"
      />
    </div>
    <div class="btn-wrapper-register">
      <button class="btn-register">Register</button>
    </div>
  </form>
</template>

<style>
.register {
  display: flex;
  flex-direction: column;
  justify-items: center;
  text-align: left;
  margin: 10px auto;
  width: 300px;
  padding: 20px;
  background: rgb(27, 26, 26);
  border-radius: 30px;
  border: 2px solid rgb(221, 6, 139);
  box-shadow: 0 0 20px #eee;
}
.btn-register {
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
.btn-register:hover {
  box-shadow: 0 0 20px #eee;
  background-position: right center;
  color: #fff;
  text-decoration: none;
}
.btn-wrapper-register {
  display: flex;
  justify-content: center;
  margin-top: 10px;
}
</style>
