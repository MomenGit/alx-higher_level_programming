#!/usr/bin/node

const { argv } = require('process');

const args_length = argv.length - 2;

if (args_length === 0) {
  console.log('No argument');
} else if (args_length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
