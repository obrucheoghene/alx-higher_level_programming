#!/usr/bin/node
const process = require('process');
const fs = require('fs');

if (process.argv.length < 3) {
  process.stderr.write('Usage: ./O-readme.js <filename>');
  process.exit();
}

const file = process.argv[2];
try {
  const data = fs.readFileSync(file, 'utf8');
  console.log(data);
} catch (error) {
  console.log(error);
}
