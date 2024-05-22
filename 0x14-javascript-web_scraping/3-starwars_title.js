#!/usr/bin/node

const request = require('request');
const args = process.argv;
const endpoint = 'https://swapi-api.alx-tools.com/api/films/';

request(`${endpoint}${args[2]}`, (error, response, body) => {
  if (error) {
    return;
  }
  console.log(JSON.parse(response.body).title);
});
