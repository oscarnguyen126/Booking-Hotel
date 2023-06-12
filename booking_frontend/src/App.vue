<script>
import RoomItem from './components/RoomItem.vue'
import CreateRoomModal from './components/CreateRoomModal.vue'
import FacItem from './components/FacItem.vue'
import DetailRoomModal from './components/DetailRoomModal.vue'
import UpdateRoomModal from './components/UpdateRoomModal.vue'
import * as yup from "yup";

export default {
  name: 'App',
  components: {
    RoomItem, CreateRoomModal, FacItem, DetailRoomModal, UpdateRoomModal
  },
  data() {
    return {
      title: 'Hotel Booking',
      listRoom: [],
      isModalCreateRoomOpen: false,
      listFacs: [],
      errors: {
        title: 'Is required'
      }
    }
  },
  methods: {
    async getData() {
      const res = await fetch("http://127.0.0.1:8000/rooms/");
      const finalRes = await res.json();
      this.listRoom = finalRes;
    },

    async createRoom(data) {
      const yupObject = yup.object().shape({
        name: yup.string().required(),
        description: yup.string(),
        price: yup.number(),
        roomsize: yup.number(),
        facilities: yup.array()
          .of(
            yup.object().shape({
              name: yup.string(),
              checked: yup.boolean(),
            })
          )
          .compact((v) => !v.checked),
        image: yup.string()
      });
      yupObject.validate(data);
      try {
        // TODO:
        // validate data use yup validator
        // if correct -> send request + push into listRoom
        // incorrect -> save error message into state + show error message under corresponding input
        await fetch("http://127.0.0.1:8000/rooms/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data)
        })
        data.facilities = this.listFacs.filter(e => data.facilities.includes(e.name))
        this.listRoom.push(data)
        this.toggleModalCreateRoom()
      } catch (e) {
        alert(e.message)
      }
    },

    async updateRoom(id, data) {
      try {
        fetch(`http://127.0.0.1:8000/rooms/${id}`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(data)
        })
      }
      catch (e) {
        alert(e.message)
      }
    },

    deleteRoom(id) {
      if (!confirm('are u sure?')) return
      fetch(`http://127.0.0.1:8000/rooms/${id}`, {
        method: 'DELETE',
      })
      this.listRoom = this.listRoom.filter(room => room.id !== id)
    },
    toggleModalCreateRoom() {
      this.isModalCreateRoomOpen = !this.isModalCreateRoomOpen;
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
    <RoomItem :room="room" :deleteRoom="deleteRoom" :updateRoom="updateRoom" :listFacs="listFacs" />
  </div>
  <div v-if="isModalCreateRoomOpen">
    <CreateRoomModal :createRoom="createRoom" :isOpen="isModalCreateRoomOpen" :listFacs="listFacs"
      @click.self="toggleModalCreateRoom" />
  </div>
  <!-- <div>
    <UpdateRoomModal :updateRoom="updateRoom" />
  </div> -->
  <button class="create-button" @click="toggleModalCreateRoom">Create new room</button>
</template>


<style scope>
body {
  padding: 0;
}

h1 {
  background: linear-gradient(90deg, #ff0000, #ffff00, #ff00f3, #0033ff, #ff00c4, #ff0000);
  background-size: 400%;
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

.create-button {
  margin-top: 1%;
  background-color: blueviolet;
  border: 1px solid purple;
}
</style>
