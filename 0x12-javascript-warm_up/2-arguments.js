#!/usr/bin/node
const count = process.argv.length - 2;
console.log(count === 0 ? 'No argument' : count === 1 ? 'Argument found' : 'Arguments found');
