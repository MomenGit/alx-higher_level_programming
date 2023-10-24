#!/usr/bin/node
// comment
const request = require('request');
const process = require('process');
const fs = require('fs');

request.get(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(process.argv[3], body, 'utf-8', (error) => {
      if (error) console.log(error);
    });
  }
});
