#!/usr/bin/node

const req = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

req.get(url, (error, res, body) => {
  if (error) return console.log(error);

  const data = JSON.parse(body);
  data.characters.forEach((characterUrl) => {
    req.get(characterUrl, (error, res, body1) => {
      if (error) return console.log(error);

      const data1 = JSON.parse(body1);
      console.log(data1.name);
    });
  });
});
