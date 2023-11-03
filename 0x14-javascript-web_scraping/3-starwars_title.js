#!/usr/bin/node
const request = require('request');
const filmId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const parsedBody = JSON.parse(body);
    console.log(parsedBody.title);
  }
});
