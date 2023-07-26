#!/usr/bin/node
const process = require('process');
const request = require('request');

const url = process.argv[2];
const records = {};

request(url, function (error, response, body) {
  if (!error) {
    const data = JSON.parse(body);
    data.forEach(todo => {
      if (todo.completed) {
        if (records[todo.userId]) {
          records[todo.userId]++;
        } else {
          records[todo.userId] = 0;
        }
      }
    });
    console.log(records);
  }
});
