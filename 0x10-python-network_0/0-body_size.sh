#!/bin/bash
#script to take url send request and send body

curl -sI "$1" | grep 'Content-Length:' | cut -d ':' -f2
