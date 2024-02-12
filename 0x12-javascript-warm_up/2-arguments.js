#!/usr/bin/node

// chacks the number of arguments
const keyarg = process.argv.length - 2;

if (keyarg === 0) {
  console.log('No argument');
} else if (keyarg === 1) {
  console.log('Argument found');
} else {
  console.log('Argument found');
}
