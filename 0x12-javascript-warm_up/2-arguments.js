#!/usr/bin/node

// chacks the number of arguments
const keyarg = process.argv.length - 2;

console.log(keyarg === 0 ? 'No argument' : keyarg === 1 ? 'Argument found' : 'Argument found');
