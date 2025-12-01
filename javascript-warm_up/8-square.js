#!/usr/bin/node
const arg = process.argv[2];
const size = parseInt(arg, 10);

if (isNaN(size)) {
  console.log('Missing size');
} else if (size > 0) {
  const row = 'X'.repeat(size);
  for (let i = 0; i < size; i++) {
    console.log(row);
  }
}
