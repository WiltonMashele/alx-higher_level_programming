#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl --silent --header "Content-Type: application/json" --data "$(cat "$2")" "$1"
