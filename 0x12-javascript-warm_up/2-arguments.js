#!/usr/bin/node
const keyargs = process.argv.length - 2;
console.log(keyargs === 0 ? 'No argument' : keyargs === 1 ? 'Argument found' : 'Arguments found');
