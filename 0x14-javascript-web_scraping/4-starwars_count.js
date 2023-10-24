#!/usr/bin/node
// comment
const request = require('request');
const process = require('process');

request.get(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(body).results;
    const charFilms = films.reduce((count, film) => {
      return film.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0);

    console.log(charFilms);
  }
});
