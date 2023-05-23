#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url, (error, response, data) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const films = JSON.parse(data);
  const charactersUrls = films.characters;

  const charactersPromises = charactersUrls.map(characterUrl => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          reject(error);
          return;
        }

        const character = JSON.parse(body);
        resolve(character.name);
      });
    });
  });

  Promise.all(charactersPromises)
    .then(characters => {
      console.log(characters.join('\n'));
    })
    .catch(error => {
      console.error('Error:', error);
    });
});
