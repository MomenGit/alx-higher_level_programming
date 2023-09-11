#!/usr/bin/node

const { argv } = require('process');

const argsLength = argv.length - 2;

if (argsLength === 0) {
  console.log('No argument');
} else if (argsLength === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
