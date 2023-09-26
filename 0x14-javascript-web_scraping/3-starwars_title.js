#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  process.exit(1);
}

const episode = process.argv[2];

const apiUrl = 'https://swapi-api.hbtn.io/api/films/';

request(apiUrl + episode, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const jsonResponse = JSON.parse(body);
    console.log(jsonResponse.title);
  } else {
    console.log('Error code : ' + response.statusCode);
  }
});
