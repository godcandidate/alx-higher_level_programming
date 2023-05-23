#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const character = "https://swapi-api.alx-tools.com/api/people/18/";

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    const result = films.filter((film) => film.characters.includes(character));
    console.log(result.length);
  }
});
