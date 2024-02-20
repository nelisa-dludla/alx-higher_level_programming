#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const completedTasks = {};

const fetchData = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(JSON.parse(body));
      }
    }
    );
  });
};

const fetchAndProcessData = async () => {
  for (let i = 1; i <= 10; i++) {
    const currentUrl = `${url}?userId=${i}`;
    const resBody = await fetchData(currentUrl);
    const completedArr = resBody.filter((item) => {
      return item.completed === true;
    });

    completedTasks[`${i}`] = completedArr.length;
  }

  console.log(completedTasks);
};

fetchAndProcessData();
