#!/bin/bash
# sends a request to that URL, and displays the size of the body of the response
[ -z "$1" ] && { echo "Usage: $0 <URL>"; exit 1; }
curl -sI "$1" | wc -c
