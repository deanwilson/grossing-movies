$(document).ready(function() {

  $.ajax({
    method: "GET",
    url: "/films/2017",
    dataType: 'JSON',
  })
    .done(function( msg ) {
      var results = msg.films;

//     var results = JSON.stringify(msg.films);
//     alert( "-- Films --: " + Object.keys(results));

//      alert("Single file: " + film_title + " released in " + film_year + " made " + film_amount)

      // TODO
      // Ensure none of the random selections are duplicates

      for(let step = 1; step < 4; step++) {

        var film = results[Math.floor(Math.random() * results.length)];

        var film_title = film[1]
        var film_year = film[0]
        var film_amount = film[2]

        $( "h4.film-" + step + "-title" ).text(film_title);
        $( "h1.film-" + step + "-body" ).text(film_title);
        $( "p.film-" + step + "-release" ).text(film_year);
      }

    });
});
