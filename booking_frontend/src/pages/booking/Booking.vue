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
      // TODO: validate me
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
    @click.self="toggleModalCreateRoom"
  />
  <button class="create-button" @click="toggleModalCreateRoom">
    Create new room
  </button>
</template>

<style scope></style>
