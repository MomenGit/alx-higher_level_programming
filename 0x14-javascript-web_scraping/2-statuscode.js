#!/usr/bin/node
// display the status code of a GET request
const request = require('request');
const process = require('process');

request.get(process.argv[2], (err, res, body) => {
  if (err) console.log(err);
  else console.log('code: ', res && res.statusCode);
});
