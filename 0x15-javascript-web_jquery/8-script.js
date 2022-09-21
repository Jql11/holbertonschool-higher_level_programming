$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $.each(data.results, function (key, val) {
    $('#list_movies').append('<li>' + val.title + '</li>');
  });
});
