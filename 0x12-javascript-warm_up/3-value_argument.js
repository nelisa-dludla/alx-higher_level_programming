#!/usr/bin/node

const args = process.argv;
const firstArg = args.splice(2, 1);

if (typeof (firstArg[0]) === 'string') {
  console.log(firstArg[0]);
} else {
  console.log('No argument');
}
