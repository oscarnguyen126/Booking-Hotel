<script>
import Modal from "../../../components/Modal.vue";
import { convertBase64 } from "../../../utils";

export default {
  components: { Modal },
  props: [
    "room",
    "isOpen",
    "facilities",
    "updateRoom",
    "toggleModalUpdateRoom",
  ],
  data() {
    return {
      form: {
        ...this.room,
        facilities: this.room.facilities.map((e) => e.name),
      },
    };
  },
  methods: {
    async onFileChanged({ target }) {
      if (target && target.files) {
        const file = target.files[0];
        const base64img = await convertBase64(file);
        this.form.img = base64img;
      }
    },
    onSubmit() {
      this.updateRoom(this.room.id, this.form);
      this.toggleModalUpdateRoom();
    },
  },
};
</script>

<template>
  <Modal :isOpen="this.isOpen">
    <form class="form" @submit.prevent="onSubmit">
      <div>
        <div class="input-group">
          <label class="input-label" for="name">Room name</label>
          <input
            v-model="form.name"
            type="text"
            id="name"
            name="name"
            placeholder="Room name"
            required
          />
        </div>

        <div class="input-group">
          <label class="input-label" for="roomsize">Room size</label>
          <input
            v-model="form.roomsize"
            type="number"
            id="roomsize"
            name="roomsize"
            placeholder="Room size"
          />
        </div>

        <div class="input-group">
          <label class="input-label" for="description">Room description</label>
          <textarea
            v-model="form.description"
            type="text"
            id="description"
            name="description"
            placeholder="Description"
          />
        </div>

        <div class="input-group">
          <label class="input-label" for="price">Price</label>
          <input
            v-model="form.price"
            type="number"
            id="price"
            name="price"
            placeholder="Price"
          />
        </div>

        <div class="input-group">
          <label class="input-label" for="img">Image</label>
          <input
            id="img"
            type="file"
            @change="onFileChanged($event)"
            accept="image/*"
            capture
          />
        </div>

        <div class="input-group">
          <label class="input-label">Facilities</label>
          <div class="facility-checkbox-group">
            <div class="facility-checkbox-input" v-for="item in facilities">
              <input
                v-model="form.facilities"
                type="checkbox"
                name="facs"
                :value="item.name"
                :id="item.id"
              />
              <label :for="item.id">{{ item.name }}</label>
            </div>
          </div>
        </div>
      </div>
      <div class="submit-container">
        <button
          class="create-button"
          type="submit"
          name="update"
          @click="toggleModalUpdateRoom"
        >
          Update
        </button>
      </div>
    </form>
  </Modal>
</template>
