#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const urlApi = 'https://swapi-api.hbtn.io/api/films/' + movieId;
request(urlApi, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    displayCharacters(characters, 0);
  }
});

function displayCharacters (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        displayCharacters(characters, index + 1);
      }
    }
  });
}
