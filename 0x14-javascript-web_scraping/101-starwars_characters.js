#!/usr/bin/node
// prints the title of a Star Wars movie where the episode number matches a given integer
const request = require('request');
const process = require('process');

const movieId = process.argv[2];

function fetchCharacterNames (characterUrls, index) {
  if (index >= characterUrls.length) return;

  request.get(characterUrls[index], (err, res, body) => {
    if (!err) {
      const character = JSON.parse(body);
      console.log(character.name);
      fetchCharacterNames(characterUrls, index + 1);
    }
  });
}

request.get(
  `https://swapi-api.alx-tools.com/api/films/${movieId}`,
  (err, res, body) => {
    if (err) {
      console.log(err);
    } else {
      const filmData = JSON.parse(body);
      const charactersUrls = filmData.characters;
      fetchCharacterNames(charactersUrls, 0);
    }
  }
);
