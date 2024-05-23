#!/usr/bin/node

const request = require('request');
const args = process.argv;

request(`${args[2]}`, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const todosList = JSON.parse(response.body);
  const idCtask = {};
  for (let i = 0; i < todosList.length; i++) {
    if (!idCtask[todosList[i].userId]) {
      idCtask[todosList[i].userId] = 0;
    }
    if (todosList[i].completed) {
      idCtask[todosList[i].userId]++;
    }
  }
  console.log(idCtask);
});
