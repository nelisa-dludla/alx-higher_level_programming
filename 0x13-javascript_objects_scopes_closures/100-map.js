#!/usr/bin/node

const data = require('./100-data.js');
const list = data.list;

let i = 0;

const newList = list.map(item => {
  const result = item * i;
  i++;

  return result;
});

console.log(list);
console.log(newList);
