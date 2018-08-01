#!/bin/bash
#script to post arg
curl -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
