
const map = L.map("map", {
    center: [60.192059, 24.945831],
    zoom: 13
});

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Stara',
    maxZoom: 20,
    id: 'mapbox.streets',
    accessToken: 'pk.eyJ1IjoidmphbmRyZWkiLCJhIjoiY2szMW03NWVvMDh0czNkcXV3b3pwODJzdCJ9.IntVurhAqNv-L70ZvDs9Xw'
}).addTo(map);

let filterall = document.getElementById('filterall');
let filter1 = document.getElementById('filter1');
let filter2 = document.getElementById('filter2');
let filter = document.getElementById('filter1');

const data = [
  {
  "type": "Feature",
    "properties": {
        "name": "Mäkelänrinteen Lukio",
        "amenity": "Baseball Stadium",
        "popupContent": "This is where the Rockies play!",
        "number": 1,
        "show_on_map": null
    },
    "geometry": {
        "type": "Point",
        "coordinates": [24.947900, 60.198420]
    }
  },

  {
  "type": "Feature",
    "properties": {
        "name": "Hietarannan uimaranta",
        "amenity": "Baseball Stadium",
        "popupContent": "This is where the Rockies play!",
        "number": 2,
        "show_on_map": null
    },
    "geometry": {
        "type": "Point",
        "coordinates": [25.111050, 60.216620]
    }
  }

]


let marker = L.geoJson(data).addTo(map);


document.addEventListener('input', function (event) {

  if (event.target.value === 'all') {
    marker.setFilter(function(f){
      return f.properties.show_on_map = true;
    });
  }
  
	if (event.target.value === 'value1') {
    marker.setFilter(function(f){
      return f.properties.number === 1;
    });
  }

  if (event.target.value === 'value2') {
    marker.setFilter(function(f){
      return f.properties.number === 2;
    });
  }
    
	// Do stuff...

}, false);

