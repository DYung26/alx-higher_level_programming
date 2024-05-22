#!/usr/bin/node

fs = require('fs');

args = process.argv;

fs.writeFile(`${args[2]}`, `${args[3]}`, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  }
});
