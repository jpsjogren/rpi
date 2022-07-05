#!/bin/bash

git pull
cd src

sudo nohup python api.py > log.txt 2>&1 &
