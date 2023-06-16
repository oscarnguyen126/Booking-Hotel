<script>
export default {};
</script>

<template>
  <h1 class="title">Hotel Booking</h1>

  <slot />
</template>

<style>
.title {
  background: linear-gradient(
    90deg,
    #ff0000,
    #ffff00,
    #ff00f3,
    #0033ff,
    #ff00c4,
    #ff0000
  );
  background-size: 300%;
  font-size: 70px;
  font-family: sans-serif;
  letter-spacing: 5px;
  font-weight: 600;
  word-spacing: 5px;
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
  animation: animate 20s linear infinite;
}

@keyframes animate {
  0% {
    background-position: 0%;
  }

  10% {
    background-position: 400%;
  }
}
</style>
