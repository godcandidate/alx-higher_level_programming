#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filePath = process.argv[3];

request(url, 'utf-8', (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(filePath, body, (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
