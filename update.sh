#!/bin/bash

git pull

sudo nohup python api.py > log.txt 2>&1 &
