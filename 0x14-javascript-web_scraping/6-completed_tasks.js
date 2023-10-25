#!/usr/bin/node
// computes the number of tasks completed by user id
const request = require('request');
const process = require('process');

const usersCompleted = {};
function computeCompleted (todos) {
  for (const todo of todos) {
    if (todo.completed === true) {
      if (usersCompleted[todo.userId]) {
        usersCompleted[todo.userId] += 1;
      } else {
        usersCompleted[todo.userId] = 1;
      }
    }
  }
}

request(`${process.argv[2]}`, (err, res, body) => {
  if (err) console.log(err);
  else computeCompleted(JSON.parse(body));
  console.log(usersCompleted);
});
