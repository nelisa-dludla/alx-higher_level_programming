#!/bin/bash
# This script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response

server=$1

if [[ ${server:0:4} == "http" ]]; then
        url="$server"
else
        url=http://"$server"
fi

email="test@gmail.com"
subject="I will always be here for PLD"

curl -sX POST -d "email=$email&subject=$subject" "$url"
