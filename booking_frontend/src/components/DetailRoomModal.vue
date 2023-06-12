<script>
import Modal from './Modal.vue'


export default {
  props: ['room', 'isOpen'],
  components: { Modal },
  mounted() {
    console.log('detail setup', this.room.facilities)
  }
}
</script>


<template>
  <Modal :isOpen="this.isOpen">
    <h3 class="room-title">{{ this.room.name }}</h3>
    <p class="room-description">{{ this.room.description }}</p>
    <ul>
      <li>
        <p><span class="information-title">Room size:</span> {{ this.room.roomsize }} m2</p>
      </li>
      <li>
        <p class="information-title">Facilities:</p>
        <div class="room-facility-container">
          <div class="room-facility" v-for="facility in this.room.facilities">
            {{ facility.name }}
          </div>
        </div>
      </li>
    </ul>
    <div>
      <img :src="this.room.img" class="room-image" />
    </div>
    <p class="room-price">$ {{ this.room.price }} for 1 night</p>
    <div class="btn-wrapper">
      <button id="reserve">Reserve</button>
    </div>
  </Modal>
</template>


<style>
.room-facility-container {
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
}

.room-facility {
  width: 50%;
}

.information-title {
  font-weight: bold;
}

.room-price {
  display: flex;
  font-weight: bold;
  flex-direction: row-reverse;
  background: linear-gradient(90deg, #ff0000, #ffff00, #ff00f3, #0033ff, #ff00c4, #ff0000);
  background-size: 200%;
  -webkit-text-fill-color: transparent;
  -webkit-background-clip: text;
  animation: animate 10s linear infinite;
}

@keyframes animate {
  0% {
    background-position: 0%;
  }
}

#reserve {
  color: white;
  background-color: blueviolet;
  margin: 1%;
}
</style>