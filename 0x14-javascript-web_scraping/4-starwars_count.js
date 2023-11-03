#!/usr/bin/node

const request = require('request');

const apiURL = 'https://swapi-api.alx-tools.com/api/films/';
const characterId = '18';

request(apiURL, (error, response, body) => {
  if (!error) {
    const films = JSON.parse(body).results;
    const filmsWithWedgeAntilles = films.filter((film) => {
      return film.characters.some((character) => character.endsWith(`/${characterId}/`));
    });

    console.log(filmsWithWedgeAntilles.length);
  }
});
