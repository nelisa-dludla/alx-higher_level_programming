#!/bin/bash
# This script that sends a DELETE request to the URL passed as the first argument and displays the body of the response

server=$1

if [[ ${server:0:4} ]]; then
        url="$server"
else
        url=http://"$server"
fi

curl -sX DELETE "$url"
