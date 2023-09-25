#!/usr/bin/node
function add(a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('Error: Both arguments must be valid numbers.');
    return;
  }
  console.log(a + b);
}

const num1 = Number(process.argv[2]);
const num2 = Number(process.argv[3]);

if (num1 === undefined || num2 === undefined) {
  console.log('Error: Please provide two numbers as arguments.');
} else {
  add(num1, num2);
}
