#!/usr/bin/node

const request = require('request');
const args = process.argv;

request(`${args[2]}`, (error, response, body) => {
  if (error) {
    return;
  }
  console.log(`code: ${response.statusCode}`);
});
