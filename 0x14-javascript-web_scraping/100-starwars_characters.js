#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
request(url + id, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const characters = data.characters;
  for (const i of characters) {
    request(i, function (error, res, body1) {
      if (error) {
        console.log(error);
      }
      const charDetails = JSON.parse(body1);
      console.log(charDetails.name);
    });
  }
});
