#!/bin/bash
# This script takes in a URL, sends a request to that URL, and displays the size of the body of response

server=$1

if [[ ${server:0:4} == "http" ]]; then
        url=$server
else
        url=http://$server
fi

curl -s "$url" | wc -c
