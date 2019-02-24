<template>
  <div id="app">
    <v-app>
      <v-toolbar dark>
        <v-toolbar-title>InstaTracker</v-toolbar-title>
        <v-spacer />
        <v-toolbar-items>
          <v-btn v-if="selected" @click="newUser()" flat>{{ selected }}</v-btn>
        </v-toolbar-items>
      </v-toolbar>
      <v-dialog v-model="dialog" width="500" persistent>
        <v-card>
          <v-card-title class="headline grey lighten-2" primary-title>
            Enter a user
          </v-card-title>
          <v-card-text>
            <v-alert :value="error" type="error">
              {{ error }}
            </v-alert>
            <v-form>
              <v-text-field label="Instagram Handle" v-model="handle" />
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" flat @click="search()" :loading="loading">
              Search
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <Map v-if="!dialog" :posts="posts"></Map>
    </v-app>
  </div>
</template>

<script>
import Map from "./components/Map.vue";
import { L } from "vue2-leaflet";

export default {
  name: "app",
  data() {
    return {
      dialog: true,
      handle: "",
      posts: [],
      error: "",
      selected: "",
      loading: false,
      response: undefined
    };
  },
  components: {
    Map
  },
  methods: {
    search() {
      this.loading = true;
      this.axios
        .post("/profile/" + this.handle)
        .then(response => {
          this.response = response;
          this.loading = false;
          this.dialog = false;
          this.posts = [];
          this.selected = this.handle;
          response.data.posts.forEach(e => {
            this.posts.push({
              location: L.latLng(e.latitude, e.longitude),
              comment: e.text,
              img: e.img_url,
              id: e.id
            });
          });
        })
        .catch(reason => {
          this.loading = false;
          this.error = reason;
        });
    },
    newUser() {
      this.dialog = true;
      this.handle = "";
      this.selected = "";
    }
  }
};
</script>
<style lang="stylus">
.map {
  width: 100%;
  height: 100%;
}
</style>
