#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}/`;

const fetchName = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (err) {
        reject(err);
      } else {
        const resBody = JSON.parse(body);
        resolve(resBody.name);
      }
    });
  });
};

const fetchAndProcessNames = async () => {
  request(filmUrl, async (err, res, body) => {
    if (err) {
      console.error(err);
    } else {
      const resBody = JSON.parse(body);
      const charactersArr = resBody.characters;
      const characterNames = await Promise.all(charactersArr.map(async (characterUrl) => fetchName(characterUrl)));

      for (let i = 0; i < characterNames.length; i++) {
        console.log(characterNames[i]);
      }
    }
  }
  );
};

fetchAndProcessNames();
