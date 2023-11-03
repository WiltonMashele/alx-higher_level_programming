#!/usr/bin/node

const axios = require('axios');
const apiUrl = process.argv[2];
const characterId = process.argv[3];

if (!apiUrl || !characterId) {
  console.error('Usage: node script.js <API_URL> <character_id>');
} else {
  axios.get(apiUrl)
    .then((response) => {
      const nFilms = response.data.results.reduce((count, result) => {
        return count + result.characters.filter((character) => character.includes(characterId)).length;
      }, 0);
      console.log(nFilms);
    })
    .catch((error) => {
      console.error('An error occurred:', error);
    });
}
