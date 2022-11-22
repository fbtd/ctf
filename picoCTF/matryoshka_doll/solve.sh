#!/bin/bash

wget "https://mercury.picoctf.net/static/2978e1270538613cd8181c7b0dabe9bd/dolls.jpg"

binwalk -e -M dolls.jpg
find . -iname '*.txt' -exec cat {} \;
echo ""

# cleanup
rm -r _dolls.jpg.extracted/