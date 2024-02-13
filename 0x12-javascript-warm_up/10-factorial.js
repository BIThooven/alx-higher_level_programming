#!/usr/bin/node

const inputArg = (process.argv[2]);
const inputargument = parseInt(inputArg);
function computeFactorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * computeFactorial(n - 1);
  }
}
if (isNaN(inputargument)) {
  console.log(1);
} else {
  console.log(computeFactorial(inputargument));
}
