#!/usr/bin/node
const process = require('process');
const request = require('request');

const api = process.argv[2];

request(api, function (error, response, body) {
  if (!error) {
    const data = JSON.parse(body);
    const movies = data.results
      .filter(movie => movie.characters
        .find(character => character.match(/\/people\/18\/?$/)));
    console.log(movies);
  }
});
