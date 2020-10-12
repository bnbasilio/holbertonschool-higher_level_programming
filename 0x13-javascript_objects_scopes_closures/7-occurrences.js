#!/usr/bin/node
// returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let number = 0;
  for (const item of list) {
    if (item === searchElement) {
      number++;
    }
  }
  return number;
};
