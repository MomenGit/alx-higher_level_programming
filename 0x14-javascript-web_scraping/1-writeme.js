#!/usr/bin/node
// writes a string to a file
const fs = require('fs');
const { argv } = require('process');

fs.writeFile(argv[2], argv[3], 'utf-8', (err) => {
  if (err) console.log(err);
});
