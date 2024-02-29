#!/bin/bash
#sending a request to the URL and display methods
sudo curl -I -s $1 | grep "Allow" | cut -d ' ' -f2-
