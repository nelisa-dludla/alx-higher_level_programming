#!/usr/bin/node

function factorial (num) {
  if (Number.isNaN(num) || num === 0 || num === 1) {
    return 1;
  } else {
    let result = 1;

    for (let i = 2; i <= num; i++) {
      result *= i;
    }
    return result;
  }
}

const args = process.argv;
const num = parseInt(args[2], 10);

const result = factorial(num);
console.log(result);
