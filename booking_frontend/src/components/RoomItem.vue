<script>
export default {
  props: ['room', 'deleteRoom'],
  methods: {
    showDetail() {
      alert(JSON.stringify(this.room))
    }
  }
}
</script>


<template>
  <div class="room" @click="showDetail">
    <div>
      <img :src="room.img" class="room-image" />
    </div>
    <div>
      <p>{{ room.name }}</p>
      <p style="font-weight: normal;">{{ room.description }}</p>
      <button class="remove" @click.stop="deleteRoom(room.id)">Remove</button>
    </div>
  </div>
</template>


<style>
.room {
  border: 1px solid purple;
  background-color: white;
  color: black;
  border-bottom: 40px;
  font-weight: bold;
  text-align: start;
  display: flex;
}

.room-image {
  width: 150px;
  height: 150px;
}

.roomDetail {
  color: white;
  background-color: blue;
  margin-bottom: 10px;
  margin-top: 0;
  margin-left: 40em;
}

.remove {
  margin-left: 50em;
  background-color: white;
  color: black;
  border: 1px solid black;
}
</style>
