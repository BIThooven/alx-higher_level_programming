#!/usr/bin/node

const keyarg = Math.floor(Number(process.argv[2]));
const keyargs = Math.floor(Number(process.argv[3]));
function add (a, b) {
  return (a + b);
}

console.log(add(keyarg, keyargs));
