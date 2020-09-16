#!/usr/bin/node

if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurances');
} else {
  for (let i = 0; i >= 0 && i < process.argv[2]; i++) {
    console.log('C is fun');
  }
}
