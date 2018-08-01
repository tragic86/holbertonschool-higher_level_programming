#!/bin/bash
#script to find only certain prams
curl -sI "$1" | grep 'Allow' | cut -d ' ' -f2
