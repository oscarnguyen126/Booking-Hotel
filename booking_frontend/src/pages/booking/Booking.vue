<script lang="js">
import RoomItem from './components/RoomItem.vue'
import CreateRoomModal from './components/CreateRoomModal.vue'
import DetailRoomModal from './components/DetailRoomModal.vue'
import UpdateRoomModal from './components/UpdateRoomModal.vue'
import { validate } from './validation'
import { bookingService } from '../../services/booking.service'

export default {
  name: 'Booking',
  components: {
    RoomItem, CreateRoomModal, DetailRoomModal, UpdateRoomModal
  },
  data() {
    return {
      rooms: [],
      facilities: [],
      isModalCreateRoomOpen: false,
      errors: {
        title: 'Is required'
      }
    }
  },
  methods: {
    logout() {
      localStorage.clear();
      this.$router.push({name:'login'})
    },
    toggleModalCreateRoom() {
      this.isModalCreateRoomOpen = !this.isModalCreateRoomOpen;
    },
    async getRooms() {
      this.rooms = await bookingService.getRooms()
    },
    async getFacilities() {
      this.facilities = await bookingService.getFacilities();;
    },
    async createRoom(data) {
      validate(data)
      try {
        await bookingService.createRoom(data)
        data.facilities = this.facilities.filter(e => data.facilities.includes(e.name))
        this.rooms.push(data)
        this.toggleModalCreateRoom()
      } catch (e) {
        alert(e.message)
      }
    },
    async updateRoom(id, data) {
      try {
        bookingService.updateRoom(id, data)
      }
      catch (e) {
        alert(e.message)
      }
    },
    async deleteRoom(id) {
      if (!confirm('are u sure?')) return
      await bookingService.deleteRoom(id)
      this.rooms = this.rooms.filter(room => room.id !== id)
    },
  },
  mounted() {
    this.getRooms()
    this.getFacilities()
  }
}
</script>

<template>
  <button class="btn-logout" @click="logout">Logout</button>
  <div v-for="room in rooms">
    <RoomItem
      :room="room"
      :facilities="facilities"
      :deleteRoom="deleteRoom"
      :updateRoom="updateRoom"
    />
  </div>
  <CreateRoomModal
    :isOpen="isModalCreateRoomOpen"
    :facilities="facilities"
    :createRoom="createRoom"
    :toggleModalCreateRoom="toggleModalCreateRoom"
    @click.self="toggleModalCreateRoom"
  />
  <button class="btn-create" @click="toggleModalCreateRoom">
    Create new room
  </button>
</template>

<style>
.btn-logout {
  position: absolute;
  top: 1%;
  right: 2%;
  border-radius: 30px;
  background-image: linear-gradient(
    to right,
    #ff0084 0%,
    #33001b 51%,
    #ff0084 100%
  );
  background-size: 200% auto;
}
.btn-logout:hover {
  box-shadow: 0 0 20px #eee;
}
.btn-create {
  margin-top: 1%;
  background-color: blueviolet;
  border: 1px solid purple;
  background-image: linear-gradient(
    to right,
    #ff0084 0%,
    #33001b 51%,
    #ff0084 100%
  );
  text-align: center;
  background-size: 200% auto;
  color: white;
  border-radius: 20px;
}
.btn-create:hover {
  box-shadow: 0 0 20px #eee;
}
</style>
