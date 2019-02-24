<template>
  <div id="app">
    <p>Hello, {{ name }}</p>
  </div>
</template>

<script>
export default {
  name: "app",
  data() {
    return {
      name: "Chris"
    };
  },
  methods: {
    getPlace() {
      this.name = "Alex";
    }
  }
};
</script>
<style lang="stylus"></style>
