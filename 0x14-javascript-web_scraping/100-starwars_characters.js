#!/usr/bin/node
const request = require('request-promise');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

(async () => {
  try {
    const film = await request(url, { json: true });
    const characterNames = await Promise.all(
      film.characters.map(async (character) => {
        const characterData = await request(character, { json: true });
        return characterData.name;
      })
    );

    console.log(characterNames);
  } catch (error) {
    console.error('Error:', error.message);
  }
})();
