#!/usr/bin/node

const { argv } = require('process');

const arr = argv.slice(2);

if (arr.length <= 1) console.log(0);

let biggest = arr[0];
let second = biggest;
arr.forEach((element) => {
  if (element > biggest) {
    second = biggest;
    biggest = element;
  }
});
console.log(second);
