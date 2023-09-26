#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const apiUrl = 'https://swapi-api.hbtn.io/api/films/';
request.get(apiUrl + movieId, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const info = JSON.parse(body);
  const data = info.characters;
  for (const i of data) {
    request.get(i, function (error, response, body) {
      if (error) {
        console.error(error);
      }
      const information = JSON.parse(body);
      console.log(information.name);
    });
  }
});
