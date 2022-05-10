#!/bin/bash

api=$(curl "$3")

python3 /Users/tyler/Desktop/SMS-Messages/src/main.py "$1" "$2" "$api"