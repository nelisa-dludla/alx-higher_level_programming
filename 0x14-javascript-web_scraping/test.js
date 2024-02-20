#!/usr/bin/node

const request = require('request')
const url = 'https://swapi-api.alx-tools.com/api/people/1/'

const getNames = (url) => {
	request( url, (err, res, body) => {
		if (err) {
			console.error(err);
		} else {
			const resBody = JSON.parse(body);
			console.log(resBody)
		}
	});
}

getNames(url);
