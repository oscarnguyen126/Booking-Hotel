<script>
export default {
  props: ["isOpen"],
};
</script>

<template>
  <div class="backdrop" v-if="this.isOpen">
    <div class="modal">
      <slot />
    </div>
  </div>
</template>

<style>
.modal {
  width: 600px;
  padding: 20px;
  margin: 100px auto;
  background: rgb(27, 26, 26);
  border-radius: 10px;
  color: white;
  text-align: start;
  border: 1px solid purple;

  overflow-y: scroll;
  overflow-x: hidden;
  max-height: 80vh;
}

.backdrop {
  top: 0;
  position: fixed;
  background: rgba(0, 0, 0, 0.5);
  width: 100%;
  height: 100%;
  left: 0;
}
</style>
