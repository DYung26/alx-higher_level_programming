#!/usr/bin/node

const request = require('request');
const args = process.argv;
const moviesEndpoint = 'https://swapi-api.alx-tools.com/api/films/';
const charactersEndpoint = 'https://swapi-api.alx-tools.com/api/people/';

request(`${moviesEndpoint}`, (error, response, body) => {
  if (error) {
    return;
  }
  const movie = JSON.parse(response.body).results[args[2]];

  const charactersArray = movie.characters;
  for (let j = 0; j < charactersArray.length; j++) {
    request(`${charactersArray[j]}`, (error, resp, body) => {
      if (error) {
        return;
      }
      const character = JSON.parse(resp.body).name;
      console.log(character);
    });
  }
});
