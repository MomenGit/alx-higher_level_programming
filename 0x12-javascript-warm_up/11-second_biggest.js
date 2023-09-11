#!/usr/bin/node

const { argv } = require('process');

const args = argv.slice(2); // Get the command-line arguments (excluding the first two)
const numbers = args.map(Number); // Convert the arguments to numbers

if (numbers.length <= 1) {
  console.log(0); // If no arguments or only one argument is passed, print 0
} else {
  // Sort the numbers in descending order
  numbers.sort((a, b) => b - a);

  // Find the second biggest number (at index 1)
  const secondBiggest = numbers[1];
  console.log(secondBiggest);
}
