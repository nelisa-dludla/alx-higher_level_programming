#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

const findActor = (obj, id) => {
  let isFound = false;

  for (let i = 0; i < obj.characters.length; i++) {
    if (obj.characters[i] === 'https://swapi-api.alx-tools.com/api/people/18/') {
      isFound = true;
    }
  }

  return !!(isFound);
};

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const responseBody = JSON.parse(body);

    const results = responseBody.results.map(findActor);

    const numFound = results.filter((result) => result === true);

    console.log(numFound.length);
  }
}
);
