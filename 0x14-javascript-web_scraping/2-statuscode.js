#!/usr/bin/node
const process = require('process');
const request = require('request');

if (process.argv.length < 3) {
  process.stderr.write('Usage: ./2-statuscode.js <url>');
  process.exit();
}

const url = process.argv[2];
request(url, function (error, response) {
  if (!error) {
    console.log('code: ', response.statusCode);
  }
});
