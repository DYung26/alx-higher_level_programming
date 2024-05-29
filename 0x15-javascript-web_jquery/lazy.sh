#!/bin/bash

echo "Enter file name:"
read -e file_name # `-e` option to enable line editing

git add "$file_name"

echo "Enter Your Commit Message:"
# read -e commit_msg

echo "Enter multiline input. Type 'END' on a new line to finish:"
commit_msg=""
while IFS= read -e -r line && [ "$line" != "END" ]; do
    commit_msg+="$line"$'\n'
done

echo "Multiline input received:"
echo "$commit_msg"


git commit -m "$commit_msg"

git push
