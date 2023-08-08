$($(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json',
    function (data, status) {
      data.results.forEach(film => {
        $('UL#list_movies').append(`<li>${film.title}</li>`);
      });
    });
}));
