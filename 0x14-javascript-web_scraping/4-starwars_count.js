#!/usr/bin/node

const request = require('request');
const args = process.argv;

request(`${args[2]}`, (error, response, body) => {
  const moviesArray = JSON.parse(response.body).results;
  let count = 0;
  for (let i = 0; i < moviesArray.length; i++) {
    if (error) {
      return;
    }
    const charactersArray = moviesArray[i].characters;
    for (let j = 0; j < charactersArray.length; j++) {
      if (charactersArray[j].replace(/\D/g, '') === '18') {
        count += 1;
      }
    }
  }
  console.log(count);
});
