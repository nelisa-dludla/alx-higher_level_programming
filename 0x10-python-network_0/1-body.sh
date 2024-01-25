#!/bin/bash
# This script that takes in a URL, sends a GET request to the URL, and displays the body of the response

server=$1

if [[ ${server:0:4} == "http" ]]; then
        url="$server"
else
        url=http://"$server"
fi

curl -sL "$url"
