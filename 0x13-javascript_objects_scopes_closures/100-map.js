#!/usr/bin/node
const { list } = require('./100-data.js');
console.log('Initial list:', list);
const newList = list.map((item, index) => item * index);
console.log('New list:', newList);
