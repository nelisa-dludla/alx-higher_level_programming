#!/usr/bin/node

const args = process.argv;
const size = parseInt(args[2], 10);

if (!Number.isNaN(size)) {
  let i = 0;

  while (i < size) {
    let j = 0;
    while (j < size) {
      process.stdout.write('#');
      j++;
    }
    console.log();
    i++;
  }
} else {
  console.log('Missing size');
}
