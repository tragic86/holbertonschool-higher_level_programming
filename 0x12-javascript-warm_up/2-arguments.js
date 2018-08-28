#!/usr/bin/node
let arg = process.argv;
if (arg.length > 3) {
  console.log('Arguments found');
} else if (arg.length < 3) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
