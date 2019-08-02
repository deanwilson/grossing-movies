$(document).ready(function() {

  var highest_amount = 100;
  var highest_title = '';

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

      for(let step = 1; step < 4; step++) {

        var film = results[Math.floor(Math.random() * results.length)];

        var film_title  = film[1]
        var film_year   = film[0]
        var film_earnings = film[2];
        var sanitised_earnings = parseInt(film_earnings.replace(/,/g, ""));

        $( "h4.film-" + step + "-title" ).text(film_title);
        $( "h1.film-" + step + "-body" ).text(film_title);
        $( "h1.film-" + step + "-body" ).text(film_earnings);
        $( "p.film-" + step + "-release" ).text(film_year);

        if (sanitised_earnings > highest_amount) {
          // alert("In if: " + film_title + " " + film_earnings + " Current " + highest_title + " " + highest_amount);
          highest_title = film_title;
          highest_amount = sanitised_earnings;
        }
      }

      // alert("Hightest earning is " + highest_title);

    });

  for(let card of [1, 2, 3]) {
    $(".film-" + card + "-card").click("Hello", function (msg) {
      clicked_title = $("h4.film-" + card + "-title").text();

      if (clicked_title === highest_title) {
        $(".film-" + card + "-card").css('background-color', 'green');
      } else {
        $(".film-" + card + "-card").css('background-color', 'red');
      }
    });
  }

});
