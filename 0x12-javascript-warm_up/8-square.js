#!/usr/bin/node

if (isNaN(Number(process.argv[2]))) {
  console.log('Missing size');
} else {
  for (let i = 1; i <= process.argv[2]; i++) {
    let s = '';
    for (let j = 1; j <= process.argv[2]; j++) {
      s += 'X';
    }
    console.log(s);
  }
}
