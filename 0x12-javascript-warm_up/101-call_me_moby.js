#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  Array.from({ length: x }, theFunction);
};
