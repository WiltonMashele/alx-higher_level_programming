$.get('https://swapi.dev/api/people/5/', function (data) {
  $('#character').text(data.name);
});
