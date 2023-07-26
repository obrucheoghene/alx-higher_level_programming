#!/usr/bin/node
const process = require('process');
const request = require('request');

const api = 'https://swapi-api.alx-tools.com/api/films';
const movieId = process.argv[2];

request(`${api}/${movieId}`, function (error, response, body) {
  if (!error) {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
