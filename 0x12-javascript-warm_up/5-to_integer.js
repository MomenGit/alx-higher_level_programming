#!/usr/bin/node

const { argv } = require('process');

const number = parseInt(argv[2]);

if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number:', number);
}
