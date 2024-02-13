#!/usr/bin/node

const a = process.argv.length;
const b = process.argv.map(Number);
if (a <= 3) {
  console.log(0);
} else {
  const sortednums = b.slice(2, a).sort((arg, args) => args - arg);
  console.log(sortednums[1]);
}
