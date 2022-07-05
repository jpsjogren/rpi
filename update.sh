#!/bin/bash

rm -r rpi

git clone git@github.com:jpsjogren/rpi.git

sudo nohup python test.py > log.txt 2>&1 &
