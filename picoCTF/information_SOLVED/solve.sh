#!/bin/bash

IMG_URL="https://mercury.picoctf.net/static/d1375e383810d8d957c04eef9e345732/cat.jpg"

curl -O --silent $IMG_URL

exiftool cat.jpg \
| grep License \
| sed 's/\s//g' \
| cut -d ':' -f 2 \
| base64 -d