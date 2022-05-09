#!/bin/bash

insult=$(curl "https://insult.mattbas.org/api/insult")

python3 absolute_path_to_main.py "$1" c "$insult"