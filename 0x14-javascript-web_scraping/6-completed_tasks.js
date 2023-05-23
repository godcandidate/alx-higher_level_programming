#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const tasksDone = {};
    const tasks = JSON.parse(body);
    tasks.forEach((todo) => {
      if (todo.completed) {
        if (tasksDone[todo.userId]) {
          tasksDone[todo.userId]++;
        } else {
          tasksDone[todo.userId] = 1;
        }
      }
    });
    console.log(tasksDone);
  }
});
