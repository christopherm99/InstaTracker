<template>
  <div class="map">
    <l-map ref="map" :zoom="zoom" :center="center" :options="mapOptions">
      <l-tile-layer :url="url" :attribution="attribution" />
      <l-marker v-for="post in posts" :key="post.id" :lat-lng="post.location">
        <l-popup @click="goToPost(post)">
          <a class="popup" :href="'https://www.instagram.com/p/' + post.id">
            <img class="image" :src="post.img" />
            <div>
              {{ post.date }}
            </div>
            <div>
              {{ post.comment }}
            </div>
          </a>
        </l-popup>
        <l-polyline :latLngs="line"></l-polyline>
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
      url:
        "https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png",
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      mapOptions: {
        zoomSnap: 0.5
      }
    };
  },
  props: ["posts", "line"],
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
.image {
  width: 200px;
}
.popup {
  text-decoration: none;
  color: black;
}
</style>
