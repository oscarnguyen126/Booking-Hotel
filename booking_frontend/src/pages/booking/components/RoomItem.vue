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
    <div class="room-container">
      <img :src="room.img" class="room-image" />
      <div class="content">
        <p class="room-title">{{ room.name }}</p>
        <div class="line"></div>
        <p class="room-description">{{ room.description }}</p>
      </div>
    </div>
    <div class="btn-wrapper">
      <button class="btn-remove" @click.stop="deleteRoom(room.id)">
        Remove
      </button>
      <button class="btn-update" @click.stop="toggleModalUpdateRoom">
        Update
      </button>
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
}

.room-image {
  width: 215px;
  height: 215px;
  margin-right: 1%;
}

.roomDetail {
  color: white;
  margin-bottom: 10px;
  margin-top: 0;
  margin-left: 40em;
}

.btn-remove,
.btn-update {
  background-image: linear-gradient(
    to right,
    #ff0084 0%,
    #33001b 51%,
    #ff0084 100%
  );
  background-size: 200% auto;
  border: 1px solid purple;
  border-radius: 20px;
  margin: 10px 5px;
  color: white;
}

.btn-remove:hover,
.btn-update:hover {
  box-shadow: 0 0 20px #eee;
}

.btn-wrapper {
  display: flex;
  justify-content: flex-end;
  flex-direction: row-reverse;
  align-items: end;
  width: 10%;
}

.room-container {
  flex-grow: 1;
  display: flex;
  float: right;
}

.room:hover {
  box-shadow: 0 0 20px #e908e9;
}

.room-description {
  font-style: italic;
}

.room-title {
  font-weight: bold;
  margin-bottom: 0;
}
.line {
  height: 1px;
  background: white;
}
.content {
  width: 100%;
}
</style>
