#!/bin/bash

api=$(curl "$3")

python3 absolute_path_to_main.py "$1" "$2" "$api"