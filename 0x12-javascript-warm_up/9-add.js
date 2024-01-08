#!/usr/bin/node

const args = process.argv;
const [x, y] = args.slice(-2);

function add (a, b) {
  const sum = parseInt(a, 10) + parseInt(b, 10);
  console.log(sum);
}

add(x, y);
