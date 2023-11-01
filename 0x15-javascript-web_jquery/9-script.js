$.get('https://swapi.dev/api/films/', function (data) {
  $('#list_movies').append(
    data.results.map(movie => `<li>${movie.title}</li>`).join('')
  );
});
