#!/usr/bin/node

const array = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let count = 0;
for (count in array) {
  console.log(array[count++]);
}
