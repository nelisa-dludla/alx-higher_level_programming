#!/usr/bin/node

exports.esrever = function (list) {
  const sortedList = [];

  for (let i = list.length; i > 0; i--) {
    sortedList.push(list[i - 1]);
  }

  return sortedList;
};
