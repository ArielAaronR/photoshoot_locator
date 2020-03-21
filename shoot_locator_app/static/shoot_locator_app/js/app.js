// var map;
// var marker;
// var geocoder;


// function initMap() {
//   map = new google.maps.Map(document.getElementById("map"), {
//     center: { lat: 33.764147, lng: -118.007398 },
//     zoom: 10
//   });

//   var iconImg = {
//     url:
//       "data:image/png;base64,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",
//     scaledSize: new google.maps.Size(30, 30), // scaled size
//     origin: new google.maps.Point(0, 0), // origin
//     anchor: new google.maps.Point(0, 0) // anch
//   };

//   geocoder = new google.maps.Geocoder();
//   codeAddress(geocoder, map, iconImg);

//   function codeAddress(geocoder, map, iconImg) {
//     var markers = [];

//     var addresses = [
//       "3P2X+H9 Los Angeles, California",
//       "Downtown Fullerton",
//       "P4XJ+5X Santa Ana, California",
//       "200 N Pine Ave, Long Beach, CA 90802",
//       "200 W 2nd St, Pomona, CA 91766",
//       "3601 S Gaffey St, San Pedro, CA 90731"
//     ];
//     for (let address = 0; address < addresses.length; address++) {
//       geocoder.geocode({ address: addresses[address] }, function(
//         results,
//         status
//       ) {
//         if (status === "OK") {
//           marker = new google.maps.Marker({
//             map: map,
//             position: results[0].geometry.location,
//             animation: google.maps.Animation.DROP,
//             icon: iconImg
//           });
//           markers.push(marker);
//           marker.addListener("click", function() {
//             for (var i = 0; i < markers.length; i++) {
//               markers[i].setAnimation(null);
//             }
//             toggleBounce(this);
//           });
//         } else {
//           console.log(
//             "Geocode was not successful for the following reason: " + status
//           );
//         }
//       });
//     }
//     console.log(markers);
//     function toggleBounce(ele) {
//       if (ele.getAnimation() !== null) {
//         ele.setAnimation(null);
//       } else {
//         ele.setAnimation(google.maps.Animation.BOUNCE);
//       }
//     }
//   }
// }
