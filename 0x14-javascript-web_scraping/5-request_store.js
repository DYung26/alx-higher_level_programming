#!/usr/bin/node

const request = require('request');
const args = process.argv;
const fs = require('fs');

request(`${args[2]}`, (error, response, body) => {
  if (error) {
    return;
  }
  fs.writeFile(`${args[3]}`, `${body}`, 'utf8', (err) => {
    if (err) {
      return;
    }
  });
});
