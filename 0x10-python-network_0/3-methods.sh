#!/bin/bash
# This script that takes in a URL and displays all HTTP methods the server will accept

server=$1

if [[ ${server:0:4} == "http" ]]; then  
        url="$server"
else
        url=http://"$server"
fi

curl -sI "$url" | awk -F ': ' '/Allow/ {print $2}'
