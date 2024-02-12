#!/usr/bin/node

const array = ['C is fun', 'Python is cool', 'Javascript is amazing'];
let count = 0;
for (count in array) {
  console.log(array[count++]);
}
