<template>
  <div class="map">
    <l-map ref="map" :zoom="zoom" :center="center" :options="mapOptions">
      <l-tile-layer :url="url" :attribution="attribution" />
      <l-marker v-for="post in posts" :key="post.id" :lat-lng="post.location">
        <l-popup @click="goToPost(post)">
          <a :href="'https://www.instagram.com/p/' + post.id">
            <img :src="post.img" />
            <div>
              {{ post.comment }}
            </div>
          </a>
        </l-popup>
      </l-marker>
    </l-map>
  </div>
</template>

<script>
import { L, LMap, LTileLayer, LMarker, LPopup } from "vue2-leaflet";

export default {
  data() {
    return {
      zoom: 5,
      center: L.latLng(39.8333333, -98.585522),
      url: "http://{s}.tile.osm.org/{z}/{x}/{y}.png",
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      mapOptions: {
        zoomSnap: 0.5
      },
      posts: [
        {
          location: [38.8977, -77.0366],
          img: "https://via.placeholder.com/150",
          id: "asdfjaksldf",
          comment:
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean quis nisl a nunc imperdiet malesuada a nec sapien. In ac augue tellus. Ut velit elit, ultricies a elementum et, dignissim nec nulla. Proin nibh ligula, pulvinar quis elit eu, auctor dapibus elit. Maecenas pulvinar quam massa. Sed interdum lectus fermentum."
        }
      ]
    };
  },
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LPopup
  },
  methods: {
    goToPage(post) {
      window.location.href = "https://www.instagram.com/p/" + post.id;
    }
  }
};
</script>

<style lang="stylus">
.map {
  width: 100%;
  height: 100vh;
}
</style>
