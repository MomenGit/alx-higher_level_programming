#!/usr/bin/node

const { argv } = require('process');

function factorial (num) {
  if (isNaN(num) || num === 0) return 1;
  return num * factorial(num - 1);
}

const num = parseInt(argv[2]);

console.log(factorial(num));
