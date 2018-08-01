#!/bin/bash
#script to find only certain prams
curl -s -I "$1" | grep 'Allow' | cut -d ' ' -f2
