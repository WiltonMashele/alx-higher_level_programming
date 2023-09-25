#!/usr/bin/node
const input = process.argv[2];
const size = parseInt(input);

if (isNaN(size) || size < 1) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
