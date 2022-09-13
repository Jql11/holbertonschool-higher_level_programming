#!/usr/bin/node

const axios = require('axios');
const url = process.argv[2];

axios.get(url)
  .then(response => {
    const tasks = response.data;
    const dict = {};
    let count = 0;
    for (const i in tasks) {
      dict[tasks[i].userId]++;
      const completion = tasks[i].completed;
      if (completion) {
        count++;
      }
    }
    console.log(dict);
  })
  .catch(error => {
    console.error(error);
  });
