#!/usr/bin/node
const { list } = require('./100-data.js');
console.log('Original list:', list);
console.log('Mapped list:', list.map((item, index) => item * index));
