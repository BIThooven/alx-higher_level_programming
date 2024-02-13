#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];
  let i = list.length - 1;
  for (let count = 0; count < list.length; count++) {
    reversedList[count] = list[i];
    i--;
  }
  return reversedList;
};
