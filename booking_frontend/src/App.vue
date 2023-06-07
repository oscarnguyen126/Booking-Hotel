<script>
import RoomItem from './components/RoomItem.vue'
import CreateRoomModal from './components/CreateRoomModal.vue'
import FacItem from './components/FacItem.vue'

export default {
  name: 'App',
  components: {
    RoomItem, CreateRoomModal, FacItem
  },
  data() {
    return {
      title: 'Hotel Booking',
      listRoom: [],
      formisOpen: false,
      listFacs: []
    }
  },
  methods: {
    async getData() {
      const res = await fetch("http://127.0.0.1:8000/rooms/");
      const finalRes = await res.json();
      this.listRoom = finalRes;
    },
    async createRoom(data) {
      try {
        const res = await fetch("http://127.0.0.1:8000/rooms/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data)
        })
        this.listRoom.push(data)
        console.log('====', this.listRoom)
        // TODO: apppend res to this.listRoom
      } catch (e) {
        console.error(e)
        // custom logic handle error
      }
    },
    deleteRoom(id) {
      alert('aze')
      fetch(`http://127.0.0.1:8000/rooms/${id}`, {
        method: 'DELETE',
      })
      this.listRoom = this.listRoom.filter(room => room.id !== id)
    },
    toggleForm() {
      this.formisOpen = !this.formisOpen;
    },
    async getFacs() {
      const res = await fetch("http://127.0.0.1:8000/facility/");
      const finalRes = await res.json();
      this.listFacs = finalRes;
    },
  },
  mounted() {
    this.getData()
    this.getFacs()
  }
}
</script>

<template>
  <h1>{{ title }}</h1>
  <div v-for="room in listRoom">
    <RoomItem :room="room" :deleteRoom="deleteRoom"/>
  </div>
  <div v-if="formisOpen">
    <CreateRoomModal :createRoom="createRoom" :formisOpen="formisOpen" :listFacs="listFacs" @click.self="toggleForm" />
  </div>
  <button @click="toggleForm">Create new room</button>
</template>


<style scope>
body {
  padding: 0;
  border: 1px solid purple
}

h1 {
  color: pink;
}
</style>
