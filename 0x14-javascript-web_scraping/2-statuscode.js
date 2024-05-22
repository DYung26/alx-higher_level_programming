#!/usr/bin/node

const request = require('request');
const args = process.argv

request(`${args[2]}`, (error, response, body) => {
  console.log(`code: ${response.statusCode}`);
})
