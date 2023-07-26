#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const file = process.argv[3];

request(url, function (error, response, body) {
  if (!error) {
    try {
      fs.writeFileSync(file, body, 'utf8');
    } catch (error) {
      console.log(error);
    }
  }
});
