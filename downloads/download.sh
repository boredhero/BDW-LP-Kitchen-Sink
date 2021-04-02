#!/bin/bash
input="dl_client.txt"
while IFS= read -r line
do
    echo "$line"
    wget "$line"
done < "$input"