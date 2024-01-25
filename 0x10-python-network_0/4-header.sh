#!/bin/bash
# This script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response

server=$1

if [[ ${server:1:4} == "http" ]]; then
        url="$server"
else
        url=http://"$server"
fi

curl -sH "X-School-User-Id: 98" "$url"
