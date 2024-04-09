#!/usr/bin/node
const dict = require('./101-data').dict;

const totalList = Object.entries(dict);
const values = Object.values(dict);
const uniqueValues = [...new Set(values)];
const newDict = {};

for (const value of uniqueValues) {
  const list = [];
  for (const pair of totalList) {
    if (pair[1] === value) {
      list.unshift(pair[0]);
    }
  }
  newDict[value] = list;
}

console.log(newDict);
