#!/usr/bin/node
const number = parseInt(process.argv[2]);
const factorial = (num) => {
  if (isNaN(num) || num <= 1) {
    return 1;
  }
  return num * factorial(num - 1);
};
console.log(factorial(number));
