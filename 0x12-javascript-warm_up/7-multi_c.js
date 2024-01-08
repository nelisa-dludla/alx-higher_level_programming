#!/usr/bin/node

const args = process.argv;
const x = parseInt(args[2], 10);

if (x > 0) {
  let i = 0;

  while (i < x) {
    console.log('C is fun');
    i++;
  }
} else if (Number.isNaN(x)) {
  console.log('Missing number of occurrences');
}
