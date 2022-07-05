#!/bin/bash

git pull

sudo nohup python test.py > log.txt 2>&1 &
