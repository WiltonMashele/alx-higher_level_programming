#!/usr/bin/node
const fs = require('fs');

fs.promises.readFile(process.argv[2], 'utf8')
  .then(content => console.log(content))
  .catch(error => console.error(error));
