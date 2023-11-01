#!/usr/bin/node
/*
fetches and lists the title for all movies
by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
*/

$.get(
  'https://swapi-api.alx-tools.com/api/films/?format=json',
  (data, textStatus) => {
    const movies = data.results;
    $.each(movies, (i, movie) => {
      $('ul#list_movies').append(`<li>${movie.title}</li>`);
    });
  }
);
