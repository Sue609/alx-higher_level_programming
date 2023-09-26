#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];

const content = process.argv[3];

if (!filePath || !content) {
  process.exit(1);
}
fs.writeFile(filePath, content, error => {
  if (error) console.log(error);
});
