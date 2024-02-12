#!/usr/bin/node
const MyNumber = process.argv[2];
if (!parseInt(MyNumber)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${MyNumber}`);
}
