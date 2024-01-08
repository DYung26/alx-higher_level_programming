#!/bin/bash

echo "Enter file name:"
read file_name

git add "${file_name}"

echo "Enter Your Commit Message:"
read commit_msg

git commit -m "${commit_msg}"

git push
