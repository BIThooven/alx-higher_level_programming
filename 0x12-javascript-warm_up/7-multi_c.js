#!/usr/bin/node

const keyargs = Math.floor(Number(process.argv[2]));
const C = 'C is fun';
let count;
if (!parseInt(keyargs)) {
  console.log('Missing number of occurrences');
} else {
  for (count = 0; count < keyargs; count++) {
    console.log(C);
  }
}
