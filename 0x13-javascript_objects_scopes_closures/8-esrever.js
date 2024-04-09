#!/usr/bin/node
exports.esrever = function (list) {
  let length = list.length - 1;
  let start = 0;
  while ((length - start) > 0) {
    const temp = list[length];
    list[length] = list[start];
    list[start] = temp;
    start++;
    length--;
  }
  return list;
};
