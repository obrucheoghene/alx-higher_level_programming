#!/usr/bin/node
const process = require('process');
const fs = require('fs');

if (process.argv.length < 4) {
  console.log('Usage ./1-writeme.js <file_path> <text> ');
}

const file = process.argv[2];
const text = process.argv[3];

try {
  fs.writeFileSync(file, text, 'utf8');
} catch (error) {
  console.log(error);
}
