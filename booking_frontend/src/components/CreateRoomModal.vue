<script>
import { ref } from "vue";
export default {
  props: ['createRoom', 'formisOpen', 'listFacs'],
  data() {
    return {
      form: {
        name: "",
        description: "",
        price: 0,
        img: null,
        facs: [],
        roomsize: 0,
      },
    }
  },
  mounted() {
    console.log(this.listFacs)
  },
  methods: {
    async onFileChanged($event) {
      const convertBase64 = (file) => {
        return new Promise((resolve, reject) => {
          const fileReader = new FileReader();
          fileReader.readAsDataURL(file);

          fileReader.onload = () => {
            resolve(fileReader.result);
          };

          fileReader.onerror = (error) => {
            reject(error);
          };
        });
      };

      const target = $event.target;
      if (target && target.files) {
        const file = target.files[0];
        const base64img = await convertBase64(file)
        this.form.img = base64img;
      }
    },
  }
}

</script>


<template>
  <div class="backdrop">
    <div class="modal" v-if="this.formisOpen">
      <form @submit.prevent="createRoom(form)">
        <label for="name">Room name</label><br>
        <input v-model="form.name" type="text" id="name" name="name" placeholder="Room name" style="width: 100%;" /><br>
        <label for="roomsize">Room size</label><br>
        <input v-model="form.roomsize" type="number" id="roomsize" name="roomsize" placeholder="Room size"
          style="width: 100%;" /><br>
        <label for="description">Room description</label><br>
        <input v-model="form.description" type="text" id="description" name="description" placeholder="Description"
          style="height:200px; width: 100%;" /><br>
        <label for="price">Price</label><br>
        <input v-model="form.price" type="number" id="price" name="price" placeholder="Price" style="width: 100%;" /><br>
        <input type="file" @change="onFileChanged($event)" accept="image/*" capture /><br>
        <p>Facilities:</p>
        <div v-for="item in listFacs">
          <input v-model="form.facs" type="checkbox" name="facs" :value="item.name" :id="item.id" />
          <label :for="item.id">{{ item.name }}</label>
        </div>
        <button type="submit" name="create">Submit</button>
      </form>
    </div>
  </div>
</template>


<style>
.modal {
  width: 400px;
  padding: 20px;
  margin: 100px auto;
  background: rgb(255, 254, 254);
  border-radius: 10px;
  color: black;
  text-align: start;
}

.backdrop {
  top: 0;
  position: fixed;
  background: rgba(0, 0, 0, 0.5);
  width: 100%;
  height: 100%;
  left: 0;
}
</style>
