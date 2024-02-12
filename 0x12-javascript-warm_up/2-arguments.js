#!/usr/bin/node

// chacks the number of arguments
const keyarg = process.argv.length;

console.log(keyarg === 2 ? 'No argument' : keyarg === 3 ? 'Argument found' : 'Argument found');
