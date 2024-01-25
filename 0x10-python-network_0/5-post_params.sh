#!/bin/bash
# This script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -sX POST -d "email=5-post_params.sh&subject=I will always be here for PLD" "$1"
