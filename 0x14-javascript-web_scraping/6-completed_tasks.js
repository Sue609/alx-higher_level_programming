#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  process.exit(1);
}

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const complete = {};
    const todos = JSON.parse(body);
    for (const task of todos) {
      const todo = task;
      if (todo.completed === true) {
        if (complete[todo.userId] === undefined) {
          complete[todo.userId] = 1;
        } else {
          complete[todo.userId]++;
        }
      }
    }
    console.log(complete);
  } else {
    console.error('An error occurred. Status code: ' + response.statusCode);
  }
});
