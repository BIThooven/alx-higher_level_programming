#/bin/bash
# Display all HTTP method the server will accept
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
