#!/bin/bash

# $1 takes the file passed as an argument
input_file="$1"

# Creates a new filename by appending '_converted.csv'
output_file="${input_file%.*}_converted.csv"

# Replace semicolons with commas and write out to the new file
tr ';' ',' < "$input_file" > "$output_file"

echo "Converted $input_file and saved as $output_file"