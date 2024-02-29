#!/bin/bash
# sending a POST request to the URL and display the body of the response
sudo curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
