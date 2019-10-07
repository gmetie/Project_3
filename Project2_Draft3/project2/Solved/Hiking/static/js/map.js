// Creating map object
  var myMap = L.map("map", {
    center: [38.49, -106.08],
    zoom: 7
  });

  // Adding tile layer to the map
  var light = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.streets",
    accessToken: API_KEY
  }).addTo(myMap);

// Define variables for our tile layers

var dark = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.dark",
  accessToken: API_KEY
});

// Only one base layer can be shown at a time
var baseMaps = {
  Light: light,
  Dark: dark
};


  // Store API query variables
var url = "https://www.hikingproject.com/data/get-trails?lat=40.0274&lon=-105.2519&maxDistance=200&maxResults=500&key=" + TRAIL_KEY;


// Grab the data with d3
d3.json(url, function(response) {

  // Create a new marker cluster group
  var markers = L.markerClusterGroup();

  var trails = response.trails

  trails.forEach(function(data){
    markers.addLayer(L.marker([data.latitude, data.longitude])
    .bindPopup("<hr> Trail Name: " + data.name + "<hr> Length: " + data.length + "  Miles"));

  }) 

  // Add our marker cluster layer to the map
  myMap.addLayer(markers);
  L.control.layers(baseMaps).addTo(myMap);

});

console.log(myMap.getLayers())