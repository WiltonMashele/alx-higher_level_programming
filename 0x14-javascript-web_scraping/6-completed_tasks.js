#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (!err && response.statusCode === 200) {
    const json = JSON.parse(body);
    const resp = json.reduce((acc, item) => {
      if (item.completed) {
        acc[item.userId] = (acc[item.userId] || 0) + 1;
      }
      return acc;
    }, {});
    console.log(resp);
  }
});
