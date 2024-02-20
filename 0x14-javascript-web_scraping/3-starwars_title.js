#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const responseBody = JSON.parse(body);
    console.log(responseBody.title);
  }
}
);
