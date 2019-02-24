<template>
  <div id="app">
    <v-app>
      <v-toolbar dark>
        <v-toolbar-title>InstaTracker</v-toolbar-title>
      </v-toolbar>
      <v-dialog v-model="dialog" width="500">
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

export default {
  name: "app",
  data() {
    return {
      dialog: true,
      handle: "",
      posts: undefined,
      error: ""
    };
  },
  components: {
    Map
  },
  methods: {
    search() {
      this.loading = true;
      this.axios
        .get("/profile/" + this.handle)
        .then(response => {
          this.loading = false;
          this.dialog = false;
          this.posts = response.data.posts;
        })
        .catch(reason => {
          this.loading = false;
          this.error = reason;
        });
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
