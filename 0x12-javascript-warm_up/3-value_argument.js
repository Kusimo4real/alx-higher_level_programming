#!/usr/bin/node

// if (process.argv[1] === '') {
//  console.log('No Argument');
// }
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
