<script>
import DetailRoomModal from "./DetailRoomModal.vue";
import UpdateRoomModal from "./UpdateRoomModal.vue";
export default {
  props: ["room", "deleteRoom", "updateRoom", "facilities"],
  components: {
    DetailRoomModal,
    UpdateRoomModal,
  },
  data() {
    return {
      isModalDetailRoomOpen: false,
      isModalUpdateRoomOpen: false,
    };
  },
  methods: {
    showDetail() {
      this.toggleModalDetailRoom();
    },
    toggleModalDetailRoom() {
      this.isModalDetailRoomOpen = !this.isModalDetailRoomOpen;
    },
    toggleModalUpdateRoom() {
      this.isModalUpdateRoomOpen = !this.isModalUpdateRoomOpen;
    },
  },
};
</script>

<template>
  <div class="room" @click="showDetail">
    <img :src="room.img" class="room-image" />
    <div class="room-container">
      <div>
        <p class="room-title">{{ room.name }}</p>
        <p class="room-description">{{ room.description }}</p>
      </div>
      <div class="btn-wrapper">
        <button class="remove" @click.stop="deleteRoom(room.id)">Remove</button>
        <button class="remove" @click.stop="toggleModalUpdateRoom">
          Update
        </button>
      </div>
    </div>
  </div>

  <DetailRoomModal
    :isOpen="isModalDetailRoomOpen"
    :room="this.room"
    @click.self="toggleModalDetailRoom"
  />
  <UpdateRoomModal
    :isOpen="isModalUpdateRoomOpen"
    :room="this.room"
    :facilities="this.facilities"
    :updateRoom="updateRoom"
    :toggleModalUpdateRoom="toggleModalUpdateRoom"
  />
</template>

<style>
.room {
  text-align: start;
  display: flex;
  gap: 20px;
  margin: 2% auto 0;
  background: rgba(0, 0, 0, 0.5);
  border-radius: 5px;
  border: 1px solid purple;
}

.room-image {
  width: 215px;
  height: 215px;
}

.roomDetail {
  color: white;
  margin-bottom: 10px;
  margin-top: 0;
  margin-left: 40em;
}

.remove {
  background-color: blueviolet;
  color: black;
  border: 1px solid purple;
  border-radius: 5px;
  margin: 10px;
  color: white;
}

.btn-wrapper {
  display: flex;
  flex-direction: row-reverse;
  flex-grow: 2;
  align-items: end;
}

.room-container {
  flex-grow: 1;
  display: flex;
}

.room-description {
  font-style: italic;
}

.room-title {
  font-weight: bold;
  border-bottom: 1px solid purple;
}
</style>
