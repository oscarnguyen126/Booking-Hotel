<script>
import Modal from "../../../components/Modal.vue";
import { convertBase64 } from "../../../utils";

export default {
  props: ["createRoom", "isOpen", "facilities"],
  components: { Modal },
  data() {
    return {
      form: {
        name: "",
        description: "",
        price: 0,
        img: null,
        facilities: [],
        roomsize: 0,
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
  },
};
</script>

<template>
  <Modal :isOpen="this.isOpen">
    <form class="form" @submit.prevent="createRoom(form)">
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
        <button class="create-button" type="submit" name="create">
          Submit
        </button>
      </div>
    </form>
  </Modal>
</template>

<style>
.facility-checkbox-group {
  display: flex;
  flex-wrap: wrap;
}

.facility-checkbox-input {
  width: 50%;
}

.form {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.submit-container {
  display: flex;
  flex-grow: 1;
  justify-content: center;
  align-items: end;
}

.input-group {
  padding-bottom: 12px;
  display: flex;
  flex-direction: column;
}

.input-label {
  font-weight: 600;
  font-size: 16px;
}
</style>
