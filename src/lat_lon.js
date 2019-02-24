const axios = require("axios");
var start_link = "https://api.mapbox.com/geocoding/v5/mapbox.places/"
var end_link = ".json?access_token=pk.eyJ1IjoiY2FkMzE0IiwiYSI6ImNqc2ozaGQwYTF2bGk0OXM3Y3ltczI2aTYifQ.Txtofo3qGGSnep5GRu-vQw"
function makeLink(place_name){
  return start_link.concat(place_name, end_link);
};
function getCoor(place_name) {
  axios.get(makeLink(place_name))
  .then(response => {
      console.log(response);
    });
  };

getCoor("san francisco") 

/*axios.get("https://api.mapbox.com/geocoding/v5/mapbox.places/paris.json?access_token=pk.eyJ1IjoiY2FkMzE0IiwiYSI6ImNqc2ozaGQwYTF2bGk0OXM3Y3ltczI2aTYifQ.Txtofo3qGGSnep5GRu-vQw")
  .then(response => {
    console.log(response);
  }); */
