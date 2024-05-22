#!/usr/bin/node

const fs = require('fs');

const args = process.argv;

fs.writeFile(`${args[2]}`, `${args[3]}`, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  }
});
