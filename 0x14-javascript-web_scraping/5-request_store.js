#!/usr/bin/node
const fs = require('fs');
require('request')(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
