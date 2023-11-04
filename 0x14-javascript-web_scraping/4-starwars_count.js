#!/usr/bin/node
const request = require('request');
let nFilms = 0;

request(process.argv[2], (err, response, body) => {
  if (!err && response.statusCode === 200) {
    const results = JSON.parse(body).results;
    for (let i = 0; i < results.length; i++) {
      nFilms += results[i].characters.some(character => character.includes('18'));
    }
  }
  console.log(nFilms);
});
