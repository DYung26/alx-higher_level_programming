#!/usr/bin/node

const request = require('request');
const args = process.argv;
const moviesEndpoint = `https://swapi-api.alx-tools.com/api/films/${args[2]}`;

request(`${moviesEndpoint}`, (error, response, body) => {
  if (error) {
    return;
  }

  const charactersArray = JSON.parse(response.body).characters;
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
