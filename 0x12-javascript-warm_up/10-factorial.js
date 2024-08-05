#!/usr/bin/node

const n = Number(process.argv[2]);

function recursive (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  }
  if (n === 1) {
    return 1;
  }
  return (n * recursive(n - 1));
}

console.log(recursive(n));
