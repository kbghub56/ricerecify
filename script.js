var map;
var service;
var infowindow;
var input;

function initMap() {
    var riceRecreationCenter = { lat: 29.7174, lng: -95.4018 }; // Coordinates for Rice University Recreation Center

    infowindow = new google.maps.InfoWindow();
    map = new google.maps.Map(document.getElementById('map'), {
        center: riceRecreationCenter,
        zoom: 15
    });

    // Create an input field for Autocomplete
    input = document.getElementById('pac-input');
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);

    var autocomplete = new google.maps.places.Autocomplete(input);
    autocomplete.bindTo('bounds', map);

    autocomplete.addListener('place_changed', function () {
        infowindow.close();
        var place = autocomplete.getPlace();

        if (!place.geometry) {
            window.alert("No details available for input: '" + place.name + "'");
            return;
        }

        console.log("Place ID for Rice University Recreation Center: ", place.place_id);

        // Uncomment the line below if you want to display the Place details in an infowindow
        // displayPlaceDetails(place);
    });
}

function displayPlaceDetails(place) {
    infowindow.setContent('<div><strong>' + place.name + '</strong><br>' +
        'Place ID: ' + place.place_id + '<br>' +
        place.formatted_address + '</div>');
    infowindow.open(map, marker);
}
