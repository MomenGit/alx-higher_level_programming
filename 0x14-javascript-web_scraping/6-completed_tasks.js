#!/usr/bin/node
// computes the number of tasks completed by user id
const request = require('request');
const process = require('process');

const usersCompleted = {};
function computeCompleted (todos) {
  for (const todo of todos) {
    if (usersCompleted[todo.userId]) {
      usersCompleted[todo.userId] += 1;
    } else {
      usersCompleted[todo.userId] = 1;
    }
  }
}

request(`${process.argv[2]}?completed=true`, (err, res, body) => {
  if (err) console.log(err);
  else computeCompleted(JSON.parse(body));
  console.log(usersCompleted);
});
