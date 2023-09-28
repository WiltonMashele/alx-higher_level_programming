#!/bin/bash
# sends a request to that URL, and displays the size of the body of the response
size=$(curl -sI "$1" | wc -c)
echo "Size of the HTTP response header: $size bytes"
