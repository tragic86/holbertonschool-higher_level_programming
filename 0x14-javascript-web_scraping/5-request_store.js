#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const urls = process.argv[2];
const path = process.argv[3];
request(urls).pipe(fs.createWriteStream(path, 'utf8'));
