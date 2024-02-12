#!/usr/bin/node

const keyargs = Math.floor(Number(process.argv[2]));
let count;
if (!parseInt(keyargs)) {
  console.log('Missing size');
} else {
  for (count = 0; count < keyargs; count++) {
    let rows = '';
    for (let row = 0; row < keyargs; row++) {
      rows += 'X';
    }
    console.log(rows);
  }
}
