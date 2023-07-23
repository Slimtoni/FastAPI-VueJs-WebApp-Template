<template>
  <div class="card text-center m-3">
    <h5 class="card-header">VueJS Template</h5>
    <p class="h3">Server Root Response: {{rootResponse}}</p>
    <div class="container">
      <form @submit.prevent="createItem">
        <div class="form-group">
          <label>Article</label>
          <input
              type="text"
              placeholder="Bread"
              v-model="newArticleName"
              class="form-control"
          />
        </div>
        <button class="btn btn-primary" type="submit">Submit</button>
      </form>
    </div>
    <table class="table">
      <thead>
      <tr>
        <th scope="col">ID</th>
        <th scope="col">Article</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="(entry, i) in itemList" :key="i">
        <td>{{ entry.id }}</td>
        <td>{{ entry.description }}
          <button type="button" class="btn btn-danger" v-on:click="deleteItem(entry.id)">Delete</button></td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "post-request",
  data() {
    return {
      rootResponse: "",
      newArticleId: null,
      newArticleName: null,
      itemList: [],
      statusCode: null
    };
  },
  created() {
    axios.get("http://127.0.0.1:8081/").then(response => this.rootResponse = response.data.message);
    this.reloadList()
  },
  methods: {
    async createItem() {
      const item = {
        description: this.newArticleName,
        public: true
      };
      await axios.post("http://127.0.0.1:8081/item/", item).then(response => this.statusCode = response.status)
          .catch(err => console.log(err))
      this.clearForm()
      this.reloadList()
    },
    clearForm() {
      this.newArticleName = ""
    },
    reloadList() {
      axios.get("http://127.0.0.1:8081/all_items/").then(response => this.itemList = response.data);
    },
    async deleteItem(id) {
      await axios.delete("http://127.0.0.1:8081/item/" +id.toString()).then(response => console.log(response))
      this.reloadList()
    }
  }
};
</script>
