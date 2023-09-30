#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, current) => {
    if (current === searchElement) return count + 1;
    return count;
  }, 0);
};
